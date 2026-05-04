# DSA_Internship
DSA_Internship
**1. Problem Understanding**
The primary objective of this analysis is to evaluate the market performance and consumer perception of a large-scale catalog of Indian literature. With 1,000,000 records, the challenge lies in identifying which factors—such as Language, Genre, or Pricing Strategy—actually drive book success in a highly diverse market.

Key Business Questions:

Market Dominance: Which regional languages and genres generate the highest estimated revenue?

Pricing Sensitivity: How do discounts and final price points impact the popularity and sales volume of a title?

Content Strategy: Is there a specific "sweet spot" for book length (Pages) that correlates with higher ratings?

Accessibility: Does the format (Ebook vs. Hardcover) or translation status significantly alter the reach of a book?

**2. Success Metric Definition**
To quantify "Success" in this dataset, several advanced metrics were engineered to move beyond simple raw counts.
<img width="572" height="193" alt="image" src="https://github.com/user-attachments/assets/8d110480-6905-431f-91be-5762c65a01a0" />
<img width="560" height="157" alt="image" src="https://github.com/user-attachments/assets/f2e2f031-312a-448f-9091-889b6770aeca" />
<img width="581" height="76" alt="image" src="https://github.com/user-attachments/assets/bca3fbce-f6e5-4167-944d-ae1b3c05c55e" />
**Conclusion**
The "Success" of a book in this analysis is not just about having a 5-star rating; it is a multi-dimensional calculation of visibility (Popularity), economic return (Revenue), and consumer utility (Value Score). These metrics allow a publisher to distinguish between a "niche masterpiece" (high rating, low reviews) and a "mass-market blockbuster" (medium rating, very high reviews).
**Project Overview**

This project focuses on analyzing a large-scale dataset of Indian books to extract meaningful insights about publishing trends, authorship patterns, pricing, and reader preferences. By working with a dataset of approximately one million records, the project demonstrates data processing, exploratory data analysis (EDA), and potential applications such as recommendation systems or market analysis.

The primary objectives of this project include:

Understanding trends in Indian book publishing
Identifying popular genres, authors, and publishers
Analyzing pricing distribution and availability
Building a foundation for recommendation or prediction models
**Dataset Description**

The dataset (indian_books_1million.csv) contains detailed information about a large collection of books. While the exact schema may vary, it typically includes the following types of features:

Title – Name of the book
Author(s) – One or more authors
Publisher – Publishing company
Language – Language of the book
Genre/Category – Classification of the book
Price – Cost of the book
Rating/Reviews – User ratings and/or review counts
Publication Year – Year the book was published
ISBN/ID – Unique identifier
Key Characteristics:
Large-scale dataset (~1 million rows)
Likely contains missing or inconsistent values
Mix of categorical and numerical features
Suitable for EDA, visualization, and machine learning tasks
**Setup Instructions**
1. Prerequisites

Make sure you have the following installed:

Python (>= 3.8)
pip or conda
2. Install Required Libraries
pip install pandas numpy matplotlib seaborn scikit-learn
3. Project Structure
project/
│── data/
│   └── indian_books_1million.csv
│── notebooks/
│── scripts/
│── README.md
4. Load the Dataset
import pandas as pd

df = pd.read_csv("data/indian_books_1million.csv")
print(df.head())
5. Basic Exploration
print(df.shape)
print(df.info())
print(df.describe())
6. (Optional) Data Cleaning
Handle missing values
Remove duplicates
Standardize text fields
df.drop_duplicates(inplace=True)
df.fillna(method='ffill', inplace=True)
