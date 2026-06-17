import yfinance as yf
import streamlit as st

ticker = "^STOXX50E"  # Euro Stoxx 50

data = yf.download(ticker, period="5y", interval="1wk")

st.title("Euro Stoxx 50 - évolution hebdomadaire")

st.line_chart(data["Close"])
