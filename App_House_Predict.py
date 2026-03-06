import streamlit as st
import pandas as pd
import joblib

@st.cache_resource 
def load_my_model():
    return joblib.load("model_h.pkl")

model = load_my_model()

st.title("🏠 نظام توقع أسعار العقارات")

st.sidebar.header("خصائص المنزل")



Square_Feet = st.sidebar.number_input("المساحة (Square Feet)", value=150)
Num_Bedrooms = st.sidebar.slider("عدد الغرف", 1, 5, 3)
Num_Bathrooms = st.sidebar.slider("عدد الحمامات", 1, 3, 2)
Num_Floors = st.sidebar.slider("عدد الأدوار", 1, 3, 1)
Year_Built = st.sidebar.number_input("سنة البناء", 1900, 2026, 2010)
Has_Garden = st.sidebar.selectbox("حديقة؟", [1, 0], format_func=lambda x: "نعم" if x == 1 else "لا")
Has_Pool = st.sidebar.selectbox("مسبح؟", [1, 0], format_func=lambda x: "نعم" if x == 1 else "لا")
Garage_Size = st.sidebar.slider("مساحة الجراج", 10, 50, 20)
Location_Score = st.sidebar.slider("تقييم الموقع", 0.0, 10.0, 5.0)
Distance_to_Center = st.sidebar.slider("البعد عن المركز", 0.0, 20.0, 10.0)

input_data = pd.DataFrame({
    'Square_Feet': [Square_Feet],
    'Num_Bedrooms': [Num_Bedrooms],
    'Num_Bathrooms': [Num_Bathrooms],
    'Num_Floors': [Num_Floors],
    'Year_Built': [Year_Built],
    'Has_Garden': [Has_Garden],
    'Has_Pool': [Has_Pool],
    'Garage_Size': [Garage_Size],
    'Location_Score': [Location_Score],
    'Distance_to_Center': [Distance_to_Center]
})


if st.button("احسب السعر المتوقع"):
    prediction = model.predict(input_data)
    
    predicted_price = float(prediction[0])
    
    st.success(f"💰 السعر التقديري هو: ${predicted_price:,.2f}")
