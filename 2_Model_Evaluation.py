import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Model Evaluation",
    page_icon="📉",
    layout="wide"
)

# ==========================
# LOAD DATA
# ==========================
metrics = joblib.load("metrics.pkl")
model = joblib.load("model_xgboost.pkl")

# ==========================
# GLOBAL CSS
# ==========================
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">

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

/* ==========================
TAB STYLING
========================== */

.stTabs [data-baseweb="tab-list"] {
    font-family: 'Poppins', poppins;
    border-radius: 18px;
    font-size: 15px;
    gap: 12px;
    background: transparent;
    margin-bottom: 25px;
}

.stTabs [data-baseweb="tab"] {
    background: #E2E8F0;
    color: #475569;
    border-radius: 18px;
    padding: 14px 28px;
    font-family: 'Poppins', poppins;
    font-weight: 700;
    font-size: 15px;
    border: none;
    transition: all 0.3s ease;
}

/* Hover */
.stTabs [data-baseweb="tab"]:hover {
    font-family: 'Poppins', poppins;
    background: #CBD5E1;
    color: #0F172A;
}

/* Active tab */
.stTabs [aria-selected="true"] {
    font-family: 'Poppins', poppins;
    background: linear-gradient(
        135deg,
        #081F5C 0%,
        #123C9C 100%
    ) !important;
    color: white !important;
    box-shadow: 0px 8px 20px rgba(8,31,92,0.25);
}

/* Hilangkan garis bawah bawaan */
.stTabs [data-baseweb="tab-border"] {
    font-family: 'Poppins', poppins;
    display: none;
}

/* KPI CARD */
.kpi-box {
    font-family: 'Poppins', poppins;
    background: linear-gradient(
        135deg,
        #081F5C 0%,
        #2563EB 100%
    );
    padding: 20px;
    border-radius: 18px;
    text-align: justified;
    color: white;
    box-shadow: 0px 8px 25px rgba(37,99,235,0.18);
}

/* TABLE CARD */
table {
    font-family: 'Poppins', poppins;
    text-align: center;
    width: 100%;
    border-collapse: collapse;
    background: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
    text-size: 8px;
}

thead th {
    font-family: 'Poppins', poppins;
    background: linear-gradient(
        135deg,
        #081F5C 0%,
        #123C9C 100%
    );
    color: white !important;
    padding: 14px;
    text-align: center;
    test-size: 8px;
}

tbody td {
    font-family: 'Poppins', poppins;
    padding: 12px;
    text-align: center;
    test-size: 8px;
}

tbody tr:nth-child(even) {
    font-family: 'Poppins', poppins;
    background: #EFF6FF;
    text-align: center;
    test-size: 8px;
}

tbody tr:hover {
    font-family: 'Poppins', poppins;
    background: #DBEAFE;
    text-align: center;
    test-size: 8px;
}

/* STRIPED ROW */
.table-card tbody tr:nth-child(even) td {
    font-family: 'Poppins', poppins;
    background: #EFF6FF;
}

/* HOVER */
.table-card tbody tr:hover td {
    font-family: 'Poppins', poppins;
    background: #DBEAFE;
    transition: 0.3s;
}

/* CHART CARD */
.chart-card {
    font-family: 'Poppins', poppins;
    background: linear-gradient(
        135deg,
        #081F5C 0%,
        #123C9C 100%
    );
    padding: 20px;
    border-radius: 22px;
    margin-bottom: 20px;
    box-shadow: 0px 10px 30px rgba(8,31,92,0.25);
}

