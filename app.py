import streamlit as st
import pandas as pd
import joblib

st.title("EduPro Recommendation System")

# Load data
learner_profiles = pd.read_csv("data/learner_profiles.csv")
courses = pd.read_csv("data/courses.csv")

# Load model
kmeans = joblib.load("models/kmeans_model.pkl")

# Select User
user_id = st.selectbox("Select User", learner_profiles["UserID"])

user_data = learner_profiles[learner_profiles["UserID"] == user_id]

cluster = user_data["Cluster"].values[0]

st.write("User Cluster:", cluster)

# Dummy recommendation (replace later)
recommended = courses.sample(5)

st.write("Recommended Courses")
st.dataframe(recommended)
