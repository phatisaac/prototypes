import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("pcs.csv")

# App title
st.title("Health & Lifestyle Dashboard")

# Dataset preview
st.subheader("Dataset Preview")
st.write(df.head())

# Sidebar filters
st.sidebar.header("User Input")
smoking_filter = st.sidebar.selectbox("Smoking Status", options=df["Smoking"].unique())
filtered_df = df[df["Smoking"] == smoking_filter]

st.subheader(f"Records with Smoking Status = {smoking_filter}")
st.write(filtered_df)

# Age category distribution
st.subheader("Age Category Distribution")
st.bar_chart(df["age_cat"].value_counts())

# --- UPDATED ITEM ---
# Line plot: Income vs PCS
st.subheader("Line Plot: Income vs PCS")
fig_line, ax_line = plt.subplots()
sns.lineplot(x="income", y="PCS", data=df, marker="o", ax=ax_line)
ax_line.set_xlabel("Income")
ax_line.set_ylabel("PCS")
st.pyplot(fig_line)

# Boxplot: PCS vs Income
st.subheader("Boxplot: PCS vs Income")
fig1, ax1 = plt.subplots()
sns.boxplot(x="income", y="PCS", data=df, ax=ax1)
st.pyplot(fig1)

# Boxplot: MCS vs Educationlevel
st.subheader("Boxplot: MCS vs Education Level")
fig2, ax2 = plt.subplots()
sns.boxplot(x="Educationlevel", y="MCS", data=df, ax=ax2)
st.pyplot(fig2)

# Line plot: MCS vs Age
st.subheader("Line Plot: MCS vs Age")
fig3, ax3 = plt.subplots()
sns.lineplot(x="age_cat", y="MCS", data=df, marker="o", ax=ax3)
ax3.set_xlabel("Age Category")
ax3.set_ylabel("MCS")
st.pyplot(fig3)
