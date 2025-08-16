# Fake News Detector powered by AI
**A full-stack application for detecting fake news using a fine-tuned BERT model with SHAP visualizations.** <br>
**Demo:** [fake-news-detector-production.vercel.app](https://fake-news-detector-production.vercel.app/) <br>
  - Training Detail with Dataset used in this model available in [here](https://fake-news-detector-production.vercel.app/about) <br>
  
**Model API:** [alexlai7777-fake-news-backend.hf.space](https://alexlai7777-fake-news-backend.hf.space) <br>
**Model for download:** [Fine-tune-model x 3](https://huggingface.co/alexlai7777/fake-news-detector/tree/main)

---
## Notes & Thoughts

After experimentation, I found that the model with highest accuracy comes from:

- Keep all layers of the base BERT model **frozen** except for the last two. (Helps reduce overfit)
- Adding **two custom fully-connected layers** on top
- Keep batch size = 32
- Train no more than 6 epoches. after that, it overfits

This approach balances fine-tuning power with generalization, avoiding overfitting while still adapting the model to the fake news detection task.

---
## Project Structure
fake_news_detector/ <br>
├── frontend/ # Next.js + Tailwind frontend UI <br>
├── backend/ # Python backend with BERT model + SHAP
├── notebook/ # Code from Jupyter Notebook on How I fine-tune my model

---

## Tools & Technologies

**Frontend**
- [Next.js](https://nextjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [React](https://react.dev/)
- [shadcn/ui](https://ui.shadcn.com/)

**Backend**
- [FastAPI](https://fastapi.tiangolo.com/)
- [PyTorch](https://pytorch.org/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [SHAP](https://shap.readthedocs.io/)

**Model**
- Fine-tuned **BERT** model  
- Base: `bert-base-uncased`

---

## Status
> This project is under active development.




