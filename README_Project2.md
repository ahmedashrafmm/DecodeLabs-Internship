# 📊 Project 2: Data Classification Using AI

**DecodeLabs | Industrial Training Kit | Batch 2026**

---

## 📌 Overview

A supervised machine learning pipeline that classifies Iris flowers into three species using the K-Nearest Neighbors (KNN) algorithm. This project demonstrates the complete ML workflow — from raw data loading and feature scaling, through model training and hyperparameter tuning, to professional evaluation using Confusion Matrix and F1 Score.

> *"We do not write the rules. We provide history, and the machine derives the logic."* — DecodeLabs

---

## 🎯 Goal

Build a classification model using a small dataset that can:
- Load and understand a real dataset
- Split data into training and testing sets
- Apply a supervised learning algorithm
- Evaluate performance beyond simple accuracy

---

## ⚙️ Architecture: IPO Framework

| Phase | Task | Tools |
|---|---|---|
| **INPUT** | Load Iris dataset, explore, scale features | `load_iris`, `StandardScaler` |
| **PROCESS** | Train/test split, find optimal K, train KNN | `train_test_split`, `KNeighborsClassifier` |
| **OUTPUT** | Confusion matrix, F1 Score, live predictions | `confusion_matrix`, `f1_score` |

---

## 📂 Dataset: The Iris Benchmark

| Property | Value |
|---|---|
| Total Samples | 150 (Balanced) |
| Classes | 3 — Setosa, Versicolor, Virginica |
| Features | 4 — Sepal Length, Sepal Width, Petal Length, Petal Width |
| Source | `sklearn.datasets.load_iris` |

---

## 🔬 Pipeline Breakdown

### Phase 1 — Input
- **Load & Explore:** Dataset shape, class distribution, descriptive statistics
- **Visualize:** Class distribution bar chart + Petal scatter plot
- **Feature Scaling:** `StandardScaler` (Mean=0, Variance=1)
  - ⚠️ Scaler fitted on **training data only** to prevent data leakage

### Phase 2 — Process
- **Train/Test Split:** 80% training / 20% testing with shuffle
- **Elbow Method:** Scans odd K values (1–25) to find optimal K with lowest error rate
- **KNN Training:** Instantiate → Fit → Predict

### Phase 3 — Output
- **Accuracy & F1 Score**
- **Confusion Matrix** heatmap (TP / FP / FN / TN per class)
- **Full Classification Report** (Precision, Recall, F1 per class)
- **Feature Correlation Heatmap**
- **Live Predictions** on new unseen samples with confidence scores

---

## 📈 Results

| Metric | Score |
|---|---|
| Accuracy | 100% |
| F1 Score (Weighted) | 1.0 |
| Misclassifications | 0 |

---

## 💡 Key Design Decisions

### Why Feature Scaling is Mandatory for KNN
KNN is a distance-based algorithm. Without scaling, features with larger value ranges dominate the distance calculation, producing a biased model. `StandardScaler` normalizes all features to an equal footing.

### Why F1 Score Over Accuracy
> *"In imbalanced data, accuracy is a lie. We must look deeper."* — DecodeLabs

Accuracy can be misleading. F1 Score (harmonic mean of Precision & Recall) is the professional standard for evaluating classifiers.

### Why Odd K Values
Odd K values prevent tie votes during majority voting in multi-class classification.

---

## 🚀 How to Run

**Option 1 — Jupyter Notebook (Recommended):**
```bash
jupyter notebook Project2_Data_Classification.ipynb
```

**Option 2 — Google Colab:**
Upload `Project2_Data_Classification.ipynb` directly to [colab.research.google.com](https://colab.research.google.com)

---

## 🛠️ Requirements

```bash
pip install scikit-learn pandas numpy matplotlib seaborn
```

---

## 📚 Key Skills Demonstrated

- Supervised learning fundamentals
- Data loading, exploration & visualization
- Feature scaling & train/test split
- K-Nearest Neighbors algorithm
- Hyperparameter tuning (Elbow Method)
- Model evaluation: Confusion Matrix, F1 Score, Classification Report
- Live inference on unseen data
- IPO (Input → Process → Output) ML pipeline

---

*DecodeLabs | Batch 2026 | Project 2 of the AI Engineering Track*
