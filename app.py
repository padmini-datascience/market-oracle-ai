import streamlit as st
import pandas as pd
import os
from signals.entry import generate_entry_signal
from signals.exit import generate_exit_signal
from signals.reversal import detect_reversal
from data.options_chain import get_options_data

from data.fetch_nifty import get_nifty_data
from indicators.atr import calculate_atr
from indicators.adx import calculate_adx
from indicators.supertrend import calculate_supertrend
from models.trade_score import calculate_trade_score
from models.market_sentiment import get_market_sentiment
from signals.suggested_trade import get_suggested_trade
from models.signal_agreement import get_signal_agreement
from models.risk_management import get_risk_management
from models.decision_reason import get_decision_reason
from models.confidence_score import get_confidence_score
from models.trade_readiness import get_trade_readiness
from models.signal_accuracy import get_signal_accuracy
from models.accuracy_rate import get_accuracy_rate
from models.signal_logger import log_signal




st.set_page_config(
    page_title="Market Oracle AI",
    layout="wide"
    
)

st.title("📈 Market Oracle AI")
st.caption("AI Powered Trading Decision Support System")

st.markdown("---")

try:

    # Fetch NIFTY Data
    data = get_nifty_data()
    options_data = get_options_data()
    pcr = options_data["PCR"]
    pcr_status = options_data["PCR_Status"]
    call_oi = options_data["Call_OI"]
    put_oi = options_data["Put_OI"]
    data = calculate_atr(data)
    data = calculate_adx(data)
    data = calculate_supertrend(data)
    entry_result = generate_entry_signal(data)
    exit_result = generate_exit_signal(data)
    reversal_result = detect_reversal(data)
    latest_close = float(data["Close"].iloc[-1])
    latest_atr = float(data["ATR"].iloc[-1])
    latest_adx = float(data["ADX"].iloc[-1])

    accuracy_data = get_accuracy_rate()
    correct_signals = accuracy_data["Correct"]
    wrong_signals = accuracy_data["Wrong"]
    pending_signals = accuracy_data["Pending"]
    accuracy_rate = accuracy_data["Accuracy"]

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
#signal accuracy
    signal_accuracy = get_signal_accuracy(
    signal,
    verdict
    )

#call logger
    if os.path.exists("signal_history.csv"):
        history = pd.read_csv("signal_history.csv")
    else:
        history = pd.DataFrame()
    if len(history) == 0:
        log_signal(
        latest_close,
        signal,
        verdict,
        signal_accuracy)

    elif history.iloc[-1]["Signal"] != signal:
        log_signal(
        latest_close,
        signal,
        verdict,
        signal_accuracy)

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

# market sentiment

    market_sentiment = get_market_sentiment(
    trend_strength,
    pcr_status
    )
#singal agreement

    signal_agreement = get_signal_agreement(
    signal,
    market_sentiment
)
# confidence score
    confidence_score = get_confidence_score(
    trade_score,
    signal_agreement
    )
# trade readiness
    trade_readiness = get_trade_readiness(
    latest_adx,
    signal_agreement,
    confidence_score
    )

#trade_suggestion

    suggested_trade = get_suggested_trade(
    market_sentiment,
    trend_strength,
    signal_agreement
    )

#decision reason
    decision_reasons = get_decision_reason(
    trend_strength,
    signal_agreement,
    confidence,
    suggested_trade
)

# risk management 
    risk = get_risk_management(
    data["Close"].iloc[-1],
    data["ATR"].iloc[-1],
    suggested_trade
    )
    stop_loss = risk["Stop Loss"]

    target = risk["Target"]
    
# market overview

    st.subheader("📈 Market Overview")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("NIFTY", f"{latest_close:.2f}")

    with col2:
        st.metric("ATR", f"{latest_atr:.2f}")

    with col3:
        st.metric("ADX", f"{latest_adx:.2f}")

    with col4:
        st.metric("Trend", trend_strength)

    with col5:
        st.metric("PCR", pcr) 

    if verdict == "BULLISH":
        st.success("🟢 Market Status : BULLISH")

    elif verdict == "BEARISH":
        st.error("🔴 Market Status : BEARISH")

    else:
        st.warning("🟡 Market Status : WAIT")

# trading decision
    st.markdown("---")

    st.subheader("🎯 Trading Decision")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Signal", signal)

    with col2:
        st.metric("Verdict", verdict)

    with col3:
        st.metric("Confidence", confidence)

    with col4:
        st.metric("Suggested Trade", suggested_trade)

# Risk Management

    st.markdown("---")

    st.subheader("🛡️ Risk Management")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Stop Loss", stop_loss)

    with col2:
        st.metric("Target", target)

    with col3:
        st.metric("Trade Readiness", f"{trade_readiness}/100")

# Performance
    st.markdown("---")

    st.subheader("📊 Performance")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Correct", correct_signals)

    with col2:
        st.metric("Wrong", wrong_signals)

    with col3:
        st.metric("Pending", pending_signals)

    with col4:
        st.metric("Accuracy", f"{accuracy_rate}%")

    st.markdown("---")

    st.subheader("Recent NIFTY Data")
    st.write(
    "🕒 Last Candle :",
    data.index[-1].tz_convert("Asia/Kolkata").strftime("%d-%m-%Y %H:%M:%S")
    )
    st.dataframe(data.tail())
    st.markdown("---")

    st.subheader("📒 Trade Journal")
    st.caption("Last 10 Trading Signals")
    try:

        history = pd.read_csv("signal_history.csv")

        if len(history) > 0:

            st.dataframe(
            history.tail(10).iloc[::-1],
            hide_index=True,
            use_container_width=True)

        else:

            st.info("No signal history available.")

    except Exception:

        st.info("No signal history available.")

 #trading statistics
    st.markdown("---")

    st.subheader("📊 Trading Statistics")
    st.write(f"Correct Signals : {correct_signals}")
    st.write(f"Wrong Signals : {wrong_signals}")
    st.write(f"Pending Signals : {pending_signals}")
    st.write(f"Accuracy Rate : {accuracy_rate}%")
    st.write(f"Completed Signals : {correct_signals + wrong_signals}")
    st.markdown("---")
    st.subheader("🎯 Latest Signal")

    if len(history) > 0:

        latest_signal = history.iloc[-1]

        st.write("🕒 Last Market Update :",
        data.index[-1].tz_convert("Asia/Kolkata").strftime("%H:%M:%S"))
        st.write(f"📒 Last Logged Signal : {latest_signal['DateTime']}")
        st.write(f"💰 Price : {latest_signal['Price']:.2f}")
        st.write(f"📈 Signal : {latest_signal['Signal']}")
        st.write(f"🎯 Verdict : {latest_signal['Verdict']}")
        st.write(f"✅ Accuracy : {latest_signal['Accuracy']}")
        st.success(f"Current Market Decision : {latest_signal['Signal']}")

    else:

        st.info("No signal history available.")
        st.write(
        f"Total Signals Logged: {len(history)}"
        )

# signal statistics

    st.markdown("---")

    st.subheader("📊 Signal Statistics")

    st.metric(
    "Total Signals Logged",
    len(history)
    )
    

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

    st.markdown("---")

    st.subheader("🧠 Decision Reason")

    for reason in decision_reasons:
        st.write("•", reason)

    st.markdown("---")
    st.caption(
    "📈 Market Oracle AI v1.0 | AI Powered Trading Dashboard | Developed by Naga Padmini")
except Exception as e:
    st.error(f"Error: {e}")

    