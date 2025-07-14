#  Retail Price Optimization using Machine Learning

An end-to-end machine learning project focused on predicting the **optimal retail unit price** for products using **real-world sales data** and **advanced regression techniques**. This project combines data analytics, model building, and deployment into a user-friendly web interface.

---

##  Problem Statement

In today’s dynamic retail environment, setting the right price is crucial for:
-  Maximizing revenue
-  Retaining customers
-  Staying competitive

Traditionally, pricing decisions were based on intuition or static rules. This project leverages **machine learning models** to make **data-driven pricing decisions** by analyzing:
- Product attributes
- Cost-related features
- Seasonal and category trends
- Historical unit prices and sales behavior

---

##  Project Goals

1. **Predict optimal retail price** using regression models
2. Analyze key pricing features such as freight value, product category, quantity, etc.
3. Provide an **interactive Gradio interface** for end users (non-technical stakeholders)
4. Help businesses implement **dynamic pricing** to boost margins and efficiency

---

##  Dataset Overview

- **File Name**: `retail_price.csv`
- **Rows**: 676
- **Columns**: 30
- **Target Column**: `unit_price`

###  Key Features Used:
- `qty`: Quantity purchased
- `freight_value`: Delivery cost
- `product_category_name`: Category of product
- `price`: Historical price
- `product_weight_g`: Weight of item
- `product_photos_qty`: Visual quality indicator
- ... (plus 20+ more features)

---

##  Data Preprocessing Steps

1. **Missing Value Handling** – Imputed or removed null values
2. **Categorical Encoding** – Converted category features using `LabelEncoder`
3. **Feature Scaling** – Standardized numerical values
4. **Feature Selection** – Selected top contributors using correlation analysis
5. **Data Split** – Training/Testing split (80/20)

---

## 🤖 Machine Learning Models

| Model                   | R² Score | Accuracy  | MAE   | MSE   |
|------------------------|----------|-----------|-------|--------|
| Linear Regression       | 0.9882   | 98.8%     | 3.14  | 47.03  |
| Decision Tree Regressor| 0.9881   | 98.8%     | 3.14  | 47.03  |
| ✅ Random Forest Regressor | **0.9913** | **99.1%** | **3.14** | **47.03** |

✅ **Random Forest Regressor** was chosen for final deployment due to its superior performance and ability to capture nonlinear relationships.

---

##  Exploratory Data Analysis (EDA)

- **Histogram** – Showed skewed distribution in unit prices
- **Scatter Plots** – Revealed correlation between freight value and final price
- **Box Plot** – Detected outliers in high-priced categories
- **Correlation Heatmap** – Helped select top 10 contributing features

---

##  Key Insights

- Freight value has a strong positive impact on unit price
- Quantity ordered influences pricing decisions significantly
- Certain product categories consistently have higher unit prices
- Random Forest outperforms linear methods due to feature interaction

---

##  Gradio Interface

A simple, interactive web app created using **Gradio** allows users to:
- Input product details (quantity, category, freight)
- Instantly get the predicted **optimal price**
- Useful for retailers, sales analysts, and marketing teams

---
![Gradio App](https://github.com/iamsunaina1/Retail-Price-Optimization/blob/main/gradio%20preview.png)


##  How to Run This Project

### 1. Clone the repo
```bash
git clone https://github.com/iamsunaina1/Retail-Price-Optimization.git
cd Retail-Price-Optimization


