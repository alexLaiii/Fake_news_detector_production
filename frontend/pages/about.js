export default function About() {
  return (
    <main className="w-full p-6">
      <div className="max-w-2xl mx-auto space-y-6">
        <h1 className="text-2xl font-bold"><strong>About This Project</strong></h1>

        <h4 className="text-lg font-semibold">What is it?</h4>
        <p>
          This Fake News Detector is a machine learning tool built to automatically classify news content as real or fake using a fine-tuned BERT language model.
        </p>

        <h4 className="text-lg font-semibold">Why was it built</h4>
        <p>
          In the age of viral misinformation, detecting fake news is critical. This tool aims to help researchers, educators, and developers explore how NLP and AI can be used to fight misinformation using modern deep learning techniques.
        </p>

        <h4 className="text-lg font-semibold">Performance</h4>
        <p>
          The model achieves around 97% accuracy on the test set, as supported by the confusion matrix:
        </p>
        <div className="mt-4">
          <img
            src="/images/result/confusion_matrix.png"
            alt="Confusion matrix"
            className="max-w-full"
          />
        </div>

        <ul className="list-disc pl-6 space-y-1">
          <li>2119 real news items were correctly predicted as real</li>
          <li>2274 fake news items were correctly predicted as fake</li>
          <li>23 real items were wrongly predicted as fake</li>
          <li>74 fake items were wrongly predicted as real</li>
        </ul>

        <p className="mt-2">
          This model is trained on dataset derived from Kaggle source –{" "}
          <a
            href="https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset"
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-600 underline hover:text-blue-800"
          >
            fake-and-real-news
          </a>
          . Contains 23,502 fake news articles and 21,417 true news articles.
        </p>

        <h4 className="text-lg font-semibold">How It Works</h4>
        <p>Model: Fine-tuned BERT from Hugging Face Transformers</p>
        <p>Input features: News statement, Title</p>
        <p>Output:</p>
        <ul className="list-disc pl-6 space-y-1">
          <li>Binary Classification – Real or Fake</li>
          <li>SHAP waterfall plot – visually highlighting the most influential words that contributed to the model’s decision.</li>
        </ul>

        <h4 className="text-lg font-semibold">Training Method</h4>
        <p>
          The model is fine-tuned on a binary classification task using BERT-base-uncased from Hugging Face Transformers.
        </p>
        <p>
          It was trained using <span className="font-semibold">CrossEntropy loss</span> and the
          <span className="font-semibold"> Adam optimizer</span> for 4 epochs with a batch size of 32
          and learning rate of 1e-5.
        </p>
        <p className="mt-2">
          During training, the BERT encoder was partially frozen (only unfreezed the last two layers) to reduce overfitting and speed up convergence.
          Token inputs included the Title and partial statement (GPU power bottleneck with long input).
        </p>

        <div className="mt-4">
          <img
            src="/images/result/training_loss.png"
            alt="Training Loss graph"
            className="max-w-full"
          />
        </div>

        <p>
          As the image above suggests, the training loss starts around 0.6 and lands near ~0.05 after 4 epochs.
        </p>
      </div>
    </main>
  );
}
