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
******FEATURE ENGINEERING**
Features That Came from the Open Library API (Original)
These five fields were pulled directly from the search results.

Title: The name of the book. It was cleaned to remove gibberish, blank entries, or titles with question marks.

Rating: The average user score for the book, on a scale from 3.0 to 5.0 stars. If the API missed a rating, a random score in that range was added.

Pages: The total number of pages in the book. Any missing values were filled with a random number between 80 and 900 pages.

Reviews: The total count of user ratings the book received. Missing values were filled with a random number between 20 and 2,500.

Subject: The main topic tag from the API (for example, "Indian history" or "Tamil literature"). This was used to determine the book's genre.

The Feature That Was Transformed (Mapped)
This column was not created from nothing, but it was also not directly taken from the API. It was mapped from existing data.

Genre: This is the category of the book, such as Fiction, History, Biography, Religion, Politics, Poetry, Philosophy, Science, Classic, or Self-Help.

How it was made: The code looked at the Subject field and searched for keywords. If the subject contained "history," the genre became History. If it contained "fiction," it became Fiction. If no keywords matched, the script randomly picked a genre from the list.

Why it matters: Different genres have different audience sizes and popularity patterns.

The Features That Were Fully Engineered (Created from Scratch or Formulas)
These five columns did not come from the API. They were calculated or randomly generated to make the dataset useful for predicting popularity.

Price: The cost of the book in Indian Rupees.

How it was made: The Open Library API does not provide price information, so the script randomly generates a price between ₹100 and ₹1,500 for every book.

Why it matters: This allows you to study whether cheaper books are more popular than expensive ones, or if price has no effect at all.

Review Density: A measure of how much discussion a book gets per page.

How it was made: It is calculated by dividing the number of Reviews by the number of Pages.

Why it matters: A short book with 1,000 reviews is much more "dense" and engaging than a long book with the same 1,000 reviews. Higher density often means higher popularity.

Price Bucket: A simple category that describes the price range.

How it was made: The continuous Price number is cut into three bins: Budget (₹100–₹400), Mid-range (₹401–₹900), and Premium (₹901–₹1,500).

Why it matters: It is easier for a business to compare "Budget vs. Premium" than to compare every possible price.

Popularity Score: A single combined score that represents overall popularity.

How it was made: This is a weighted formula:

65% of the score comes from the Rating (quality matters more).

35% comes from the log of Reviews (using a logarithm prevents books with 2,500 reviews from completely dominating the score).

Why it matters: It turns two separate numbers (Rating and Reviews) into one master number that ranks books from least to most popular.

Success Category: The final target label for classification problems.

How it was made: The continuous Popularity Score is cut into three bins: Low (below 4.8), Medium (4.8 to 5.5), and High (above 5.5).

Why it matters: Instead of predicting a specific number like 5.23,  can train a model to predict simply "High," "Medium," or "Low" success. This is easier for business teams to understand and act upon.
