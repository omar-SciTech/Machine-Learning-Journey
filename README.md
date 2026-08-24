# 🤖 Machine Learning Journey

### NTI × ITIDA Summer Training — Machine Learning Track (120 Hours)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=flat&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-Applied%20Math-8CAAE6?style=flat&logo=scipy&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Neural%20Networks-FF6F00?style=flat&logo=tensorflow&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20EDA-3F4F75?style=flat&logo=plotly&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed%20Training-brightgreen?style=flat)

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
Machine-Learning-Journey/
│
├── python/                                  # Core Python practice
│   ├── Algorithms.ipynb
│   ├── basics.ipynb
│   ├── datastructure.ipynb
│   ├── intro.py
│   ├── oop.ipynb
│   ├── programflow.ipynb
│   ├── pythonic.ipynb
│   └── python_cheat_sheet_250710_120729.pdf
│
├── Data Analytics For ML/                   # NumPy, SciPy, Pandas, Matplotlib & applied EDA
│   ├── Data Science/
│   │   ├── 0. Setup.ipynb
│   │   ├── 1 Numpy.ipynb
│   │   ├── 2 Scipy.ipynb
│   │   ├── 2.1 Sparse Matrices.ipynb
│   │   ├── 3 Matplotlib.ipynb
│   │   ├── Pandas_intro.ipynb
│   │   └── pandas-and-jupyter-notebook.ipynb
│   ├── covid-global-plotly/
│   ├── flights-delay-analysis/
│   ├── covid19-california-counties-analysis.ipynb
│   └── covid19-california-percapita-ranking.ipynb
│
├── ML/                                      # Machine learning algorithms & mini-projects
│   ├── Housing_Price_Prediction/
│   ├── KNN/
│   ├── Store_clustering/
│   ├── linreg-carprice/
│   ├── linreg-houseprice/
│   ├── naive-bayes-income/
│   ├── svm_iris_classification/
│   ├── DB & PCA.ipynb
│   ├── DTC.ipynb
│   ├── Decision-Tree-Reg.ipynb
│   ├── Fruit NN.ipynb
│   ├── Gradient Boosting.ipynb
│   ├── Hierarchical Clustering.ipynb
│   ├── PCA.ipynb
│   ├── Sklearn & Machine Learning.ipynb
│   ├── basic neural network.ipynb
│   ├── basic-kmeans.ipynb
│   ├── customer-segments.ipynb
│   ├── forest.ipynb
│   ├── kmeans-ram.ipynb
│   ├── logreg-basic.ipynb
│   ├── logreg_diabetes_eval.ipynb
│   ├── rand_forest.ipynb
│   └── svm.ipynb
│
├── Big project/                             # Bigger, cross-domain capstone work
│   ├── Lung Cancer Prediction.ipynb
│   └── survey lung cancer.csv
│
└── README.md
```

---

## 🧠 What's Inside

### 🐍 Python Fundamentals — [`python/`](./python)

Core language practice: introductory setup script ([`intro.py`](./python/intro.py)), syntax basics ([`basics.ipynb`](./python/basics.ipynb)), object-oriented programming with classes, inheritance, and magic methods ([`oop.ipynb`](./python/oop.ipynb)), data structures ([`datastructure.ipynb`](./python/datastructure.ipynb)), algorithms ([`Algorithms.ipynb`](./python/Algorithms.ipynb)), control flow ([`programflow.ipynb`](./python/programflow.ipynb)), idiomatic ("pythonic") code ([`pythonic.ipynb`](./python/pythonic.ipynb)), and a comprehensive reference cheat sheet ([`python_cheat_sheet_250710_120729.pdf`](./python/python_cheat_sheet_250710_120729.pdf)).

### 📊 Data Analytics for ML — [`Data Analytics For ML/`](./Data%20Analytics%20For%20ML)

The core data-science toolkit (NumPy, SciPy, sparse matrices, Matplotlib, Pandas) housed under [`Data Science/`](./Data%20Analytics%20For%20ML/Data%20Science), plus applied exploratory data analysis projects:

| Project / Notebook | What it covers |
|---|---|
| [`Data Science/0. Setup.ipynb`](./Data%20Analytics%20For%20ML/Data%20Science/0.%20Setup.ipynb) | Environment configuration, package verification, and workspace setup |
| [`Data Science/1 Numpy.ipynb`](./Data%20Analytics%20For%20ML/Data%20Science/1%20Numpy.ipynb) | Multidimensional arrays, slicing, vectorization, and linear algebra operations |
| [`Data Science/2 Scipy.ipynb`](./Data%20Analytics%20For%20ML/Data%20Science/2%20Scipy.ipynb) & [`2.1 Sparse Matrices.ipynb`](./Data%20Analytics%20For%20ML/Data%20Science/2.1%20Sparse%20Matrices.ipynb) | Scientific computing routines and memory-efficient sparse matrix representations |
| [`Data Science/3 Matplotlib.ipynb`](./Data%20Analytics%20For%20ML/Data%20Science/3.%20Matplotlib.ipynb) | Static data visualization, custom plots, subplots, and styling |
| [`Data Science/Pandas_intro.ipynb`](./Data%20Analytics%20For%20ML/Data%20Science/Pandas_intro.ipynb) & [`pandas-and-jupyter-notebook.ipynb`](./Data%20Analytics%20For%20ML/Data%20Science/pandas-and-jupyter-notebook.ipynb) | Data wrangling, DataFrame manipulation, filtering, aggregation, and notebook workflows |
| [`covid-global-plotly/`](./Data%20Analytics%20For%20ML/covid-global-plotly) | Global COVID-19 trends visualized interactively with Plotly (bar, scatter, and table views) |
| [`covid19-california-counties-analysis.ipynb`](./Data%20Analytics%20For%20ML/covid19-california-counties-analysis.ipynb) | County-level case/death analysis for California, with 7-day rolling averages |
| [`covid19-california-percapita-ranking.ipynb`](./Data%20Analytics%20For%20ML/covid19-california-percapita-ranking.ipynb) | Per-capita normalization and top-10 county ranking, building on the analysis above |
| [`flights-delay-analysis/`](./Data%20Analytics%20For%20ML/flights-delay-analysis) | Flight delay patterns by month, day, and airport using Pandas |

### 🤖 Machine Learning — [`ML/`](./ML)

**Supervised Learning**

| Notebook / Folder | Algorithm | Notes |
|---|---|---|
| [`linreg-carprice/`](./ML/linreg-carprice) | Linear Regression | Predicting resale car price from vehicle features, with full EDA and correlation analysis |
| [`linreg-houseprice/`](./ML/linreg-houseprice) | Linear Regression | Predicting house prices |
| [`Housing_Price_Prediction/`](./ML/Housing_Price_Prediction) | Linear Regression | End-to-end real estate pricing workflow with data cleaning and feature engineering |
| [`logreg-basic.ipynb`](./ML/logreg-basic.ipynb) | Logistic Regression | Breast cancer classification (94.74% test accuracy) |
| [`logreg_diabetes_eval.ipynb`](./ML/logreg_diabetes_eval.ipynb) | Logistic Regression | Diabetes classification with scaling, confusion matrix, classification report, ROC curve, and decision boundary |
| [`svm.ipynb`](./ML/svm.ipynb), [`svm_iris_classification/`](./ML/svm_iris_classification) | Support Vector Machines | Iris species classification with linear and non-linear kernel spaces |
| [`KNN/`](./ML/KNN) | K-Nearest Neighbors | Wheat-seed classification (PCA-reduced) and Wisconsin breast-cancer diagnosis, with a full hyperparameter search across scalers, reducers, K, and weighting schemes |
| [`naive-bayes-income/`](./ML/naive-bayes-income) | Gaussian Naive Bayes | Income-bracket classification on the Adult/Census dataset — full EDA, encoding, and evaluation |
| [`DTC.ipynb`](./ML/DTC.ipynb), [`Decision-Tree-Reg.ipynb`](./ML/Decision-Tree-Reg.ipynb) | Decision Trees | Classification and regression variants |
| [`forest.ipynb`](./ML/forest.ipynb), [`rand_forest.ipynb`](./ML/rand_forest.ipynb) | Random Forests | Ensemble classification |
| [`Gradient Boosting.ipynb`](./ML/Gradient%20Boosting.ipynb) | Gradient Boosting | Boosted ensemble classification |
| [`Sklearn & Machine Learning.ipynb`](./ML/Sklearn%20&%20Machine%20Learning.ipynb) | Scikit-Learn Workflows | Unified estimators, transformers, and model evaluation pipelines |

**Unsupervised Learning & Dimensionality Reduction**

| Notebook / Folder | Algorithm | Notes |
|---|---|---|
| [`basic-kmeans.ipynb`](./ML/basic-kmeans.ipynb), [`kmeans-ram.ipynb`](./ML/kmeans-ram.ipynb) | K-Means | Core clustering practice & RAM benchmark clustering |
| [`Store_clustering/`](./ML/Store_clustering) | K-Means | Applied to retail/store data |
| [`Hierarchical Clustering.ipynb`](./ML/Hierarchical%20Clustering.ipynb) | Agglomerative Clustering | Hierarchical grouping & dendrogram analysis |
| [`customer-segments.ipynb`](./ML/customer-segments.ipynb) | DBSCAN, K-Means, Agglomerative | Customer segmentation, comparing all three algorithms on the same data |
| [`PCA.ipynb`](./ML/PCA.ipynb), [`DB & PCA.ipynb`](./ML/DB%20&%20PCA.ipynb) | PCA & DBSCAN | Dimensionality reduction and density-based clustering exploration |

**Neural Networks**

| Notebook | Notes |
|---|---|
| [`Fruit NN.ipynb`](./ML/Fruit%20NN.ipynb), [`basic neural network.ipynb`](./ML/basic%20neural%20network.ipynb) | A first neural network built with TensorFlow/Keras, focused on understanding raw logits vs. Softmax probabilities and multi-class fruit classification |

### 🏆 Capstone Project — [`Big project/`](./Big%20project)

The program's major applied project ([`Lung Cancer Prediction.ipynb`](./Big%20project/Lung%20Cancer%20Prediction.ipynb)), built collaboratively with **two teammates** as a complete, end-to-end machine learning workflow covering data analysis, preprocessing, model development, evaluation, model selection, serialization, and an interactive Gradio interface.

**My role:** I owned the **AI/ML modeling side** — building, tuning, comparing, and evaluating the classification models — and the **deployment layer**, packaging the final model and wrapping it in an interactive interface. Debugging and problem-solving were a genuine team effort throughout, with real collaboration on every blocker we hit.

**Pipeline:**
1. **EDA** — univariate, bivariate, and multivariate analysis of symptoms and lifestyle factors against the target outcome
2. **Preprocessing** — de-duplication, outlier handling, and categorical/binary encoding
3. **Modeling** — Decision Tree, Random Forest, AdaBoost, and Gradient Boosting classifiers, each tuned via `GridSearchCV`
4. **Model selection** — compared with cross-validated F1 score to account for class imbalance
5. **Evaluation** — confusion matrices, classification reports, feature-importance rankings, and ROC-AUC
6. **Deployment** — best model serialized with `joblib` and integrated into an interactive Gradio interface

**Key Results:**
- **Best model:** Random Forest
- **Cross-validated F1:** 0.9358
- **Test Accuracy:** 91.2%
- **Test Precision:** 93.4%
- **Test Recall:** 96.6%
- **Test F1-score:** 95.0%
- **Test ROC-AUC:** 0.962

**Important:** This is an educational machine-learning project based on a small survey dataset and is not intended for clinical diagnosis or medical decision-making.

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

- Going deeper into deep learning frameworks (TensorFlow / PyTorch)
- Deploying more projects end-to-end, not just training models in a notebook
- Taking on Kaggle competitions for real-world, messier data
- Exploring specializations (NLP, computer vision) built on this foundation

## 🙏 Acknowledgments

- **NTI** and **ITIDA** for organizing and running the training
- The Machine Learning track's instructors and mentors
- My two teammates on the Lung Cancer Prediction capstone project

## 📬 Connect

- GitHub: [*https://github.com/omar-SciTech*](https://github.com/omar-SciTech)
- LinkedIn: [*www.linkedin.com/in/omar-mohamed-g*](https://www.linkedin.com/in/omar-mohamed-g)
- Email: [*omarmgamaleldin7@gmail.com*](mailto:omarmgamaleldin7@gmail.com)
