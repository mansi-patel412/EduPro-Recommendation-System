import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.title("EduPro Recommendation System")

# ---------------- Load Data ----------------
learner_profiles = pd.read_csv("data/learner_profiles.csv")
courses = pd.read_csv("data/courses.csv")

# ---------------- Load Model ----------------
kmeans = joblib.load("models/kmeans_model.pkl")

# ---------------- Select User ----------------
user_id = st.selectbox("Select User", learner_profiles["UserID"])

user_data = learner_profiles[learner_profiles["UserID"] == user_id]
cluster = user_data["Cluster"].values[0]

st.write("User Cluster:", cluster)

# =====================================================
# ⭐ Learner Profile Explorer
# =====================================================
st.markdown("---")
st.subheader("Learner Profile Explorer")

st.dataframe(user_data)

# =====================================================
# ⭐ Cluster Visualization Dashboard
# =====================================================
st.markdown("---")
st.subheader("Cluster Visualization Dashboard")

cluster_counts = learner_profiles["Cluster"].value_counts().sort_index()

fig, ax = plt.subplots()
ax.bar(cluster_counts.index.astype(str), cluster_counts.values)
ax.set_xlabel("Cluster")
ax.set_ylabel("Number of Learners")
ax.set_title("Learners per Cluster")

st.pyplot(fig)

# =====================================================
# ⭐ Personalized Course Recommendation
# =====================================================

# Dummy Recommendation Based On Cluster
# (Later you can replace with real recommendation logic)
recommended = courses.sample(10)

# =====================================================
# ⭐ Filter Recommendations
# =====================================================
st.markdown("---")
st.subheader("Filter Recommendations")

level_filter = st.selectbox(
    "Select Course Level",
    ["All"] + list(courses["CourseLevel"].unique())
)

category_filter = st.selectbox(
    "Select Course Category",
    ["All"] + list(courses["CourseCategory"].unique())
)

filtered_courses = recommended.copy()

if level_filter != "All":
    filtered_courses = filtered_courses[
        filtered_courses["CourseLevel"] == level_filter
    ]

if category_filter != "All":
    filtered_courses = filtered_courses[
        filtered_courses["CourseCategory"] == category_filter
    ]

# ---------------- Show Recommendations ----------------
st.subheader("Recommended Courses")
st.dataframe(filtered_courses)

# =====================================================
# ⭐ Segment Comparison Panel
# =====================================================
st.markdown("---")
st.subheader("Segment Comparison Panel")

cluster_summary = learner_profiles.groupby("Cluster").mean(numeric_only=True)

st.dataframe(cluster_summary)
