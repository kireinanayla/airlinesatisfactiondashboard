import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Dashboard Analysis",
    page_icon="📊",
    layout="wide"
)

# ==========================
# LOAD DATA
# ==========================
df = pd.read_csv("test.csv")

# ==========================
# COLOR PALETTE
# ==========================
chart_colors = [
    "#BFDBFE",  # soft blue
    "#60A5FA",  # medium blue
    "#DBEAFE"   # icy blue
]

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
    font-family: 'Poppins';
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
    font-family: 'Poppins';
    background: rgba(255,255,255,0.10);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    margin-bottom: 25px;
}

/* PAGE TITLE */
.page-title {
    font-family: 'Poppins';
    font-size: 40px;
    font-weight: 800;
    color: #0F172A;
}

.page-subtitle {
    font-family: 'Poppins';
    color: #64748B;
    margin-bottom: 30px;
}
/* ==========================
TAB STYLING
========================== */

.stTabs [data-baseweb="tab-list"] {
    font-family: 'Poppins';
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
    background: #CBD5E1;
    color: #0F172A;
}

/* Active tab */
.stTabs [aria-selected="true"] {
    font-family: 'Poppins';
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
    display: none;
}
/* KPI */
.kpi-box {
    font-family: 'Poppins';
    background: linear-gradient(
        135deg,
        #081F5C 0%,
        #2563EB 100%
    );
    padding: 20px;
    border-radius: 18px;
    text-align: justified;
    color: white;
}

/* CHART CARD */
.chart-card {
    font-family: 'Poppins';
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
    font-family: 'Poppins';
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
<div class="page-title">📊 Dashboard Analysis</div>
<div class="page-subtitle">
Explore passenger behavior, customer segmentation, and service quality insights.
</div>
""", unsafe_allow_html=True)

# ==========================
# DARK BLUE CHART LAYOUT
# ==========================
chart_layout = dict(
    paper_bgcolor="#081F5C",
    plot_bgcolor="#081F5C",
    font=dict(
        family="Poppins, poppins",
        color="white",
        size=14
    ),
    title_font=dict(
        family="Poppins, poppins",
        size=20,
        color="white",
    ),
    xaxis=dict(
        gridcolor="rgba(255,255,255,0.08)",
        tickfont=dict(color="white")
    ),
    yaxis=dict(
        gridcolor="rgba(255,255,255,0.08)",
        tickfont=dict(color="white")
    ),
    legend=dict(
        font=dict(color="white")
    )
)

# ==========================
# TABS
# ==========================
tab1, tab2, tab3 = st.tabs([
    "Overview",
    "Customer Demographics",
    "Service Quality Analysis"
])

# ==========================
# TAB 1
# ==========================
with tab1:

    col1, col2, col3, col4 = st.columns(4)

    metrics = [
        ("Total Passenger", len(df)),
        ("Features", df.shape[1]),
        ("Avg Age", round(df["Age"].mean(),1)),
        ("Avg Distance", round(df["Flight Distance"].mean(),1))
    ]

    for col, (label, val) in zip([col1,col2,col3,col4], metrics):
        with col:
            st.markdown(f"""
            <div class="kpi-box">
                <h4>{label}</h4>
                <h2>{val}</h2>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    fig1 = px.pie(
        df,
        names="satisfaction",
        hole=0.65,
        color_discrete_sequence=chart_colors,
        title="Passenger Satisfaction Distribution"
    )
    fig1.update_traces(
    textfont_color="white"
    )
    fig1.update_layout(**chart_layout, title_x=0.05, title_y=0.95, showlegend=True)

    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================
# TAB 2
# ==========================
with tab2:

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)

        fig2 = px.histogram(
            df,
            x="Age",
            color_discrete_sequence=["#60A5FA"],
            title="Passenger Age Distribution"
        )
        fig2.update_layout(**chart_layout, title_x=0.05, title_y=0.95, showlegend=True)

        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)

        fig3 = px.pie(
            df,
            names="Gender",
            hole=0.65,
            color_discrete_sequence=chart_colors,
            title="Passenger Gender Composition"
        )
        fig3.update_layout(**chart_layout, title_x=0.05, title_y=0.95, showlegend=True)

        st.plotly_chart(fig3, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)

        fig4 = px.pie(
            df,
            names="Class",
            hole=0.65,
            color_discrete_sequence=chart_colors,
            title="Flight Class Distribution"
        )
        fig4.update_layout(**chart_layout, title_x=0.05, title_y=0.95, showlegend=True)

        st.plotly_chart(fig4, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)

        fig5 = px.pie(
            df,
            names="Customer Type",
            hole=0.65,
            color_discrete_sequence=chart_colors,
            title= "Customer Type Distribution"
        )
        fig5.update_layout(**chart_layout, title_x=0.05, title_y=0.95, showlegend=True)

        st.plotly_chart(fig5, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================
# TAB 3
# ==========================
with tab3:

    service_cols = [
        "Inflight wifi service",
        "Ease of Online booking",
        "Food and drink",
        "Seat comfort",
        "Inflight entertainment",
        "On-board service",
        "Leg room service",
        "Cleanliness"
    ]

    avg_service = df[service_cols].mean().reset_index()
    avg_service.columns = ["Service", "Rating"]

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    fig6 = px.bar(
        avg_service,
        x="Rating",
        y="Service",
        orientation="h",
        color="Rating",
        color_continuous_scale=[
            "#DBEAFE",
            "#93C5FD",
            "#60A5FA"],
        title="Average Service Ratings"
    )
    fig6.update_layout(**chart_layout, title_x=0.05, title_y=0.95, showlegend=True)

    st.plotly_chart(fig6, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    fig7 = px.box(
        df,
        y=service_cols,
        color_discrete_sequence=["#93C5FD"],
        title= "Service Rating Spread"
    )
    fig7.update_layout(**chart_layout, title_x=0.05, title_y=0.95, showlegend=True)

    st.plotly_chart(fig7, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)