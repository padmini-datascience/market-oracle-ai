import streamlit as st

from data.fetch_nifty import get_nifty_data

st.set_page_config(
    page_title="Market Oracle AI",
    layout="wide"
)

st.title("📈 Market Oracle AI")

st.markdown("---")

# Fetch Data

data = get_nifty_data()

latest_close = float(data['Close'].iloc[-1])

# Dashboard

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="NIFTY Current Price",
        value=f"{latest_close:.2f}"
    )

with col2:
    st.metric(
        label="Trade Score",
        value="--"
    )

with col3:
    st.metric(
        label="Signal",
        value="--"
    )

st.markdown("---")

st.subheader("Recent NIFTY Data")

st.dataframe(
    data.tail()
)
