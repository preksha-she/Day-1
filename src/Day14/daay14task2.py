
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler


data = {
    'Age': [22, 25, 47, 52, 46, 56],
    'Salary': [25000, 30000, 80000, 110000, 95000, 120000]
}

df = pd.DataFrame(data)

# -------------------------------
# Standardization (Mean = 0, Std = 1)
# -------------------------------
standard_scaler = StandardScaler()
df_standardized = standard_scaler.fit_transform(df)

df_standardized = pd.DataFrame(
    df_standardized,
    columns=['Age_Standardized', 'Salary_Standardized']
)

# -------------------------------
# Normalization (Range 0 to 1)
# -------------------------------
minmax_scaler = MinMaxScaler()
df_normalized = minmax_scaler.fit_transform(df)

df_normalized = pd.DataFrame(
    df_normalized,
    columns=['Age_Normalized', 'Salary_Normalized']
)

# -------------------------------
# Histograms
# -------------------------------

# Before scaling
plt.hist(df['Salary'], bins=5)
plt.title("Salary Before Scaling")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# After standardization
plt.hist(df_standardized['Salary_Standardized'], bins=5)
plt.title("Salary After Standardization")
plt.xlabel("Standardized Salary")
plt.ylabel("Frequency")
plt.show()

# After normalization
plt.hist(df_normalized['Salary_Normalized'], bins=5)
plt.title("Salary After Normalization")
plt.xlabel("Normalized Salary")
plt.ylabel("Frequency")
plt.show()