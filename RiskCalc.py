import streamlit as st

st.set_page_config(page_title="Position Size Calculator", page_icon="💰")

st.title("💰 Position Size Calculator")

# Inputs
col1, col2 = st.columns(2)
with col1:
    portfolio_capital = st.number_input("💼 Portfolio Capital ($)", min_value=0.0, step=100.0, format="%.2f")
with col2:
    risk_percent = st.number_input("⚠️ Risk %", min_value=0.0, max_value=100.0, step=0.1, format="%.1f")

col3, col4 = st.columns(2)
with col3:
    entry_price = st.number_input("🎯 Entry Price ($)", min_value=0.0, step=1.0, format="%.2f")
with col4:
    stop_loss_price = st.number_input("🛑 Stop Loss Price ($)", min_value=0.0, step=1.0, format="%.2f")

# Calculation
if all(x > 0 for x in [portfolio_capital, risk_percent, entry_price, stop_loss_price]):
    dollar_risk = (risk_percent / 100) * portfolio_capital
    risk_per_share = abs(entry_price - stop_loss_price)

    if risk_per_share > 0:
        shares_to_buy = dollar_risk / risk_per_share
        dollar_loss = shares_to_buy * risk_per_share

        st.markdown("---")
        st.markdown(
            f"""
            <div style="text-align: center; font-size: 36px; color: #4CAF50;">✅ {shares_to_buy:.0f} Shares</div>
            <div style="text-align: center; font-size: 24px; color: #FF5722;">💸 ${dollar_loss:.2f} Risked</div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.warning("❌ Stop loss price must be different from entry price.")
else:
    st.info("ℹ️ Fill in all fields to see results.")

st.markdown("---")
st.caption("Made with ❤️ by your trading assistant.")
