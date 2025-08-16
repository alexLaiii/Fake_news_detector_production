import os
import base64
from io import BytesIO

import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel
from huggingface_hub import hf_hub_download
from model.model_arch import BERT_Arch

import shap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

torch.set_num_threads(int(os.getenv("TORCH_NUM_THREADS", "1")))

HF_REPO    = os.getenv("HF_REPO", "alexlai7777/fake-news-detector")
MODEL_FILE = os.getenv("MODEL_FILE", "fake_news_model.pt")
HF_TOKEN   = os.getenv("HF_TOKEN")

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
bert = AutoModel.from_pretrained("bert-base-uncased")
model = BERT_Arch(bert)

weights_path = hf_hub_download(repo_id=HF_REPO, filename=MODEL_FILE, token=HF_TOKEN)
state_dict = torch.load(weights_path, map_location="cpu")
model.load_state_dict(state_dict)
model.eval()

def get_prediction(text: str):
    enc = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        out = model(enc["input_ids"], enc["attention_mask"])
        probs = torch.exp(out)    # head returns LogSoftmax -> exp to probs
        pred = int(torch.argmax(probs, dim=1))
        conf = float(probs[0][pred])
    return pred, conf

def predict_prob(texts):
    tokens = tokenizer(list(map(str, texts)), return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        out = model(tokens["input_ids"], tokens["attention_mask"])
        probs = torch.exp(out)
    return probs.numpy()

explainer = shap.Explainer(predict_prob, shap.maskers.Text(tokenizer))

def predict_fake_news(statement: str, save_plot_path=None):
    pred_label, base_conf = get_prediction(statement)

    shap_values = explainer([statement])
    sv = shap_values[0]

    token_impacts = []
    for token, value in zip(sv.data, sv.values):
        impact = float(value[pred_label]) if isinstance(value, (list, np.ndarray)) else float(value)
        token_impacts.append((token, impact))
    token_impacts.sort(key=lambda x: abs(x[1]), reverse=True)
    highlights = [tok for tok, _ in token_impacts[:5]]

    plot_data = None
    if save_plot_path:
        plt.clf()
        sv.values = sv.values[:, pred_label]
        sv.base_values = sv.base_values[pred_label]
        shap.plots.waterfall(sv, show=False)
        plt.tight_layout()
        buf = BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        plot_data = f"data:image/png;base64,{base64.b64encode(buf.getvalue()).decode()}"
        plt.close()

    return {
        "label": "fake" if pred_label == 1 else "real",
        "confidence": round(base_conf, 4),
        "highlights": highlights,
        "plot_data": plot_data,
    }
