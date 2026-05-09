# DSA_Internship
DSA_Internship
**Problem Understanding**
The rapid growth of online book platforms has made it difficult for publishers, sellers, and readers to identify which books are likely to become popular. Book popularity is influenced by multiple factors such as ratings, number of reviews, genre, pricing, and reader engagement. Understanding these factors can help online bookstores improve recommendation systems, optimize pricing strategies, and enhance customer satisfaction.
This project focuses on analyzing and predicting the popularity of Indian and India-related books using data collected from the Open Library API. The dataset contains 10,000 unique books along with attributes such as ratings, reviews, pages, genre, review density, and popularity score. 
The main objective is to perform:
Exploratory Data Analysis (EDA)
Feature Engineering
Statistical Analysis
Popularity Pattern Identification
Predictive Modeling preparation
The project attempts to discover:
Which factors influence book popularity
How ratings and reviews affect success
Whether price categories impact popularity
Which genres perform better in terms of engagement
**Success Metric Definition**
The success of this project can be measured using the following metrics:
1. Data Quality Metrics
No duplicate book titles
Minimal missing values
Clean and normalized dataset
Proper feature generation
2. Exploratory Analysis Success
The project successfully identifies:
Distribution of ratings, prices, and reviews
Relationships between features
Trends across genres and price buckets
Popularity patterns using visualizations
3. Feature Engineering Success
Generated features such as:
Review_Density
Price_Bucket
Popularity_Score
Success_Category
should provide meaningful insights into popularity behavior. 
4. Predictive Readiness
The dataset should become suitable for future machine learning tasks such as:
Popularity prediction
Recommendation systems
Classification of successful books
5. Business Success Metrics
The project is successful if it helps:
Identify highly engaging books
Improve pricing strategies
Understand reader behavior
Enhance recommendation systems
**Project Overview**

This project is an Online Book Popularity Analysis and Prediction System developed using Python and data analysis libraries such as:

Pandas
NumPy
Matplotlib
Seaborn
Requests

The dataset was generated using the Open Library Search API and contains India-related books collected using multiple search keywords including:

Indian fiction
Indian history
Indian literature
Malayalam literature
Tamil literature
Indian politics
Indian philosophy
Indian mythology
and more.

The project workflow includes:

Data Collection
Data Cleaning
Duplicate Removal
Missing Value Handling
Genre Assignment
Feature Engineering
Exploratory Data Analysis
Cross-tab Analysis
Correlation Analysis
Feature Selection

The system generates useful derived features such as:

Popularity Score
Review Density
Success Categories

which help in understanding the popularity behavior of books.
**Dataset Description**

The dataset contains 10,000 clean and unique Indian/India-related books collected from the Open Library API.

Dataset Size
Total Rows: 10,000
Total Columns: 10
Dataset Columns
Column Name	Description
Title	Name of the book
Rating	Average user rating of the book
Price	Simulated price of the book
Pages	Number of pages in the book
Genre	Assigned genre category
Reviews	Number of user reviews
Review_Density	Reviews per page ratio
Price_Bucket	Categorized price range
Popularity_Score	Calculated popularity metric
Success_Category	Popularity classification
**Feature Descriptions**
1. Review_Density

Calculated as:

Review_Density=
Pages
Reviews
	​


It measures reader engagement relative to book size.

2. Popularity_Score

Calculated using ratings and reviews:

Popularity_Score=(Rating×0.65)+(log(1+Reviews)×0.35)

This feature combines both quality and engagement.

3. Price_Bucket

Books are categorized into:

Budget
Mid-range
Premium

based on their price range.

4. Success_Category

Books are classified into:

Low
Medium
High

based on the popularity score.

Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Open Library API
Google Colab
**Expected Outcomes**

The project aims to:

Understand factors affecting book popularity
Discover genre-wise popularity trends
Analyze customer engagement patterns
Support recommendation and prediction systems
Prepare a high-quality dataset for machine learning models

**Setup Instructions**
1. Install Required Libraries
Run the following command to install all required Python libraries:
pip install pandas numpy matplotlib seaborn requests beautifulsoup4
If using Google Colab:
!pip install pandas numpy matplotlib seaborn requests beautifulsoup4

2. Import Required Libraries
import pandas as pdimport numpy as npimport matplotlib.pyplot as pltimport seaborn as snsimport requestsimport timeimport reimport unicodedata

3. Download or Generate Dataset
The dataset is generated using the Open Library API and saved as:
online_book_popularity_10000_clean_unique_books.csv
Load the dataset:
df = pd.read_csv("online_book_popularity_10000_clean_unique_books.csv")

4. Verify Dataset
Check whether the dataset loaded correctly:
print(df.head())print(df.shape)print(df.info())

5. Project Directory Structure
Recommended project structure:
Book_Popularity_Project/│├── data/│   └── online_book_popularity_10000_clean_unique_books.csv│├── notebooks/│   └── Indian_Books.ipynb│├── scripts/│   ├── data_cleaning.py│   ├── feature_engineering.py│   ├── eda.py│├── outputs/│   ├── plots/│   ├── reports/│└── README.md

6. Run Data Collection Script
To collect books from the Open Library API:
response = requests.get("https://openlibrary.org/search.json")
The script:


Fetches India-related books


Removes duplicates


Cleans corrupted titles


Generates additional features


Saves the final dataset



7. Run Exploratory Data Analysis (EDA)
Example:
sns.histplot(df['Popularity_Score'], kde=True)plt.show()
EDA includes:


Univariate analysis


Bivariate analysis


Correlation analysis


Cross-tab analysis


Outlier detection



8. Run Feature Engineering
Generated features include:


Review_Density


Price_Bucket


Popularity_Score


Success_Category


Example:
df["Review_Density"] = df["Reviews"] / df["Pages"]

9. Save Processed Dataset
df.to_csv("Feature_Engineered_Output.csv", index=False)

10. Recommended Environment
You can run this project using:


Jupyter Notebook


Google Colab


VS Code


PyCharm


Anaconda



11. Python Version
Recommended:
Python 3.9 or above

12. Optional Machine Learning Setup
Install Scikit-learn for future prediction models:
pip install scikit-learn
Import:
from sklearn.model_selection import train_test_splitfrom sklearn.preprocessing import StandardScalerfrom sklearn.linear_model import LinearRegression