/* INSIGHT CARD */
.insight-card {
    font-family: 'Poppins', poppins;
    background: linear-gradient(
        135deg,
        #DBEAFE 0%,
        #EFF6FF 100%
    );
    border-left: 5px solid #2563EB;
    padding: 20px;
    border-radius: 16px;
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
<div class="page-title">📉 Model Evaluation & Insights</div>
<div class="page-subtitle">
Compare machine learning performance and analyze the most influential factors in predicting passenger satisfaction.
</div>
""", unsafe_allow_html=True)

# ==========================
# CHART LAYOUT
# ==========================
chart_layout = dict(
    paper_bgcolor="#081F5C",
    plot_bgcolor="#081F5C",
    font=dict(
        family="Poppins",
        color="white",
        size=10
    ),
    title_font=dict(
        family="Poppins",
        size=14,
        color="white",
    ),
    xaxis_title_font=dict(
        family="Poppins",
        size=10,
        color="white"
    ),
    yaxis_title_font=dict(
        family="Poppins",
        size=10,
        color="white"
    ),
    xaxis=dict(
        gridcolor="rgba(255,255,255,0.08)",
        tickfont=dict(color="white", family="Poppins", size=10)
    ),
    yaxis=dict(
        gridcolor="rgba(255,255,255,0.08)",
        tickfont=dict(color="white", family="Poppins", size=10)
    ),
    legend=dict(
        font=dict(color="white", family="Poppins", size=10)
    )
)
# ==========================
# TABS
# ==========================
tab1, tab2 = st.tabs([
    "📊 Model Performance",
    "🧠 Feature Importance"
])

# ==========================
# TAB 1
# ==========================
with tab1:

    # ==========================
    # MODEL COMPARISON TABLE
    # ==========================
    st.subheader("Model Comparison Table")

    styled_metrics = metrics.style.format({
        "Accuracy": "{:.2%}",
        "Precision": "{:.2%}",
        "Recall": "{:.2%}",
        "F1 Score": "{:.2%}"
    })

    st.markdown(
    styled_metrics.to_html(),
    unsafe_allow_html=True
    )
    # ==========================
    # PERFORMANCE CHARTS
    # ==========================
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)

        fig1 = px.bar(
            metrics,
            x="Model",
            y="Accuracy",
            color="Accuracy",
            title="Model Accuracy Comparison",
            color_continuous_scale=[
                "#DBEAFE",
                "#93C5FD",
                "#60A5FA"
            ]
        )

        fig1.update_layout(**chart_layout, title_x=0.5)

        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        metrics["Error Rate"] = 1 - metrics["Accuracy"]

        st.markdown('<div class="chart-card">', unsafe_allow_html=True)

        fig2 = px.bar(
            metrics,
            x="Model",
            y="Error Rate",
            color="Error Rate",
            title="Model Error Rate Comparison",
            color_continuous_scale=[
                "#BFDBFE",
                "#93C5FD",
                "#60A5FA"
            ]
        )

        fig2.update_layout(**chart_layout, title_x=0.5)

        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    # ==========================
    # BEST MODEL
    # ==========================
    best_model = metrics.sort_values(
        by="Accuracy",
        ascending=False
    ).iloc[0]
    # BEST MODEL TEXT
    st.markdown(f"""
    <div class="insight-card">
        <h4>🏆 Best Model Selected</h4>
        <p>
          Based on performance evaluation, the best model is
          <b>{best_model['Model']}</b>
          with an accuracy of
          <b>{best_model['Accuracy']:.2%}</b>.
        </p>
      </div>
      """, unsafe_allow_html=True)
    st.markdown("### Best Model Performance")

    col1, col2, col3, col4 = st.columns(4)

    kpis = [
        ("Accuracy", f"{best_model['Accuracy']:.2%}"),
        ("Precision", f"{best_model['Precision']:.2%}"),
        ("Recall", f"{best_model['Recall']:.2%}"),
        ("F1 Score", f"{best_model['F1 Score']:.2%}")
    ]

    for col, (label, val) in zip([col1, col2, col3, col4], kpis):
        with col:
            st.markdown(f"""
            <div class="kpi-box">
                <h4>{label}</h4>
                <h2>{val}</h2>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
# ==========================
# TAB 2
# ==========================
with tab2:

    # ==========================
    # FEATURE IMPORTANCE
    # ==========================
    st.subheader("Feature Importance")

    importance = model.feature_importances_

    features = [
      "Gender",
      "Customer Type",
      "Age",
      "Type of Travel",
      "Class",
      "Flight Distance",
      "Inflight wifi service",
      "Departure/Arrival time convenient",
      "Ease of Online booking",
      "Gate location",
      "Food and drink",
      "Online boarding",
      "Seat comfort",
      "Inflight entertainment",
      "On-board service",
      "Leg room service",
      "Baggage handling",
      "Checkin service",
      "Inflight service",
      "Cleanliness",
      "Departure Delay in Minutes",
      "Arrival Delay in Minutes"
    ]

    df_imp = pd.DataFrame({
        "Feature": features,
        "Importance": importance
    }).sort_values(
        by="Importance",
        ascending=False
    )

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    fig3 = px.bar(
        df_imp.head(10),
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance",
        title="Top 10 Most Important Features",
        color_continuous_scale=[
            "#DBEAFE",
            "#93C5FD",
            "#60A5FA"
        ]
    )

    fig3.update_layout(**chart_layout, title_x=0.5)

    st.plotly_chart(fig3, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ==========================
    # FULL FEATURE TABLE
    # ==========================
    st.subheader("All Feature Importance")

    styled_imp = df_imp.style.background_gradient(
        subset=["Importance"],
        cmap="Blues"
    )

    st.markdown(
    styled_imp.to_html(),
    unsafe_allow_html=True
    )

    # ==========================
    # INSIGHT
    # ==========================
    st.markdown("""
    <div class="insight-card">
    <h4>Insight</h4>
    <p>
    Feature importance analysis helps identify which variables contribute the most to passenger satisfaction predictions.
    This can support strategic service improvements and customer experience optimization.
    </p>
    </div>
    """, unsafe_allow_html=True)