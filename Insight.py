import pandas as pd
from scipy.stats import chi2_contingency

from pathlib import Path

df = pd.read_csv(r"C:\Users\Dell\Documents\GitHub Projects\Online food delivey\corect online food delivery dataset.csv")      #\corect online food delivery dataset")

# Ek helper function: percentage table + chi-square test
def chi_test(col, data):
    table = pd.crosstab(data[col], data['Feedback'])
    chi2, p, dof, expected = chi2_contingency(table)
    print(f"\n{col}: p-value = {p:.6f}, smallest expected count = {expected.min():.1f}")
    print((pd.crosstab(data[col], data['Feedback'], normalize='index') * 100).round(1))
    if expected.min() < 5:
        print("Warning: expected count below 5, result not reliable")

# 1. Occupation vs Feedback (poore data par)
chi_test('Occupation', df)

# 2. Feedback vs Output (kya negative feedback wale reorder nahi karte?)
print("\nFeedback vs Output:")
print((pd.crosstab(df['Feedback'], df['Output'], normalize='index') * 100).round(1))

# 3. Sirf non-students par test
work = df[df['Occupation'] != 'Student'].copy()
print("\nNon-student rows:", len(work))

work['Age_Group'] = pd.cut(work['Age'], bins=[0, 25, 30, 40], labels=['Up to 25', '26-30', '31-40'])

chi_test('Age_Group', work)
chi_test('Monthly Income', work)
chi_test('Marital Status', work)



# 1. Feedback vs Output ka p-value
t = pd.crosstab(df['Feedback'], df['Output'])
print(t)
print("Feedback vs Output p-value:", f"{chi2_contingency(t)[1]:.2e}")

# 2. Occupation, House wife (chhota group) hata kar
chi_test('Occupation', df[df['Occupation'] != 'House wife'])

# 3. Marital Status, poore data par, 'Prefer not to say' hata kar
chi_test('Marital Status', df[df['Marital Status'] != 'Prefer not to say'])

# 4. Marital Status, non-students par, 'Prefer not to say' hata kar
chi_test('Marital Status', work[work['Marital Status'] != 'Prefer not to say'])

# 5. Non-students mein income groups ka size
print(work['Monthly Income'].value_counts())



print(pd.crosstab(df['Occupation'], df['Marital Status']))
print(work['Age_Group'].value_counts())