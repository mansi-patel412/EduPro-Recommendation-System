🎓 EduPro Recommendation System
An AI-powered course recommendation system that segments learners based on their behavior and preferences and suggests personalized courses using Machine Learning clustering techniques.

📌 Project Overview
Online learning platforms often struggle to recommend relevant courses due to diverse learner interests and behaviors.
The **EduPro Recommendation System** solves this problem by analyzing learner engagement data and grouping users into clusters. Based on cluster behavior, the system recommends suitable courses tailored to each learner.

🚀 Features
- Learner segmentation using Machine Learning
- Personalized course recommendations
- Interactive Streamlit dashboard
- User cluster identification
- Real-time recommendation display

🧠 Machine Learning Approach
#Clustering Algorithm
- K-Means Clustering
- Used to group learners based on behavior patterns
  
#Feature Engineering
Learner profiles were created using:
- Course category preferences
- Enrollment behavior
- Spending patterns
- Diversity score
- Learning depth index
- Engagement metrics

#Data Preprocessing
- Missing value handling
- Infinite value handling
- Feature scaling using StandardScaler

🛠️ Tech Stack
#Programming Language
- Python

#Libraries
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

#Tools
- Google Colab
- VS Code
- GitHub

📊 Dataset
The project uses synthetic EduPro platform data containing:
- Users data
- Courses data
- Transactions data
- Learner aggregated profiles

🖥️ Streamlit Dashboard

The web application allows users to:

1. Select a learner ID
2. View learner cluster
3. View recommended courses dynamically

⚙️ Installation & Setup
#Step 1: Clone Repository

git clone https://github.com/YOUR_USERNAME/EduPro-Recommendation-System.git
cd EduPro-Recommendation-System

Step 2: Install Dependencies

pip install -r requirements.txt

 Step 3: Run Application

streamlit run app.py

📁 Project Structure
EduPro_Recommendation_System/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── courses.csv
│   ├── learner_profiles.csv
│
├── models/
│   ├── kmeans_model.pkl
│   ├── scaler.pkl
│
└── notebook/
    └── training_pipeline.ipynb

📈 Future Improvements
- Add collaborative filtering recommendations
- Deploy application on cloud platform
- Add authentication system
- Improve UI and user experience
- Add model evaluation dashboard

🌍 Applications
- Online Learning Platforms
- EdTech Personalization Systems
- Skill Development Platforms
- AI-based Learning Assistants

👩‍💻 Author

**Mansi Patel**  
Machine Learning & Data Science Enthusiast

🔗 Live Demo
Deployed Streamlit App: https://edupro-recommendation-system-jwuokvh7fqmy7xrkbypvhz.streamlit.app/

