import gradio as gr
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("rf_model.pkl")  # Make sure you saved it from your notebook

def predict_price(qty, freight_value, category):
    input_data = pd.DataFrame({
        'qty': [qty],
        'freight_value': [freight_value],
        'product_category_name': [category]
    })
    prediction = model.predict(input_data)
    return round(prediction[0], 2)

demo = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Quantity"),
        gr.Number(label="Freight Value"),
        gr.Textbox(label="Product Category")
    ],
    outputs="number",
    title=" Retail Price Predictor",
    description="Predict optimal retail unit price based on product attributes"
)

demo.launch()
