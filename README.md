# A E R O F I T    E X P L O R A T O R Y    D A T A    A N A L Y S I S    ( E D A )

# Table of Contents

- [Introduction](#introduction)
- [Project Details](#project-details)
  - [Product Portfolio](#product-portfolio)
- [Data Description](#data-description)
- [Data Exploration and Processing](#data-exploration-and-processing)
  - [Data Import and Overview](#data-import-and-overview)
  - [Statistical Summary](#statistical-summary)
    - [Categorical Features](#categorical-features)
    - [Numerical Features](#numerical-features)
  - [Non-Graphical Analysis](#non-graphical-analysis)
    - [Value Counts](#value-counts)
    - [Unique Attributes](#unique-attributes)
  - [Graphical Analysis](#graphical-analysis)
    - [Univariate Analysis - Numerical Features](#univariate-analysis---numerical-features)
    - [Univariate Analysis - Categorical Features](#univariate-analysis---categorical-features)
    - [Bivariate Analysis](#bivariate-analysis)
    - [Multivariate Analysis](#multivariate-analysis)
- [Correlation Analysis](#correlation-analysis)
  - [Graph](#graph)
  - [Observations From the Heatmap](#observations-from-the-heatmap)
    - [Strong Positive Correlation](#strong-positive-correlation)
    - [Moderate Correlation](#moderate-correlation)
    - [Weak or No Correlation](#weak-or-no-correlation)
- [Outlier Detection](#outlier-detection)
- [Conditional Probabilities](#conditional-probabilities)
  - [Product Purchases](#product-purchases)
  - [Product – Gender](#product--gender)
  - [Product – Age](#product--age)
  - [Product – Income](#product--income)
  - [Product – Fitness](#product--fitness)
  - [Product – Marital Status](#product--marital-status)
- [Customer Demographics](#customer-demographics)
  - [Gender Distribution](#gender-distribution)
  - [Age Distribution](#age-distribution)
  - [Income Analysis](#income-analysis)
    - [Low-Income Customer Insights](#low-income-customer-insights)
    - [High-Income Customer Insights](#high-income-customer-insights)
  - [Fitness Level Insights](#fitness-level-insights)
    - [Fitness Level 5 Analysis](#fitness-level-5-analysis)
  - [Marital Status Analysis](#marital-status-analysis)
- [Insights and Recommendations](#insights-and-recommendations)
  - [Target Audience](#target-audience)
    - [Insight](#insight)
    - [Recommendation](#recommendation)
  - [Product Portfolio](#product-portfolio-1)
    - [Insight](#insight-1)
    - [Recommendation](#recommendation-1)
  - [Gender Preferences](#gender-preferences)
    - [Insight](#insight-2)
    - [Recommendation](#recommendation-2)
  - [Income Segmentation](#income-segmentation)
    - [Insight](#insight-3)
    - [Recommendation](#recommendation-3)
  - [Fitness Level Targeting](#fitness-level-targeting)
    - [Insight](#insight-4)
    - [Recommendation](#recommendation-4)
  - [Marital Status](#marital-status)
    - [Insight](#insight-5)
    - [Recommendation](#recommendation-5)
  - [Usage Frequency and Distance](#usage-frequency-and-distance)
    - [Insight](#insight-6)
    - [Recommendation](#recommendation-6)
- [Conclusion](#conclusion)


# Introduction
This report presents a thorough analysis of customer demographics, purchasing behavior, and product performance related to Aerofit treadmills. The primary objective is to derive actionable insights and recommendations that can guide marketing strategies, product development, and customer engagement initiatives. By investigating the characteristics of the target audience for each type of treadmill, Aerofit aims to enhance its recommendations to new customers.

# Project Details
The market research team at Aerofit seeks to identify the characteristics of the target audience for each type of treadmill offered by the company. The insights gathered will inform marketing strategies and product development.

## Product Portfolio
- **KP281**: Entry-level treadmill, priced at $1,500.
- **KP481**: Mid-level treadmill designed for runners, priced at $1,750.
- **KP781**: Advanced treadmill with premium features, priced at $2,500.

# Data Description
The dataset, `aerofit_treadmill_data.csv`, contains information on individuals who purchased a treadmill from Aerofit stores over the past three months. The features included are:
- **Product**: Type of product purchased (KP281, KP481, or KP781).
- **Age**: Customer age in years.
- **Gender**: Customer gender (male/female).
- **Education**: Education level in years.
- **MaritalStatus**: Customer marital status (single or partnered).
- **Usage**: Average number of times the customer plans to use the treadmill each week.
- **Fitness**: Self-rated fitness level on a scale of 1-5.
- **Income**: Annual income in US dollars.
- **Miles**: Average number of miles the customer expects to walk/run each week.

# Data Exploration and Processing
## Data Import and Overview
- The data is imported using pandas for analysis.
- The shape of the DataFrame is checked to understand the number of rows and columns.
- Data types of each column are verified to ensure proper analysis.
- A check for missing values is performed to assess data quality.
- The dataset is scanned for duplicate entries.

## Statistical Summary
A statistical summary is generated for both categorical and numerical features. Key observations include:

### Categorical Features
Distribution of gender, marital status, and product types.

### Numerical Features
Summary statistics, including mean, median, and standard deviation for age, income, usage, fitness, and miles.

## Non-Graphical Analysis
### Value Counts
Counts of unique values for all categorical features are documented.

### Unique Attributes
The unique attributes for each categorical feature are listed.

## Graphical Analysis
### Univariate Analysis - Numerical Features
- **Distribution Plot**: Visualizes the distribution of numerical features such as age, income, and usage.
- **Count Plot**: Shows the frequency of different fitness levels and product types.
- **Box Plot**: Identifies the spread and potential outliers in numerical features.

### Univariate Analysis - Categorical Features
- **Count Plot**: Visualizes the distribution of categorical features like gender and marital status.

### Bivariate Analysis
- **Product vs. Gender**: Analyzes the relationship between the product purchased and the customer's gender.
- **Product vs. Marital Status**: Examines how marital status influences product choice.
- **Product vs. Age**: Explores the relationship between product choice and customer age.

### Multivariate Analysis
- **Pair Plots**: Shows relationships among multiple features simultaneously.

## Correlation Analysis
### Graph
Provides a heatmap visualizing correlation values between different features.

### Observations From the Heatmap
#### Strong Positive Correlation:
- **Miles** and **Usage** (0.76): Indicates that customers planning to use the treadmill more often tend to cover more miles.
- **Income** and **Miles** (0.54): Suggests that higher-income individuals tend to cover more miles.
- **Income** and **Usage** (0.52): Shows that those with higher incomes tend to use the treadmill more frequently.
- **Age** and **Fitness** (0.61): Implies that older individuals rate their fitness higher.
- **Education** and **Income** (0.63): Indicates that users with higher education levels have higher incomes.

#### Moderate Correlation:
- **Age** and **Income** (0.51): Suggests a potential trend where older individuals tend to have higher incomes.
- **Education** and **Age** (0.63): Shows that higher-educated individuals may be older.

#### Weak or No Correlation:
- **Fitness** and **Miles** (0.06): Indicates that self-rated fitness doesn’t strongly influence miles planned.
- **Fitness** and **Usage** (0.05): Shows a weak correlation between fitness level and treadmill usage per week.

## Outlier Detection
Outliers are detected using the Interquartile Range (IQR) method, allowing identification of extreme values that may affect analysis.

## Conditional Probabilities
### Product Purchases
The percentage of customers purchasing KP281, KP481, or KP781 is calculated.

### Product – Gender
- **Percentage of Male Customers Purchasing**: Shows the male purchase percentage for KP781.
- **Percentage of Female Customers for KP281**: Indicates the probability of a customer being female for KP281.

### Product – Age
The percentage of customers aged between 20 and 30 among all customers.

### Product – Income
- **Percentage of Low-Income Customers Purchasing**: Indicates low-income customer percentage for each treadmill.
- **Percentage of High-Income Customers for KP781**: Indicates high-income customer trends for KP781.

### Product – Fitness
- **Percentage of Customers with Fitness Level 5**: Percentage of highly fit customers purchasing KP781.
  
### Product – Marital Status
- **Percentage of Partnered Customers Using Treadmills**: Shows the trend of partnered customer usage.

# Customer Demographics
## Gender Distribution
- **Total Females Who Bought KP781**: 7
- **Percentage of Females Buying KP781**: 17.5%
- **Total Females Who Bought KP281**: 40
- **Total Purchases of KP281**: 80
- **Probability of Customer Being Female for KP281**: 0.5

## Age Distribution
- **Customers Aged 20s to 30s**: 67
- **Percentage of Customers Aged 20s to 30s**: 37.22%

## Income Analysis
### Low-Income Customer Insights
- **Low-Income Customers (Income ≤ $50,000)**: 83
- **Percentage of Low-Income Customers Purchasing**: 46.11%

### High-Income Customer Insights
- **High-Income Customers (Income ≥ $80,000)**: 19
- **Percentage of High-Income Customers Purchasing KP781**: 47.5%

## Fitness Level Insights
### Fitness Level 5 Analysis
- **Percentage of Customers with Fitness Level 5**: 17.22%
- **Percentage of Fitness Level 5 Customers Buying KP781**: 93.55%

## Marital Status Analysis
- **Total Partnered Customers**: 107
- **Percentage of Partnered Customers**: 59.44%
# Insights and Recommendations
Based on the comprehensive analysis of the dataset, the following actionable insights and recommendations are provided to improve product offerings, customer targeting, and business strategies for Aerofit treadmills:

## Target Audience
### Insight
A significant portion of customers purchasing treadmills belongs to the 20-30 age range and has a higher likelihood of preferring mid to premium products.

### Recommendation
Target marketing efforts towards younger, fitness-oriented demographics, especially for KP481 and KP781 models, using social media platforms popular among this age group, such as Instagram and TikTok.

## Product Portfolio
### Insight
Each product type has a clear demographic preference in terms of age, income, and fitness level. The KP281 is favored by lower-income and less frequent users, while KP481 and KP781 attract higher-income, frequent users.

### Recommendation
Refine product features and marketing for each customer group based on the treadmill model most likely to attract them. For example, promote the KP281 as an entry-level treadmill suitable for casual users, while emphasizing the advanced features of the KP781 for seasoned athletes and fitness enthusiasts.

## Gender Preferences
### Insight
Males are more likely to purchase the premium KP781 treadmill, while females more commonly choose the entry-level KP281.

### Recommendation
Develop targeted marketing campaigns that appeal to the motivations of each gender. For instance, emphasize the KP781's advanced tracking and performance metrics in male-targeted campaigns, while promoting the KP281 as a versatile, compact treadmill in female-oriented ads.

## Income Segmentation
### Insight
High-income customers tend to prefer the KP781, while low-income customers are more likely to choose the KP281.

### Recommendation
Implement tiered financing or installment payment options to make higher-end models like the KP781 more accessible to lower-income customers, potentially increasing overall sales.

## Fitness Level Targeting
### Insight
Customers with a high self-rated fitness level (Fitness level 5) are predominantly purchasing the KP781, indicating a strong alignment with serious fitness goals.

### Recommendation
Position the KP781 as the treadmill of choice for serious fitness enthusiasts and athletes. Consider partnerships with fitness influencers or professional trainers to reinforce this positioning.

## Marital Status
### Insight
A majority of the partnered customers are purchasing mid to high-end treadmills, which may indicate shared household investments in fitness equipment.

### Recommendation
Target partnered individuals with special offers on mid to high-end treadmills, such as discounted rates on family memberships or bundle deals with fitness accessories.

## Usage Frequency and Distance
### Insight
Customers who plan on higher usage frequencies and covering more miles are naturally more inclined to invest in mid-to-premium models like KP481 and KP781.

### Recommendation
Emphasize durability, advanced tracking features, and customizability in the marketing materials for KP481 and KP781 models to attract customers who prioritize consistent usage and higher mileage.

# Conclusion
This analysis has highlighted key demographics, behavioral traits, and product preferences among Aerofit’s treadmill customers. By tailoring marketing strategies, enhancing product features, and implementing tiered pricing options, Aerofit can more effectively meet the diverse needs of its customer base. With a strong focus on younger, fitness-driven demographics and opportunities for expanded reach among partnered households, Aerofit is positioned to strengthen its market share and improve customer satisfaction.

