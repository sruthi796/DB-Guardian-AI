import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="DB Guardian AI", layout="wide")
st.title("🛡️ Full System Monitor")

placeholder = st.empty()

while True:
    try:
        df = pd.read_csv("db_metrics.csv").tail(50)
        latest = df.iloc[-1]
        
        with placeholder.container():
            # 1. Top Row: Big Numbers
            col1, col2, col3 = st.columns(3)
            col1.metric("CPU", f"{latest['cpu_usage']}%")
            col2.metric("Latency", f"{latest['query_latency']}ms")
            col3.metric("Memory", f"{latest['memory_usage']}%")
            
            # 2. Middle Row: Graphs
            st.subheader("Live System Trends")
            st.line_chart(df.set_index('timestamp')[['cpu_usage', 'memory_usage']])
            
            st.subheader("Query Response Time (Latency)")
            st.area_chart(df.set_index('timestamp')['query_latency'])
            
    except:
        st.info("Synchronizing with data stream...")
    time.sleep(1)