import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# PAGE CONFIG
st.set_page_config(
    page_title="Marketing Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)


# DATA LOADING
@st.cache_data
def load_data():
    return pd.read_csv("marketing_channels.csv")


# METRIC CALCULATION
@st.cache_data
def calculate_marketing_metrics(df):
    CTR, CPC, CPA, conversion_rate, ROAS = {}, {}, {}, {}, {}

    for c in df['Channel'].unique():
        temp = df[df['Channel'] == c].sum(numeric_only=True)

        CTR[c] = (temp['Clicks'] / temp['Impressions'] * 100).round(2)
        CPC[c] = (temp['Cost'] / temp['Clicks']).round(2)
        CPA[c] = (temp['Cost'] / temp['Conversions']).round(2)
        conversion_rate[c] = (temp['Conversions'] / temp['Clicks'] * 100).round(2)
        ROAS[c] = (temp['Revenue'] / temp['Cost']).round(2)

    return pd.DataFrame({
        "CTR (%)": CTR,
        "Conversion Rate (%)": conversion_rate,
        "CPC ($)": CPC,
        "CPA ($)": CPA,
        "ROAS": ROAS
    })


# LOAD DATA
df = load_data()
marketing_metric = calculate_marketing_metrics(df)

# SIDEBAR
st.sidebar.title("📊 Marketing Analytics")
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Channel Analysis", "Insight & Recommendation"]
)


# HOME
if menu == "Home":
    st.title("📈 Marketing Analytics & Product Strategy Insight")
    st.subheader("Data-driven marketing performance dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Cost", f"${df['Cost'].sum():,.0f}")

    with col2:
        st.metric("Total Revenue", f"${df['Revenue'].sum():,.0f}")

    with col3:
        st.metric(
            "Overall ROAS",
            f"{(df['Revenue'].sum() / df['Cost'].sum()):.2f}"
        )

    st.info(
        "Dashboard ini membandingkan efektivitas dan efisiensi "
        "setiap channel marketing berdasarkan metrik utama."
    )


# CHANNEL ANALYSIS
elif menu == "Channel Analysis":
    st.title("📌 Marketing Channel Performance")

    st.subheader("📊 Marketing Metrics by Channel")
    st.dataframe(
        marketing_metric.style.format("{:.2f}")
    )

    st.subheader("📈 CTR vs Conversion Rate (Grouped Bar)")

    fig, ax = plt.subplots(figsize=(8, 6))

    x = np.arange(len(marketing_metric))
    width = 0.35

    ax.bar(
        x - width/2,
        marketing_metric["CTR (%)"],
        width,
        label="CTR (%)"
    )

    ax.bar(
        x + width/2,
        marketing_metric["Conversion Rate (%)"],
        width,
        label="Conversion Rate (%)"
    )

    ax.set_xticks(x)
    ax.set_xticklabels(marketing_metric.index, rotation=45, ha="right")
    ax.set_ylabel("Percentage")
    ax.set_title("CTR vs Conversion Rate by Channel")
    ax.legend()

    for container in ax.containers:
        ax.bar_label(container, padding=3)

    st.pyplot(fig)


# INSIGHT & RECOMMENDATION
elif menu == "Insight & Recommendation":
    st.title("💡 Insight & Business Recommendation")

    best_ctr = marketing_metric["CTR (%)"].idxmax()
    best_conv = marketing_metric["Conversion Rate (%)"].idxmax()
    best_roas = marketing_metric["ROAS"].idxmax()

    st.markdown("### 🔍 Key Insights")
    st.write(f"""
    - Channel dengan **CTR tertinggi**: **{best_ctr}**
    - Channel dengan **Conversion Rate tertinggi**: **{best_conv}**
    - Channel dengan **ROAS terbaik**: **{best_roas}**
    """)

    st.markdown("### 🎯 Recommendation")
    st.success(
        """
        - Scale channel dengan CTR dan Conversion Rate tinggi  
        - Optimasi landing page untuk channel CTR tinggi tapi conversion rendah  
        - Alokasikan budget lebih besar ke channel dengan ROAS tinggi
        """
    )
