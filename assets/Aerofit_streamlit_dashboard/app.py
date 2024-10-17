import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv("C:\\Users\\Khola Shams\\Dropbox\\PC (3)\\Downloads\\EDA portfolio proj-due 14\\Aerofit_streamlit_dashboard\\aerofit_treadmill_data.csv")  # Update with your actual file path

df = load_data()

# Title of the app
st.title("Customer Insights Dashboard")

# Display data
if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(df)

# Data Overview
st.subheader('Data Overview')
st.write(df.describe())

# Conditional Probability Analysis
# Calculate percentage of customers purchasing each product
percentage_cust = round(df["Product"].value_counts(normalize=True) * 100, 2)
customer_product_purchased = pd.DataFrame({
    "Product": percentage_cust.index,
    "Percentage (%)": percentage_cust.values
})

# Display product purchase percentages
st.subheader("Percentage of Customers Purchasing Each Product")
st.write(customer_product_purchased)

# Calculate percentage of male customers
male_count = round((df["Gender"].value_counts(normalize=True)["Male"]) * 100, 2)
male_customers_purchased = pd.DataFrame({
    "Gender": ["Males"],
    "Percentage (%)": male_count
})

# Display male customer percentage
st.subheader("Percentage of Male Customers")
st.write(male_customers_purchased)

# Calculate count of customers who bought KP781 by gender
female_count_KP781 = df[(df["Product"] == "KP781")]["Gender"].value_counts().get("Female", 0)
female_KP781_percentage = round((df[(df["Product"] == "KP781")]["Gender"].value_counts(normalize=True).get("Female", 0)) * 100, 2)
female_KP781_fact = pd.DataFrame({
    "Gender": ["Females"],
    "Percentage (%) of Females who bought KP781": female_KP781_percentage
})

# Display females who bought KP781
st.subheader("Percentage of Females Who Bought KP781")
st.write(female_KP781_fact)

# Count of females who bought KP281
female_count_KP281 = df[df["Product"] == "KP281"]["Gender"].value_counts().get("Female", 0)
KP281_count = df["Product"].value_counts().get("KP281", 0)
probability_female_KP281 = female_count_KP281 / KP281_count if KP281_count > 0 else 0

probability_fact = pd.DataFrame({
    "Gender": ["Female"],
    "Female_KP281_Count": female_count_KP281,
    "KP281_Count": KP281_count,
    "Probability of Customer Being Female and Product is KP281": probability_female_KP281
})

# Display probability of female customers buying KP281
st.subheader("Probability of Female Customers Buying KP281")
st.write(probability_fact)

# Calculate percentage of customers aged between 20s and 30s
age_percentage = round(((df["Age"] >= 20) & (df["Age"] < 30)).sum() / df.shape[0] * 100, 2)  # Fixed parentheses
age_percentage_fact = pd.DataFrame({
    "Age": ["20s to 30s"],
    "Percentage (%)": age_percentage
})

# Display age percentage
st.subheader("Percentage of Customers Aged Between 20s and 30s")
st.write(age_percentage_fact)

# Low-income threshold analysis
low_income_threshold = 50000
low_income_customers = df[df["Income"] <= low_income_threshold]
percentage_low_income = (low_income_customers.shape[0] / df.shape[0]) * 100
low_income_fact = pd.DataFrame({
    "Income": ["Low Income"],
    "Percentage (%)": round(percentage_low_income, 2)
})

# Display low income percentage
st.subheader("Percentage of Low Income Customers")
st.write(low_income_fact)

# Insights and Recommendations
st.subheader("Insights and Recommendations")
st.write("""
1. **Product Purchases**: A significant portion of customers prefer KP781 and KP281. Targeted marketing campaigns focusing on these products can enhance sales further.

2. **Demographics**: The majority of customers are in their 20s and 30s, suggesting marketing strategies should focus on platforms that attract younger demographics.

3. **Gender Analysis**: While a considerable percentage of male customers purchase, there's room to improve engagement with female customers, especially regarding KP281.

4. **Low Income Segment**: A notable percentage of customers fall into the low-income category. Consider offering special discounts or products tailored to this segment.

5. **Recommendation**: Conduct further qualitative research to understand preferences better and to refine product offerings and marketing strategies based on demographic insights.
""")

# Visualization of customer demographics
st.subheader("Visualizations")
fig, ax = plt.subplots()
df['Age'].hist(bins=10, ax=ax, alpha=0.7, color='blue')
ax.set_title('Age Distribution of Customers')
ax.set_xlabel('Age')
ax.set_ylabel('Number of Customers')
st.pyplot(fig)

# Visualizing income distribution
fig, ax = plt.subplots()
df['Income'].hist(bins=20, ax=ax, alpha=0.7, color='green')
ax.set_title('Income Distribution of Customers')
ax.set_xlabel('Income')
ax.set_ylabel('Number of Customers')
st.pyplot(fig)

