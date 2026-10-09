import pandas as pd
df = pd.read_csv(r"C:\Users\Dell\Documents\python prog\correct online food delivery dataset.csv")

print(df.info())
print(df.describe())

for col in ['Gender', 'Marital Status', 'Occupation', 'Monthly Income', 'Educational Qualifications', 'Customer Type', 'Feedback', 'Output']:
    print(f"\n{col}:")
    print(df[col].value_counts())



print(pd.crosstab(df['Occupation'], df['Feedback'], normalize='index') * 100)
print(pd.crosstab(df['Monthly Income'], df['Feedback'], normalize='index') * 100)
print(pd.crosstab(df['Educational Qualifications'], df['Feedback'], normalize='index') * 100)
print(pd.crosstab(df['Customer Type'], df['Feedback'], normalize='index') * 100)

from scipy.stats import chi2_contingency

#crosstab
contingency_table = pd.crosstab(df['Monthly Income'], df['Feedback'])
print(contingency_table)

# Step 2: Chi-square test 
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

print(f"\nChi-square statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")
print(f"Degrees of freedom: {dof}")

print(pd.crosstab(df['Age_Group'], df['Feedback'], normalize='index') * 100)

