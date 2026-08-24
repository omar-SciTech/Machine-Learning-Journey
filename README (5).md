# 🤖 Machine Learning Journey

### A continuously growing Machine Learning portfolio — from self-taught foundations, through NTI × ITIDA training, to self-driven practice beyond it

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Actively%20Learning-brightgreen?style=flat)

---

## 📖 About This Repository

This repository traces a continuous, still-growing Machine Learning journey, built in three layers:

1. **Foundations** (`python/`, `data-science/`) — Python and core data-science tooling, built independently as groundwork. The ML track itself lists "basic Python programming" and "basic math" as *prerequisites*, not something it teaches — so this layer came first, on my own.
2. **Formal training** (`ml/`, and the capstone project inside `projects/`) — built through the **NTI × ITIDA Machine Learning track**, a 120-hour, project-based program covering classical ML end-to-end.
3. **Self-driven practice** (`from-scratch/`, and every new addition to `projects/` since) — continuing on my own past the course: re-implementing every model mathematically from the ground up, and taking on new end-to-end projects outside any syllabus.

Even layer 2 wasn't just "show up and follow along." The program was demanding by design — **120 hours total** (90 hours of core Machine Learning, 30 hours of Soft Skills), with **mandatory attendance of 6 hours a day**, a meaningful part of it hands-on practical work, and a real assignment due after every single session. But a large part of what made it click for me was self-driven on top of that required schedule — extra reading, documentation, and AI-assisted exploration of anything a session only introduced at a high level. That same instinct is what layer 3 is now built entirely out of.

> *I made it a rule not to move past a single line of code until I understood exactly what it does, why it's there, and — where relevant — the math behind it. Understanding it properly always mattered more to me than finishing fast. `from-scratch/` is that rule taken to its logical end.*

---

