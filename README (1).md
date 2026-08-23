# 🤖 Machine Learning Journey

### NTI × ITIDA Summer Training — Machine Learning Track (90 Hours)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Actively%20Learning-brightgreen?style=flat)

---

## 📖 About This Repository

This repository is a record of my hands-on journey through the **Machine Learning track** of the **NTI (National Telecommunication Institute) × ITIDA Summer Training program** — a 120-hour, project-based program covering classical machine learning end-to-end, from the math underneath each algorithm to a deployable application.

Every notebook here was written and run by me — not copied from a lecture and left untouched. The program itself was demanding by design: **120 hours total** (90 hours of core Machine Learning, 30 hours of Soft Skills), with **mandatory attendance of 6 hours a day** — a meaningful part of which had to be hands-on practical work done by me, not passive lecture-watching, and every single session ended with a real assignment to complete. On top of that required schedule, a large part of what's in this repo also came from **self-study outside the official curriculum** — extra reading, documentation, and AI-assisted exploration of anything the sessions only introduced at a high level.

> *I made it a rule not to move past a single line of code until I understood exactly what it does, why it's there, and — where relevant — the math behind it. Understanding it properly always mattered more to me than finishing fast.*

## 🎓 About the Program

| | |
|---|---|
| **Provider** | NTI (National Telecommunication Institute), in partnership with ITIDA |
| **Track** | Machine Learning |
| **Total Duration** | 120 hours — 90 hours Machine Learning + 30 hours Soft Skills |
| **Daily Commitment** | 6 hours of mandatory attendance per day, a meaningful part of it hands-on practical work — with a real assignment due after every single session |
| **Prerequisites** | Basic Python programming, basic math |
| **Audience** | 1st–3rd year students — Electronics & Communications Engineering, Computer Engineering, and Computers & Information faculties |

**Program focus:** applying machine learning algorithms to automate decision-making and uncover patterns in data, scaling from simple rule-based tasks up to real-world problems like large-scale data analysis, prediction, and forecasting.

**Curriculum covered:**

- **Supervised Learning** — Linear Regression, Logistic Regression, Support Vector Machines, K-Nearest Neighbors, Naive Bayes, Decision Trees, Random Forests & Boosting
- **Unsupervised Learning** — K-Means, Gaussian Mixture Models, Hierarchical Clustering, Principal Component Analysis (PCA)
- **Neural Networks** — introductory concepts and a first hands-on model
- **Model Selection & Practical Considerations** — cross-validation, hyperparameter tuning, evaluation metrics
- **Project-based learning**, culminating in a full applied ML project
- **Soft Skills** — 30 hours, built into the daily schedule alongside the technical curriculum

**Facilities used:** cloud compute (Google Colab / Kaggle) for GPU-scale workloads, regular hands-on assignments, and a capstone project applying the full pipeline end-to-end.

**Career paths this track builds toward:** Data Analyst, Data Scientist, Machine Learning Engineer, Machine Learning Developer, Applied Science Researcher.

---

## 🗂️ Repository Structure

```
machine-learning-journey/
│
├── python/                          # Core Python practice
│   ├── 01-basics.ipynb
│   ├── 02-oop.ipynb
│   ├── 03-datastructures.ipynb
│   ├── 04-algorithms.ipynb
│   ├── 05-controlflow.ipynb
│   ├── 06-pythonic.ipynb
│   ├── intro.py
│   └── cheatsheet.pdf
│
├── data-science/                    # NumPy, SciPy, Pandas, Matplotlib & applied EDA
│   ├── 0-setup.ipynb
│   ├── numpy-basics.ipynb
│   ├── scipy-basics.ipynb
│   ├── sparse-matrices.ipynb
│   ├── matplotlib-basics.ipynb
│   ├── pandas-intro.ipynb
│   ├── pandas-and-jupyter-notebook.ipynb
│   ├── covid-global-plotly/
│   ├── covid19-california-counties-analysis.ipynb
│   ├── covid19-california-percapita-ranking.ipynb
│   └── flights-delay-analysis/
│
├── ml/                               # Machine learning algorithms & mini-projects
│   ├── linreg-carprice/
│   ├── linreg-houseprice/
│   ├── logreg-basic.ipynb
│   ├── logreg-diabetes-eval.ipynb
│   ├── svm.ipynb
│   ├── svm-iris-classification/
│   ├── KNN/
│   ├── naive-bayes-income/
│   ├── DTC.ipynb
│   ├── decision-tree-reg.ipynb
│   ├── forest.ipynb
│   ├── rand-forest.ipynb
│   ├── gradient-boosting.ipynb
│   ├── basic-kmeans.ipynb
│   ├── kmeans-ram.ipynb
│   ├── store-clustering/
│   ├── hierarchical-clustering.ipynb
│   ├── customer-segments.ipynb
│   ├── pca.ipynb
│   ├── db-and-pca.ipynb
│   ├── fruitnn.ipynb
│   ├── basic-neural-network.ipynb
│   └── housing-price-prediction/
│
├── projects/                         # Bigger, cross-domain capstone work
│   └── lung-cancer-prediction/
│       ├── notebook.ipynb
│       └── survey lung cancer.csv
│
└── README.md
```

---

## 🧠 What's Inside

### 🐍 Python Fundamentals — `python/`

Core language practice: syntax basics, object-oriented programming (classes, inheritance, magic methods), data structures, algorithms, control flow, and idiomatic ("pythonic") code.

### 📊 Data Science Foundations — `data-science/`

The core data-science toolkit (NumPy, SciPy, sparse matrices, Matplotlib, Pandas) plus applied exploratory data analysis projects:

