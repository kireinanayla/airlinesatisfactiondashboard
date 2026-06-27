import streamlit as st
import pandas as pd
import joblib

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Prediction",
    page_icon="🔮",
    layout="wide"
)

# ==========================
# LOAD MODEL
# ==========================
model = joblib.load("model_xgboost.pkl")

# ==========================
# GLOBAL CSS
# ==========================
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>

html, body, [class*="css"] {
    font-family: 'Poppins', poppins;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    font-family: 'Poppins', poppins;
    background:
    linear-gradient(
        180deg,
        #081F5C 0%,
        #0F52BA 45%,
        #2563EB 100%
    );
    padding-top: 20px;
}

[data-testid="stSidebar"] * {
    color: white;
}
.sidebar-logo {
    font-family: 'Poppins', poppins;
    background: rgba(255,255,255,0.10);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    margin-bottom: 25px;
}

/* PAGE TITLE */
.page-title {
    font-family: 'Poppins', poppins;
    font-size: 40px;
    font-weight: 800;
    color: #0F172A;
}

.page-subtitle {
    font-family: 'Poppins', poppins;
    color: #64748B;
    margin-bottom: 30px;
}

/* INPUT CARD */
.input-card {
    font-family: 'Poppins', poppins;
    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #F8FAFC 100%
    );
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

/* SECTION TITLE */
.section-title {
    font-family: 'Poppins', poppins;
    font-size: 22px;
    font-weight: 800;
    color: #1E3A8A;
    margin-bottom: 15px;
}

/* RESULT CARD */
.result-card {
    font-family: 'Poppins', poppins;
    background: linear-gradient(
        135deg,
        #081F5C 0%,
        #2563EB 100%
    );
    padding: 25px;
    border-radius: 22px;
    color: white;
    text-align: center;
    box-shadow: 0px 10px 30px rgba(37,99,235,0.20);
}

/* BUTTON */
.stButton > button {
    font-family: 'Poppins', poppins;
    width: 100%;
    background: linear-gradient(
        90deg,
        #1D4ED8 0%,
        #60A5FA 100%
    );
    color: white;
    border: none;
    border-radius: 14px;
    padding: 12px;
    font-weight: 700;
    font-size: 15px;
}
/* FORM CONTAINER */
.form-card {
    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #F8FAFC 100%
    );
    padding: 28px;
    border-radius: 24px;
    box-shadow: 0px 12px 35px rgba(15,23,42,0.08);
    margin-bottom: 25px;
    border: 1px solid #E2E8F0;
}

/* INPUT LABEL */
label {
    font-weight: 600 !important;
    color: #1E293B !important;
}

/* SELECTBOX */
div[data-baseweb="select"] > div {
    border-radius: 14px !important;
    border: 1px solid #CBD5E1 !important;
    background: white !important;
}

/* NUMBER INPUT */
div[data-baseweb="input"] > div {
    border-radius: 14px !important;
    border: 1px solid #CBD5E1 !important;
    background: white !important;
}

/* SLIDER */
.stSlider > div[data-baseweb="slider"] {
    padding-top: 10px;
}

/* SLIDER TRACK */
.stSlider [role="slider"] {
    background: #2563EB !important;
    border: 3px solid white !important;
}

/* INFO CARD */
.info-card {
    background: linear-gradient(
        135deg,
        #DBEAFE 0%,
        #EFF6FF 100%
    );
    border-left: 5px solid #2563EB;
    padding: 18px;
    border-radius: 16px;
    margin-bottom: 20px;
}

