import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Blood Pressure Gauge
st.title("Health Monitoring App")

# Function to create a gauge
def plot_blood_pressure_gauge(current_reading):
    zones = [60, 90, 120, 140, 180]  # mmHg values
    colors = ['green', 'yellow', 'red']
    labels = ['Safe Zone', 'Caution Zone', 'High Risk Zone']
    
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(polar=True))
    
    for i in range(len(zones) - 1):
        theta = np.linspace(np.deg2rad(180), np.deg2rad(0), 100)
        r = np.array([zones[i], zones[i]] * 50)
        ax.fill_between(theta, r, color=colors[i], alpha=0.6)
        ax.text(np.deg2rad(90), (zones[i] + zones[i+1]) / 2, labels[i], horizontalalignment='center')
    
    ax.plot(np.deg2rad(90), current_reading, 'ro', markersize=10)
    ax.set_ylim(0, 180)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_title("Blood Pressure Reading: {}".format(current_reading))

    st.pyplot(fig)

# User input for blood pressure reading
current_reading = st.number_input("Enter your blood pressure reading (systolic):", min_value=60, max_value=180, value=120)
plot_blood_pressure_gauge(current_reading)

# Blood Sugar Tracking Chart
st.title("Blood Sugar Tracking Chart")

data = {
    "Time of Day": ["Fasting", "Before Meal", "1-2 Hours After Meal"],
    "Target Range (mg/dL)": ["70 - 100", "70 - 130", "Less than 180"]
}

df = pd.DataFrame(data)
st.table(df)

# Asthma Information
st.title("Asthma Management")
st.write("""
- **Symptoms:** Coughing, wheezing, shortness of breath, chest tightness.
- **Management:** Use of inhalers, avoiding triggers, regular check-ups.
- **Peak Flow Monitoring:** Regularly check your peak flow to track asthma control.
""")

# COPD Information
st.title("COPD Management")
st.write("""
- **Symptoms:** Chronic cough, mucus production, shortness of breath.
- **Management:** Quit smoking, pulmonary rehabilitation, medications (inhalers).
- **Monitoring:** Keep track of exacerbations and lung function tests.
""")

# Cardiovascular Diseases Information
st.title("Cardiovascular Health")
st.write("""
- **Risk Factors:** High blood pressure, high cholesterol, smoking, diabetes, obesity.
- **Management:** Regular exercise, healthy diet, medication adherence, routine check-ups.
- **Monitoring:** Keep track of blood pressure, cholesterol levels, and heart rate.
""")

# Stress Management Section
st.title("Stress Management")
st.write("""
- **Symptoms of Stress:** Anxiety, irritability, fatigue, sleep disturbances, physical symptoms (headaches, muscle tension).
- **Management Techniques:** 
  - Practice mindfulness and meditation
  - Regular physical activity
  - Maintain a healthy work-life balance
  - Seek social support from friends and family
  - Consider professional help if needed
- **Monitoring Stress Levels:** 
  - Keep a journal to track stress triggers and coping mechanisms
  - Use stress assessment tools or apps to evaluate your stress levels regularly
""")
