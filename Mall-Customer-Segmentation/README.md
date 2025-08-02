# Customer Segmentation Using Machine Learning

This project explores customer segmentation using both unsupervised and supervised machine learning techniques. It aims to identify patterns in customer spending behavior and group them into meaningful clusters. This can help businesses tailor marketing strategies and enhance customer satisfaction.

## Dataset

- Source: [Mall Customer Segmentation Data - Kaggle](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python)
- Features:
  - `CustomerID`
  - `Gender`
  - `Age`
  - `Annual Income (k$)`
  - `Spending Score (1-100)`

## Technologies Used

- Python – Core programming
- Jupyter Notebook – Interactive development
- Pandas / NumPy – Data manipulation
- Matplotlib / Seaborn – Data visualization
- Scikit-learn – Machine learning algorithms

## Key Features

### Exploratory Data Analysis (EDA)

- Statistical summaries and distributions
- Visualizations: pair plots, box plots, heatmaps
- Relationship analysis between features (e.g., income vs. spending)

### Unsupervised Learning (KMeans Clustering)

- Scaled features and performed clustering
- Used Elbow Method and Silhouette Score to determine optimal clusters
- Labeled clusters and visualized spending behaviors
- Identified actionable customer segments

### Supervised Learning (Random Forest Classifier)

- Labeled cluster results used as target for supervised model
- Trained Random Forest Classifier
- Evaluated model accuracy and confusion matrix

## Installation

```bash
pip install -r requirements.txt