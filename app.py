import streamlit as st
from signals.entry import generate_entry_signal
from signals.exit import generate_exit_signal
from signals.reversal import detect_reversal
from data.options_chain import get_options_data

from data.fetch_nifty import get_nifty_data
from indicators.atr import calculate_atr
from indicators.adx import calculate_adx
from indicators.supertrend import calculate_supertrend
from models.trade_score import calculate_trade_score
st.set_page_config(
    page_title="Market Oracle AI",
    layout="wide"
)

st.title("📈 Market Oracle AI")

st.markdown("---")

try:

    # Fetch NIFTY Data
    data = get_nifty_data()
    options_data = get_options_data()
    pcr = options_data["PCR"]
    pcr_status = options_data["PCR_Status"]
    data = calculate_atr(data)
    data = calculate_adx(data)
    data = calculate_supertrend(data)
    entry_result = generate_entry_signal(data)
    exit_result = generate_exit_signal(data)
    reversal_result = detect_reversal(data)
    latest_close = float(data["Close"].iloc[-1])
    latest_atr = float(data["ATR"].iloc[-1])
    latest_adx = float(data["ADX"].iloc[-1])

    if latest_adx < 20:
        market_status = "SIDEWAYS"

    elif latest_adx < 25:
         market_status = "TRANSITION"

    else:
        market_status = "TRENDING"

    if latest_adx < 20:
        trend_strength = "WEAK"

    elif latest_adx < 30:
        trend_strength = "MODERATE"

    else:
        trend_strength = "STRONG"

    latest_supertrend = data["Supertrend"].iloc[-1]

    

# calculating trade score
    trade_score = calculate_trade_score(
        latest_adx,
         latest_supertrend
        )
    
    if trade_score >= 80:
        confidence = "HIGH"

    elif trade_score >= 50:
        confidence = "MEDIUM"

    else:
        confidence = "LOW"
# Action engine
    if trade_score >= 80:
        action = "ENTER TRADE"

    elif trade_score >= 50:
        action = "WATCH"

    else:
        action = "NO TRADE"

    # Current Price
    latest_close = float(data["Close"].iloc[-1])

    #signal logic
    if latest_supertrend and latest_adx > 25:
        signal = "BUY"

    elif (not latest_supertrend) and latest_adx > 25:
        signal = "SELL"

    else:
        signal = "NO TRADE"


# trade verdict
    if (
        signal == "BUY"
        and confidence != "LOW"
    ):
        verdict = "BULLISH"

    elif (
        signal == "SELL"
        and confidence != "LOW"
    ):
        verdict = "BEARISH"

    else:
        verdict = "WAIT"

#create trade summary logic
    if trend_strength == "WEAK":

        market_summary = """
        Weak trend detected.
        Avoid new trades.
        Wait for stronger setup.
        """

    elif trend_strength == "MODERATE":

        market_summary = """
        Trend is developing.
        Watch market closely.
        Wait for confirmation.
        """

    else:

        market_summary = """
        Strong trend detected.
        Trade opportunities may exist.
        Follow risk management.
        """
# entry decision

    st.subheader("Entry Decision")

    st.write(
    f"Entry Signal: {entry_result['signal']}"
    )

    st.write(
    f"Entry Confidence: {entry_result['confidence']}"
    )

#trade quality score
    if trade_score <= 25:
        entry_quality = "POOR"

    elif trade_score <= 50:
        entry_quality = "FAIR"

    elif trade_score <= 75:
        entry_quality = "GOOD"

    else:
        entry_quality = "EXCELLENT"

    # Dashboard Metrics
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15 = st.columns(15)

    with col1:
        st.metric(
        label="NIFTY Current Price",
        value=f"{latest_close:.2f}"
        )

    with col2:
        st.metric(
        label="ATR",
        value=f"{latest_atr:.2f}"
        )

    with col3:
        st.metric(
        label="ADX",
        value=f"{latest_adx:.2f}"
        )

    with col4:
        st.metric(
        label="Signal",
        value=signal
        )

    with col5:
        st.metric(
        label="Trade Score",
        value=trade_score
        )
    with col6:
        st.metric(
        label="Confidence",
        value=confidence
        )
    with col7:
        st.metric(
        label="Action",
        value=action
        )    
    with col8:
        st.metric(
        label="Market Status",
        value=market_status
        )  
    with col9:
        st.metric(
        label="Exit Signal",
        value=exit_result["signal"]
        ) 
    with col10:
        st.metric(
        label="Reversal",
        value="YES" if reversal_result["reversal"] else "NO"
        ) 
    with col11:
        st.metric(
        label="Verdict",
        value=verdict
        )
    with col12:
        st.metric(
        label="Entry Quality",
        value=entry_quality
        )
    with col13:
        st.metric(
        label="Trend Strength",
        value=trend_strength
        )
    with col14:
        st.metric(
        label="PCR",
        value=pcr
        )
    with col15:
        st.metric(
        label="PCR Status",
        value=pcr_status
        )
    

    st.markdown("---")

    st.subheader("Recent NIFTY Data")

    st.dataframe(data.tail())

except Exception as e:

    st.error(f"Error: {e}")

#trend message
    st.markdown("---")
    if latest_adx < 20:
        st.warning(
        "Weak Trend Detected. Avoid new trades."
        )

    elif latest_adx < 25:
        st.info(
        "Trend is developing. Wait for confirmation."
        )

    else:
        st.success(
        "Strong Trend Detected."
        )

#reversal message
st.markdown("---")

st.subheader("Reversal Analysis")

st.write(reversal_result["message"])

st.markdown("---")

st.subheader("📊 Market Summary")

st.info(market_summary)