/* RESULT ANIMATION */
.result-card {
    animation: fadeIn 0.5s ease-in-out;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
/* ==========================
DROPDOWN / SELECTBOX
========================== */
div[data-baseweb="select"] > div {
    background: linear-gradient(
        135deg,
        #EFF6FF 0%,
        #DBEAFE 100%
    ) !important;
    border: 2px solid #93C5FD !important;
    border-radius: 14px !important;
    min-height: 50px;
    transition: 0.3s ease;
}

div[data-baseweb="select"] > div:hover {
    border: 2px solid #2563EB !important;
    box-shadow: 0px 0px 12px rgba(37,99,235,0.25);
}

/* Selected text */
div[data-baseweb="select"] span {
    color: #081F5C !important;
    font-weight: 600;
}

/* ==========================
NUMBER INPUT
========================== */
div[data-baseweb="input"] {
    background: linear-gradient(
        135deg,
        #EFF6FF 0%,
        #DBEAFE 100%
    ) !important;
    border-radius: 14px !important;
    border: 2px solid #93C5FD !important;
}

div[data-baseweb="input"]:hover {
    border: 2px solid #2563EB !important;
}

/* ==========================
SLIDER CONTAINER
========================== */
.stSlider {
    background: linear-gradient(
        135deg,
        #EFF6FF 0%,
        #F8FAFC 100%
    );
    padding: 15px;
    border-radius: 16px;
    margin-bottom: 12px;
    border: 1px solid #DBEAFE;
}

/* Slider track */
.stSlider [data-baseweb="slider"] > div > div {
    background: #93C5FD !important;
}

/* Active track */
.stSlider [role="slider"] {
    background: #2563EB !important;
    border: 3px solid white !important;
    width: 20px !important;
    height: 20px !important;
    box-shadow: 0px 0px 12px rgba(37,99,235,0.4);
}

/* ==========================
LABELS
========================== */
label {
    font-size: 15px !important;
    font-weight: 700 !important;
    color: #1E3A8A !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================
st.sidebar.markdown("""
<div class="sidebar-logo">
    <h2>✈ AirInsight</h2>
    <p>Passenger Analytics System</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

st.sidebar.subheader("Navigation")

st.sidebar.info(
    "Explore analytical insights, compare machine learning models, and simulate passenger satisfaction predictions."
)


# ==========================
# HEADER
# ==========================
st.markdown("""
<div class="page-title">🔮 Passenger Satisfaction Prediction</div>
<div class="page-subtitle">
Simulate passenger scenarios and predict airline satisfaction in real-time.
</div>
""", unsafe_allow_html=True)

# ==========================
# INPUT FORM
# ==========================
st.markdown('<div class="section-title">Passenger Information</div>', unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
Fill in passenger profile and service ratings to simulate airline satisfaction prediction.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="form-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    customer_type = st.selectbox("Customer Type", ["Loyal Customer", "Disloyal Customer"])
    age = st.number_input("Age", 1, 100)
    travel_type = st.selectbox("Type of Travel", ["Business Travel", "Personal Travel"])
    flight_class = st.selectbox("Class", ["Business", "Eco", "Eco Plus"])
    flight_distance = st.number_input("Flight Distance", 0)

with col2:
    wifi = st.slider("Inflight wifi service", 0, 5)
    seat_comfort = st.slider("Seat comfort", 0, 5)
    cleanliness = st.slider("Cleanliness", 0, 5)
    online_booking = st.slider("Ease of Online booking", 0, 5)
    entertainment = st.slider("Inflight entertainment", 0, 5)
    onboard_service = st.slider("On-board service", 0, 5)

st.markdown('</div>', unsafe_allow_html=True)
# ==========================
# ENCODING MAPPING
# ==========================
gender_map = {
    "Male": 1,
    "Female": 0
}

customer_type_map = {
    "Loyal Customer": 1,
    "Disloyal Customer": 0
}

travel_type_map = {
    "Business Travel": 1,
    "Personal Travel": 0
}

class_map = {
    "Business": 0,
    "Eco": 1,
    "Eco Plus": 2
}

# fixed filler values for remaining features
input_data = pd.DataFrame({
    "Gender": [gender_map[gender]],
    "Customer Type": [customer_type_map[customer_type]],
    "Age": [age],
    "Type of Travel": [travel_type_map[travel_type]],
    "Class": [class_map[flight_class]],
    "Flight Distance": [flight_distance],
    "Inflight wifi service": [wifi],
    "Departure/Arrival time convenient": [3],
    "Ease of Online booking": [online_booking],
    "Gate location": [3],
    "Food and drink": [3],
    "Online boarding": [3],
    "Seat comfort": [seat_comfort],
    "Inflight entertainment": [entertainment],
    "On-board service": [onboard_service],
    "Leg room service": [3],
    "Baggage handling": [3],
    "Checkin service": [3],
    "Inflight service": [3],
    "Cleanliness": [cleanliness],
    "Departure Delay in Minutes": [0],
    "Arrival Delay in Minutes": [0]
})

st.markdown("""
<div class="info-card">
<h4>Passenger Summary</h4>
<ul>
<li><b>Gender:</b> {}</li>
<li><b>Customer Type:</b> {}</li>
<li><b>Travel Type:</b> {}</li>
<li><b>Class:</b> {}</li>
<li><b>Age:</b> {}</li>
<li><b>Flight Distance:</b> {} km</li>
</ul>
</div>
""".format(
    gender,
    customer_type,
    travel_type,
    flight_class,
    age,
    flight_distance
), unsafe_allow_html=True)

# ==========================
# PREDICT BUTTON
# ==========================
if st.button("Predict Satisfaction"):

    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)

    confidence = max(proba[0])

    st.markdown('<div class="section-title">Prediction Result</div>', unsafe_allow_html=True)

    if prediction[0] == 1:
        st.markdown(f"""
        <div class="result-card">
            <h2>✅ Passenger Satisfied</h2>
            <p>Confidence Score: {confidence*100:.2f}%</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-card">
            <h2>⚠ Passenger Dissatisfied</h2>
            <p>Confidence Score: {confidence*100:.2f}%</p>
        </div>
        """, unsafe_allow_html=True)

    st.progress(float(confidence))