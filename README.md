# Online-Food-Delivery-Feedback-Repository
This project analyzes an online food delivery dataset to find out **which customer segments give negative feedback**, and whether those patterns are statistically real or just chance.

***Online Food Delivery: Customer Feedback Analysis***

**Overview**
This project analyzes an online food delivery dataset to find out **which customer segments give negative feedback**, and whether those patterns are statistically real or just chance.
It covers data cleaning, exploratory data analysis (EDA), hypothesis testing (chi-square), and an interactive Power BI dashboard.

**Business question**: Which customer groups (by income, age, marital status, gender) are most likely to leave negative feedback, and what should the company do about it?

**Project Structure**

├── online food delivery dataset.csv # Original dataset

├──correct online food delivery dataset.csv # Cleaned dataset (with Income_Rank, Gender_Clean)

├── onlinefood.py / .# Python cleaning, EDA and chi-square tests

├── Statistical Analysis.xlsx # Excel verification of chi-square test (optional)

├── Online Food Delivery.pbix # Power BI dashboard

├── Dashboard img.png # Dashboard screenshot

├── README.md # Project documentation


**Dataset**
388 customers, all based in the Bangalore area
Columns: Age, Gender, Marital Status, Occupation, Monthly Income, Educational Qualifications, Family size, Customer Type, latitude, longitude, Pin code, Output (reorder: Yes/No), Feedback (Positive/Negative), Corrected_Label
Class balance: 81.7% Positive vs 18.3% Negative feedback; 77.6% "Yes" vs 22.4% "No" for reorder
Profile: young (average age 24.6), student-dominated (53%), highly educated (90%+ Graduate or Post Graduate)

**Installation**

1️⃣ Clone the repository:

2️⃣ Install dependencies:
pip install pandas 
numpy 
matplotlib 
scipy

3️⃣ Open the Power BI file (`Online Food Delivery.pbix`) in Power BI Desktop to explore the dashboard.
Methodology

**Data Cleaning** 

1.	Fixed the mismatch between the Feedback and Label columns (Corrected_Label) - Converted columns to correct data types (numeric vs text) - Checked for missing values (none found) and impossible values (none found in Age, Family size, coordinates, Pin code)

2.	 Standardized Gender categories (including "Prefer not to say" as a separate "Undisclosed" group) - Encoded Monthly Income as an ordered rank (No Income = 0 up to More than 50000 = 4), treating "No Income" as a valid category, not missing data

**Exploratory Data Analysis (EDA)**

Summary statistics with `info()` and `describe()` - Category counts with `value_counts()` - Cross-tabulations of Feedback against Occupation, Income, Education, Customer Type, Marital Status, Gender and Age Group - Age grouped into Under 20, 21-25, 26-30, 31-40 

**Statistical Testing ChiSQTest**

square tests of independence between each factor and Feedback (significance level 0.05). Results were verified in both**Python (scipy)** and **Excel (CHISQ.TEST)**. Age was tested as age groups rather than individual ages, because individual ages produced expected counts below 5, which makes the chi-square test unreliable. 

**Dashboard**

Built a Power BI dashboard with DAX measures for Positive Feedback Count, Negative Feedback % and Reorder Rate, plus 100% stacked bar charts of feedback by income, marital status and age group.

**Key Findings**

 | Factor | Result | Significant? | 
|---|---|---| 
| Monthly Income | p = 0.0000080 | ✅ Yes |
 | Age Group | p = 0.0000434 | ✅ Yes |
 | Marital Status | p < 0.05 | ✅ Yes | 
| Gender | p = 0.3 | ❌ No | 

<img width="569" height="143" alt="Screenshot 2026-10-08 192935" src="https://github.com/user-attachments/assets/33271e94-1765-4c84-a33c-6659b1577ab8" />

<img width="433" height="138" alt="Screenshot 2026-10-08 192727" src="https://github.com/user-attachments/assets/38e19c19-689b-467a-9dfa-f8a3e2b72ac6" />

<img width="614" height="160" alt="Screenshot 2026-10-08 192707" src="https://github.com/user-attachments/assets/fad30381-ed7d-4ad5-b693-efc87de029c7" />

<img width="421" height="167" alt="Screenshot 2026-10-08 192626" src="https://github.com/user-attachments/assets/f95e7388-1da0-4fe0-99f5-e0b117a181b6" />

Income: "Below Rs.10000" customers had the highest negative feedback (44%), while "No Income" customers (mostly students) had the lowest (9%). 

<img width="751" height="451" alt="image" src="https://github.com/user-attachments/assets/122ed419-f11b-43e2-884e-b76338f46fba" />


 

Age:The 26-30 group was the least satisfied (35% negative), while the 21-25 group was the most satisfied (12%). 

<img width="752" height="452" alt="image" src="https://github.com/user-attachments/assets/127ea488-47d0-4643-8ef2-0417614429dc" />




Marital status: Married customers gave more negative feedback (28.7%) than single customers (13.1%).

<img width="752" height="452" alt="image" src="https://github.com/user-attachments/assets/3e5f1164-f720-4516-a676-4f4a5db3bf26" />


 
Gender: No statistically meaningful difference between male and female customers. 

<img width="752" height="452" alt="image" src="https://github.com/user-attachments/assets/d02505ae-64fb-4bc8-9373-a434069a648c" />



 
Note on small samples: Some groups are very small (Uneducated = 2, House wife = 9, Prefer not to say = 12), so percentages for these groups should not be treated as reliable conclusions. 

**Business Recommendations**

Run targeted satisfaction surveys for the 26-30 age group and low-income customers to identify their specific pain points (delivery time, pricing, portion size, quality). - Consider budget-friendly combos or loyalty offers for the "Below Rs.10000" income segment. - Improve family-size or bulk-order options for married customers. - Treat the reasons above as hypotheses to test, since this dataset shows *who* is dissatisfied but not *why*.

**Dashboard Preview (Dashboard img.png)** 

<img width="461" height="260" alt="Dashboard img" src="https://github.com/user-attachments/assets/35cd8d42-b9ec-4d5e-bc1e-9fdeba7a3ce8" />

 
**Technologies Used**

Python (Pandas, NumPy, Matplotlib, SciPy)

Microsoft Excel (Pivot Tables, CHISQ.TEST)

Power BI Desktop (DAX)

Jupyter Notebook / VS Code

**Future Improvements**

Build a machine learning model to predict negative feedback and reorder likelihood - Add the relationship between negative feedback and reorder intention (Feedback vs Output) as a deeper analysis - Use a larger or more varied dataset (this one covers only one city and mostly students) - Add customer comments or text data for sentiment analysis

