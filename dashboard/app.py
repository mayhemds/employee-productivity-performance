import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("../cleaned_employee_performance.csv")
    return df

df = load_data()

# Title
st.title("📊 Employee Productivity & Performance Dashboard")

# Show Raw Data
if st.checkbox("Show Raw Data"):
    st.write(df)

# Bar Chart: Departments with Highest Productivity
st.subheader("📌 Average Performance Score by Department")
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=df["Department"], y=df["Performance Score"], ax=ax, ci=None)
plt.xticks(rotation=45)
st.pyplot(fig)

# Scatter Plot: Work Hours vs. Performance Score
st.subheader("📌 Work Hours vs. Performance Score")
fig, ax = plt.subplots(figsize=(8,5))
sns.scatterplot(x=df["Work Hours"], y=df["Performance Score"], ax=ax)
st.pyplot(fig)

# Heatmap: Correlation Matrix
st.subheader("📌 Correlation Heatmap")
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(df[["Work Hours", "Sick Days", "Projects Completed", "Performance Score"]].corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Identify Overworked Employees
st.subheader("⚠️ Overworked Employees (High Work Hours, Low Performance)")
overworked = df[(df["Work Hours"] > 50) & (df["Performance Score"] < 50)]
st.write(overworked)
