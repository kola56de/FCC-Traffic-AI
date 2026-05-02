# 🚍 FCC Traffic AI

An AI-powered traffic prediction platform built with **Streamlit**, **Machine Learning**, and **Pretrained Models** to forecast traffic speed, travel time, congestion level, and road condition using transportation route data.

🔗 **Live App:** https://k-fcc-traffic-ai.streamlit.app/

---

## 📌 Project Overview

Traffic congestion affects productivity, commuter experience, and city efficiency. This project provides an intelligent solution that predicts route traffic conditions based on road segment characteristics and operational parameters.

The system uses trained machine learning models to estimate:

- Vehicle speed  
- Travel time  
- Traffic congestion level  
- Road condition quality  

Users can select routes, segments, time periods, and traffic factors to receive instant predictions.

---

## 🚀 Features

### 📄 Dataset Preview

Displays the uploaded traffic dataset and confirms successful loading.

### 🔍 Smart Route Inputs

Users can customize:

- Route  
- Segment  
- Time Period (AM / PM)  
- Distance (km)  
- Peak Delay Source  
- Running Speed (km/h)  
- Percent Time Delay (%)  
- Level of Service  

### 🤖 Multi-Model Prediction Engine

Uses saved `.pkl` machine learning models:

- `speed_model.pkl` → Predict speed  
- `time_model.pkl` → Predict travel time  
- `traffic_model.pkl` → Predict traffic level  
- `condition_model.pkl` → Predict road condition  

### 📊 Prediction Results

Displays results in clean dashboard metrics:

- 🚗 Predicted Speed (km/h)  
- ⏱ Travel Time (sec)  
- 🚦 Traffic Level  
- 🛣 Road Condition  

### ⚡ Fast Deployment with Joblib

Pretrained models are loaded instantly using **joblib**, avoiding retraining during app startup.

---

## 🖼️ App Screenshot

![Dashboard](assets/Dashboard.png)

---

## 📝 Dashboard Interface Explanation

The **FCC Traffic Prediction System** provides an interactive dashboard where users can input route parameters and instantly predict traffic conditions using trained machine learning models.

### 🎛️ Sidebar Input Panel

The left sidebar allows users to configure traffic prediction variables:

- **Route** – Select a major road corridor  
- **Segment** – Choose a specific road section  
- **Time Period** – AM or PM traffic session  
- **Distance (km)** – Route travel distance  
- **Peak Delay Source** – Main cause of congestion (e.g., market activity, traffic signal, security stop)  
- **Running Speed (km/h)** – Estimated moving speed without delay  
- **Percent Time Delay (%)** – Delay percentage caused by congestion  
- **Level of Service** – Road performance grade (A to F)

These values are used as model inputs for prediction.

### 📄 Data Preview Section

The dashboard confirms successful dataset loading and displays a preview of traffic records.

Example columns include:

- Route  
- Segment  
- Distance_km  
- Mean Peak Travel Time  
- Mean Peak Travel Speed  
- Total Peak Delay  
- Peak Delay Source  

This helps users verify the dataset being used.

### 🔮 Prediction Action

By clicking **Predict Traffic Conditions**, the system runs multiple machine learning models to generate outputs.

### 📊 Expected Prediction Outputs

- 🚗 Predicted Speed (km/h)  
- ⏱ Estimated Travel Time (sec)  
- 🚦 Traffic Level  
- 🛣 Road Condition  

### 📌 Benefits of This Interface

- User-friendly traffic simulation tool  
- Fast route performance estimation  
- Supports congestion analysis  
- Useful for commuters and planners  
- Enables smart transport decisions  

### 🧠 Summary

This dashboard works like an **AI-powered transport control panel**, transforming route inputs into real-time traffic insights for smarter mobility planning.

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- Scikit-learn  
- Joblib  
- Machine Learning Pipelines  

---

## 📂 Project Structure

```bash
FCC-Traffic-AI/
│── assets/
│   └── Dashboard.png
│── FCC_Traffic_300.csv
│── app2.py
│── speed_model.pkl
│── time_model.pkl
│── traffic_model.pkl
│── condition_model.pkl
│── requirements.txt
```
---
⚙️ Installation & Setup
1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/FCC-Traffic-AI.git
cd FCC-Traffic-AI
```
---
2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
---
3️⃣ Run App
```bash
streamlit run app2.py
```
---
## 📌 Use Cases

- Smart Traffic Forecasting  
- Urban Mobility Analytics  
- Public Transport Planning  
- Congestion Monitoring  
- Road Performance Evaluation  
- Smart City Decision Support  

## 📈 Future Improvements

- Real-time Traffic API Integration  
- Interactive GIS Traffic Maps  
- Accident Delay Prediction  
- Route Recommendation Engine  
- Power BI Executive Dashboard  
- Mobile App Version  

## 👨‍💻 Author

**Kolade Olonisakin**  
Data Scientist | Machine Learning Engineer | AI Enthusiast  

## ⭐ Support

If you like this project, kindly **star the repository** and share.
