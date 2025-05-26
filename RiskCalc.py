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
    # Calculate the percentage difference between entry and stop loss
    price_risk_percent = abs(entry_price - stop_loss_price) / entry_price * 100
    dollar_risk = (risk_percent / 100) * portfolio_capital
    risk_per_share = abs(entry_price - stop_loss_price)
    
    if risk_per_share > 0:
        # Check if stop loss risk is less than intended portfolio risk
        if price_risk_percent < risk_percent:
            # Stop loss is tighter than intended risk - go all in!
            max_shares = portfolio_capital / entry_price
            position_value = portfolio_capital
            actual_dollar_risk = max_shares * risk_per_share
            actual_risk_percent = (actual_dollar_risk / portfolio_capital) * 100
            
            st.markdown("---")
            st.markdown(
                f"""
                <div style="background-color: #e8f5e8; padding: 15px; border-radius: 10px; margin: 10px 0;">
                    <div style="text-align: center; font-size: 18px; color: #2e7d32; margin-bottom: 10px;">
                        🎯 <strong>TIGHT STOP LOSS DETECTED!</strong>
                    </div>
                    <div style="text-align: center; font-size: 14px; color: #666; margin-bottom: 15px;">
                        Your stop loss risk ({price_risk_percent:.2f}%) is less than your intended risk ({risk_percent:.1f}%)
                        <br><strong>Recommendation: Go ALL IN! 🚀</strong>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            st.markdown(
                f"""
                <div style="text-align: center; font-size: 36px; color: #4CAF50;">
                    ✅ {max_shares:.0f} Shares
                    <div style="font-size: 14px; color: #2e7d32;">(${position_value:,.2f} position size - 100% of portfolio)</div>
                </div>
                <div style="text-align: center; font-size: 24px; color: #FF5722;">
                    💸 ${actual_dollar_risk:.2f} Actually Risked ({actual_risk_percent:.2f}% of portfolio)
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            # Normal calculation - stop loss risk >= intended risk
            shares_to_buy = dollar_risk / risk_per_share
            position_value = shares_to_buy * entry_price
            
            st.markdown("---")
            st.markdown(
                f"""
                <div style="text-align: center; font-size: 36px; color: #4CAF50;">
                    ✅ {shares_to_buy:.0f} Shares
                    <div style="font-size: 14px; color: #666;">(${position_value:,.2f} position size)</div>
                </div>
                <div style="text-align: center; font-size: 24px; color: #FF5722;">
                    💸 ${dollar_risk:.2f} Risked ({risk_percent:.1f}% of portfolio)
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.warning("❌ Stop loss price must be different from entry price.")
else:
    st.info("ℹ️ Fill in all fields to see results.")

st.markdown("---")
st.caption("KK")