| Project | What it covers |
|---|---|
| `covid-global-plotly/` | Global COVID-19 trends visualized interactively with Plotly (bar, scatter, and table views) |
| `covid19-california-counties-analysis.ipynb` | County-level case/death analysis for California, with 7-day rolling averages |
| `covid19-california-percapita-ranking.ipynb` | Per-capita normalization and top-10 county ranking, building on the analysis above |
| `flights-delay-analysis/` | Flight delay patterns by month, day, and airport using Pandas |

### 🤖 Machine Learning — `ml/`

**Supervised Learning**

| Notebook / Folder | Algorithm | Notes |
|---|---|---|
| `linreg-carprice/` | Linear Regression | Predicting resale car price from vehicle features, with full EDA and correlation analysis |
| `linreg-houseprice/` | Linear Regression | Predicting house prices |
| `logreg-basic.ipynb` | Logistic Regression | Breast cancer classification (94.74% test accuracy) |
| `logreg-diabetes-eval.ipynb` | Logistic Regression | Diabetes classification with scaling, confusion matrix, classification report, ROC curve, and decision boundary |
| `svm.ipynb`, `svm-iris-classification/` | Support Vector Machines | Iris species classification |
| `KNN/` | K-Nearest Neighbors | Wheat-seed classification (PCA-reduced) and Wisconsin breast-cancer diagnosis, with a full hyperparameter search across scalers, reducers, K, and weighting schemes |
| `naive-bayes-income/` | Gaussian Naive Bayes | Income-bracket classification on the Adult/Census dataset — full EDA, encoding, and evaluation |
| `DTC.ipynb`, `decision-tree-reg.ipynb` | Decision Trees | Classification and regression variants |
| `forest.ipynb`, `rand-forest.ipynb` | Random Forests | Ensemble classification |
| `gradient-boosting.ipynb` | Gradient Boosting | Boosted ensemble classification |

**Unsupervised Learning & Dimensionality Reduction**

| Notebook / Folder | Algorithm | Notes |
|---|---|---|
| `basic-kmeans.ipynb`, `kmeans-ram.ipynb` | K-Means | Core clustering practice |
| `store-clustering/` | K-Means | Applied to retail/store data |
| `hierarchical-clustering.ipynb` | Agglomerative Clustering | Hierarchical grouping |
| `customer-segments.ipynb` | DBSCAN, K-Means, Agglomerative | Customer segmentation, comparing all three algorithms on the same data |
| `pca.ipynb`, `db-and-pca.ipynb` | PCA | Dimensionality reduction |

**Neural Networks**

| Notebook | Notes |
|---|---|
| `fruitnn.ipynb`, `basic-neural-network.ipynb` | A first neural network built with TensorFlow/Keras, focused on understanding raw logits vs. Softmax probabilities |

### 🏆 Capstone Project — `projects/lung-cancer-prediction/`

The program's major applied project, built collaboratively with **two teammates** as a complete, end-to-end machine learning application rather than a single-technique exercise.

**My role:** I owned the **AI/ML modeling side** — building, tuning, and evaluating the classification models — and the **deployment layer**, packaging the final model and wrapping it in an interactive interface. Debugging and problem-solving were a genuine team effort throughout, with real collaboration on every blocker we hit.

**Pipeline:**
1. **EDA** — univariate, bivariate, and multivariate analysis of symptoms and lifestyle factors against the lung cancer diagnosis
2. **Preprocessing** — de-duplication, outlier handling, encoding
3. **Modeling** — Decision Tree, Random Forest, AdaBoost, and Gradient Boosting classifiers, each tuned via `GridSearchCV`
4. **Model selection** — compared with cross-validated F1 score, to account for class imbalance
5. **Evaluation** — confusion matrices, classification reports, feature-importance rankings
6. **Deployment** — best model serialized with `joblib` and served through a Gradio web interface

---

## 🧩 Skills Demonstrated

- End-to-end ML pipelines: EDA → preprocessing → modeling → evaluation → deployment
- Supervised & unsupervised algorithms implemented from first principles, not just called from a library
- Hyperparameter tuning and model comparison (`GridSearchCV`, cross-validation)
- Data visualization for exploratory and explanatory purposes (Matplotlib, Seaborn, Plotly)
- Model deployment with Gradio and `joblib`
- Collaborative development and debugging as part of a team

## 🛠️ Tools & Libraries

Python · Jupyter Notebook · NumPy · SciPy · Pandas · Matplotlib · Seaborn · Plotly · scikit-learn · TensorFlow/Keras · Gradio · joblib

## 🚀 Getting Started

```bash
git clone <this-repo-url>
cd machine-learning-journey
pip install -r requirements.txt
jupyter notebook
```

Each project folder is self-contained with its own dataset, so its notebook can be opened and run directly.

---

## 🎓 Certificate of Completion

<!--
Once the certificate arrives, uncomment this block:
<p align="center">
  <img src="./assets/certificate.png" alt="NTI x ITIDA Machine Learning Certificate" width="600"/>
</p>
-->

| Institution | Track | Duration | Grade |
|---|---|---|---|
| NTI × ITIDA | Machine Learning — Summer Training | 90 hours | **_____** |

*Certificate to be added here upon receipt.*

---

## 🔭 What's Next

- Going deeper into deep learning frameworks (TensorFlow / PyTorch)
- Deploying more projects end-to-end, not just training models in a notebook
- Taking on Kaggle competitions for real-world, messier data
- Exploring specializations (NLP, computer vision) built on this foundation

## 🙏 Acknowledgments

- **NTI** and **ITIDA** for organizing and running the training
- The Machine Learning track's instructors and mentors
- My two teammates on the Lung Cancer Prediction capstone project

## 📬 Connect

- GitHub: *(add your profile link)*
- LinkedIn: *(add your profile link)*
- Email: *(add your email)*
