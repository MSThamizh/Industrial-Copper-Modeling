# Industrial Copper Modeling

This project aims to analyze and model sales data in the copper industry, utilizing machine learning techniques to predict sales outcomes based on various features. The project leverages tools such as MongoDB Atlas for data storage, Streamlit for building an interactive application, and visualization libraries for data insights.

## Problem Statement

The goal of this project is to develop a **Streamlit application** that enables users to explore copper sales predictions effectively. Key features include:

- **Data Cleaning**: Handle missing values, remove duplicates, and convert data types for analysis.
- **Predictive Modeling**: Build regression and classification models to predict sales prices and statuses (WON or LOST).
- **Prediction Visualization**: Allow users to visualize model predictions based on input features.

## Workflow

1. **Data Cleaning and Preparation**: Clean and preprocess the data to ensure it's ready for modeling.
2. **Feature Engineering**: Apply transformations and scaling to optimize model performance.
3. **Model Building**: Train regression and classification models to predict sales outcomes.
4. **Streamlit Web Application**: Develop an interactive web app that allows users to enter feature values and receive sales predictions.


## Features

- **Data Understanding and Cleaning**:
  - Identifies variable types and handles null and erroneous values, converting data types.

- **Data Preprocessing**:
  - Handles missing values with appropriate statistical methods (mean/median/mode).
  - Manages outliers using IQR or Isolation Forest methods from `sklearn`.
  - Corrects skewness in continuous variables using transformations like log or Box-Cox transformations, particularly for the target variable to improve regression results.
  - Encodes categorical variables with techniques such as one-hot, label, or ordinal encoding.

- **Exploratory Data Analysis (EDA)**:
  - Visualizes data distributions, outliers, and skewness using Seaborn plots, including boxplots, distplots, and violin plots, both before and after skewness treatment.

- **Feature Engineering**:
  - Creates new features and applies transformations to enhance model input.
  - Identifies and removes highly correlated features using Seaborn’s heatmap.

- **Model Building and Evaluation**:
  - Trains both classification and regression models using cross-validation for accuracy, precision, recall, F1 score, and AUC metrics.
  - Performs hyperparameter tuning via grid search and cross-validation for optimal model performance.

- **Streamlit Web Application**:
  - Provides an interactive application with a **Task Input** field to choose between Regression or Classification tasks.
  - Allows users to enter feature values for prediction, except for `Selling_Price` in regression and `Status` in classification.
  - Replicates feature engineering and transformation steps applied during training, delivering real-time predictions through the app interface.


## Technologies Used

- **Python**: Main programming language for data processing and application development.
- **Streamlit**: Framework for building the interactive web application.
- **Scikit-learn**: For machine learning model development.
- **Pandas/Numpy**: For data manipulation and analysis.

## References

- **Python**: [https://docs.python.org/3/](https://docs.python.org/3/)
- **Streamlit Documentation**: [https://docs.streamlit.io/library/api-reference](https://docs.streamlit.io/library/api-reference)
- **Scikit-learn Documentation**: [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)
- **Dataset**: [Data](https://docs.google.com/spreadsheets/d/18eR6DBe5TMWU9FnIewaGtsepDbV4BOyr/edit?usp=sharing&ouid=104970222914596366601&rtpof=true&sd=true)
