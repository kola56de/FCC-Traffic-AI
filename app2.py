import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="FCC Traffic AI", layout="wide")

st.title("🚍 FCC Traffic Prediction System")

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("FCC_Traffic_300.csv")

df = load_data()

st.success(f"Dataset loaded successfully! Shape: {df.shape}")

st.subheader("📄 Data Preview")
st.dataframe(df.head())

# -------------------------------
# Load Models
# -------------------------------
speed_model = joblib.load("speed_model.pkl")
time_model = joblib.load("time_model.pkl")
traffic_model = joblib.load("traffic_model.pkl")
condition_model = joblib.load("condition_model.pkl")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.header("Route Input Parameters")

route = st.sidebar.selectbox(
    "Route",
    sorted(df["Route"].unique())
)

segments = df[df["Route"] == route]["Segment"].unique()

segment = st.sidebar.selectbox(
    "Segment",
    sorted(segments)
)

am_pm = st.sidebar.selectbox(
    "Time Period",
    ["AM", "PM"]
)

distance = st.sidebar.number_input(
    "Distance (km)",
    min_value=0.1,
    max_value=20.0,
    value=2.5
)

delay_source = st.sidebar.selectbox(
    "Peak Delay Source",
    df["Peak_delay_source"].unique()
)

running_speed = st.sidebar.number_input(
    "Running Speed (km/h)",
    min_value=5.0,
    max_value=80.0,
    value=40.0
)

percent_delay = st.sidebar.slider(
    "Percent Time Delay (%)",
    min_value=0,
    max_value=100,
    value=40
)

los = st.sidebar.selectbox(
    "Level of Service",
    sorted(df["Level_of_service"].unique())
)

# -------------------------------
# Create Input DataFrame
# -------------------------------
input_df = pd.DataFrame([{
    "Route": route,
    "Segment": segment,
    "AM_or_PM": am_pm,
    "Distance_km": distance,
    "Peak_delay_source": delay_source,
    "Mean_peak_running_speed_kmh": running_speed,
    "Percent_time_delay": percent_delay,
    "Level_of_service": los
}])

# -------------------------------
# Predictions
# -------------------------------
if st.button("🔮 Predict Traffic Conditions"):

    speed_pred = speed_model.predict(input_df)[0]
    time_pred = time_model.predict(input_df)[0]
    traffic_pred = traffic_model.predict(input_df)[0]
    condition_pred = condition_model.predict(input_df)[0]

    st.subheader("📊 Prediction Results")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🚗 Predicted Speed (km/h)", f"{speed_pred:.2f}")
    col2.metric("⏱️ Travel Time (sec)", f"{time_pred:.0f}")
    col3.metric("🚦 Traffic Level", traffic_pred)
    col4.metric("🛣️ Road Condition", condition_pred)