## 🎓 The Formal Training — NTI × ITIDA (120 Hours)

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
Machine-Learning-Journey/
│
├── python/                          # Foundations — self-taught, ahead of the ML coursework
│   ├── 01-basics.ipynb
│   ├── 02-oop.ipynb
│   ├── 03-datastructures.ipynb
│   ├── 04-algorithms.ipynb
│   ├── 05-controlflow.ipynb
│   ├── 06-pythonic.ipynb
│   ├── intro.py
│   └── cheatsheet.pdf
│
├── data-science/                    # Foundations — NumPy, SciPy, Pandas, Matplotlib & applied EDA
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
├── ml/                               # Formal training — NTI × ITIDA Machine Learning track
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
├── from-scratch/                     # Self-driven — every model rebuilt with math + NumPy, no ML libraries
│   ├── regression/
│   ├── classification/
│   ├── clustering/
│   └── neural-networks/
│
├── projects/                         # End-to-end projects — course-assigned and self-initiated alike
│   └── lung-cancer-prediction/       # NTI × ITIDA capstone project
│       ├── notebook.ipynb
│       └── survey lung cancer.csv
│
└── README.md
```

---

## 🧠 What's Inside

### 🐍 Python Fundamentals — `python/`
*Foundations — built independently.*

Core language practice: syntax basics, object-oriented programming (classes, inheritance, magic methods), data structures, algorithms, control flow, and idiomatic ("pythonic") code.

### 📊 Data Science Foundations — `data-science/`
*Foundations — built independently.*

The core data-science toolkit (NumPy, SciPy, sparse matrices, Matplotlib, Pandas) plus applied exploratory data analysis projects:

| Project | What it covers |
|---|---|
| `covid-global-plotly/` | Global COVID-19 trends visualized interactively with Plotly (bar, scatter, and table views) |
| `covid19-california-counties-analysis.ipynb` | County-level case/death analysis for California, with 7-day rolling averages |
| `covid19-california-percapita-ranking.ipynb` | Per-capita normalization and top-10 county ranking, building on the analysis above |
| `flights-delay-analysis/` | Flight delay patterns by month, day, and airport using Pandas |

### 🤖 Machine Learning — `ml/`
*Formal training — NTI × ITIDA.*

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

### 🔬 From-Scratch Implementations — `from-scratch/`
*Self-driven — newly started, ongoing.*

Every model covered in the ML track, rebuilt using only the underlying math and NumPy — no `scikit-learn`, no shortcuts — organized by category:

- `regression/`
- `classification/`
- `clustering/`
- `neural-networks/`

The goal here isn't a model that happens to run; it's proof that I understand what each `.fit()` call was actually doing underneath. This folder will keep growing as I work through the full list.

### 🏆 Projects — `projects/`
*Course-assigned and self-initiated alike.*

Full end-to-end applications, not tied to a single source. Some started as course assignments, others are entirely self-initiated — what they share is a complete pipeline from raw data to a working, deployed result.

**Lung Cancer Prediction** — `projects/lung-cancer-prediction/`
*(NTI × ITIDA capstone project)*

The program's major applied project, built collaboratively with **two teammates** as a complete, end-to-end machine learning application rather than a single-technique exercise.

**My role:** I owned the **AI/ML modeling side** — building, tuning, and evaluating the classification models — and the **deployment layer**, packaging the final model and wrapping it in an interactive interface. Debugging and problem-solving were a genuine team effort throughout, with real collaboration on every blocker we hit.

**Pipeline:**
1. **EDA** — univariate, bivariate, and multivariate analysis of symptoms and lifestyle factors against the lung cancer diagnosis
2. **Preprocessing** — de-duplication, outlier handling, encoding
3. **Modeling** — Decision Tree, Random Forest, AdaBoost, and Gradient Boosting classifiers, each tuned via `GridSearchCV`
4. **Model selection** — compared with cross-validated F1 score, to account for class imbalance
5. **Evaluation** — confusion matrices, classification reports, feature-importance rankings
6. **Deployment** — best model serialized with `joblib` and served through a Gradio web interface

*More projects will be added here as they're finished — course-related or not.*

---

## 🧩 Skills Demonstrated

- End-to-end ML pipelines: EDA → preprocessing → modeling → evaluation → deployment
- Deriving and implementing ML algorithms from first principles — math and NumPy, no high-level libraries (see `from-scratch/`)
- Selecting and applying the right supervised/unsupervised algorithm to a given problem with scikit-learn
- Hyperparameter tuning and model comparison (`GridSearchCV`, cross-validation)
- Data visualization for exploratory and explanatory purposes (Matplotlib, Seaborn, Plotly)
- Model deployment with Gradio and `joblib`
- Collaborative development and debugging as part of a team

## 🛠️ Tools & Libraries

Python · Jupyter Notebook · NumPy · SciPy · Pandas · Matplotlib · Seaborn · Plotly · scikit-learn · TensorFlow/Keras · Gradio · joblib

## 🚀 Getting Started

```bash
git clone https://github.com/omar-SciTech/Machine-Learning-Journey.git
cd Machine-Learning-Journey
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
| NTI × ITIDA | Machine Learning — Summer Training | 120 hours | **_____** |

*Certificate to be added here upon receipt.*

---

## 🔭 What's Next

- Working through `from-scratch/`: every model from the ML track, re-derived mathematically and implemented in raw NumPy
- Adding more independent, self-initiated projects to `projects/` — not tied to any course
- Eventually starting a **Deep Learning** track — most likely as its own dedicated repository once it has real substance, rather than folded into this one

## 🙏 Acknowledgments

- **NTI** and **ITIDA** for organizing and running the training
- The Machine Learning track's instructors and mentors
- My two teammates on the Lung Cancer Prediction capstone project

## 📬 Connect

- GitHub: [github.com/omar-SciTech](https://github.com/omar-SciTech)
- LinkedIn: [linkedin.com/in/omar-mohamed-g](http://www.linkedin.com/in/omar-mohamed-g)
- Email: [omarmgamaleldin7@gmail.com](mailto:omarmgamaleldin7@gmail.com)
