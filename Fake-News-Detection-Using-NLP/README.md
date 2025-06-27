# Fake News Detection Using NLP and Machine Learning

This project leverages Natural Language Processing (NLP) and machine learning to automatically classify news articles as real or fake. It is built using the Fake and Real News Dataset from Kaggle and applies classical models with TF-IDF vectorization. The project demonstrates the effectiveness of such models and highlights the need for ethical and explainable deployment in real-world applications.

## Dataset

- Source: [Kaggle – Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- ~43,000 articles labeled as either "fake" or "real"
- Fields used: `title`, `text`

## Technologies Used

- **Python** – Core programming language
- **Jupyter Notebook** – Interactive coding and documentation
- **NLTK** – Text preprocessing (stopword removal, lemmatization)
- **Scikit-learn** – TF-IDF vectorization, machine learning models, evaluation
- **Matplotlib / Seaborn / WordCloud** – Visualizations (EDA, word clouds, performance charts)
- **Pandas / NumPy** – Data manipulation and analysis

## Key Features

- Text preprocessing (stopword removal, lemmatization)
- TF-IDF feature extraction (top 5000 terms, unigrams and bigrams)
- Model comparison: Logistic Regression, Naive Bayes, Random Forest, Linear SVM
- Evaluation using accuracy, precision, recall, F1-score, and confusion matrices
- 5-Fold cross-validation
- Feature importance analysis
- Ethical considerations and recommendations

## Installation

```bash
pip install -r requirements.txt