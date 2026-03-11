# Water Quality Data Mining Project

Dataset: Water Potability Dataset (Kaggle)

Project includes:

1. Exploratory Data Analysis (EDA)
   - Distribution analysis
   - Correlation heatmap
   - Missing value handling

2. Association Rule Mining
   - Apriori algorithm
   - Mining relationships between water quality indicators

3. Clustering
   - KMeans clustering
   - PCA visualization of clusters

4. Classification
   - Predict water potability
   - Models: Random Forest / Logistic Regression

5. Semi-Supervised Learning
   - Label Spreading algorithm
   - Evaluate performance with limited labeled data

6. Regression
   - Predict continuous variable (Solids)
   - Models: Linear Regression, Ridge, Random Forest Regressor

Outputs are saved in the outputs/ folder.

## Methods
- EDA
- Association Rule Mining
- Clustering
- Classification
- Semi-Supervised Learning
- Regression

## Models
- Random Forest
- Logistic Regression
- Label Spreading
- Linear Regression

## Results
Random Forest achieved the best performance in predicting water potability.

lệnh python -m streamlit run app.py
    python scripts/predict_water.py