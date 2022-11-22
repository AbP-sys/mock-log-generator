import streamlit as st 
import numpy as np
import pandas as pd 
import time 
import plotly.express as px 


st.set_page_config(
    page_title = 'Real-Time Log Analysis Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Log Analysis Dashboard")

# creating a single-element container.
placeholder = st.empty()
colnames = ['dd','mmm','yy','Timestamp','CPUp','CPU','MemP','Memory']
# dataframe filter 

while True: 
    # creating KPIs 
    df = pd.read_csv("cpulogs.txt",delimiter=" ",names=colnames)
    st.write(df.head())
    
    avg_cpu = np.mean((df['CPU']))  
    avg_mem = np.mean(df['Memory'])

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs 
        kpi1.metric(label="CPU ⏳", value=round(avg_cpu), delta= round(avg_cpu) - 10)
        kpi3.metric(label="Mem ＄", value= round(avg_mem),delta = round(avg_cpu) - 10)

        # create two columns for charts 

        fig_col1, fig_col2, fig_col3 = st.columns(3)
        with fig_col1:
            st.markdown("### Summary")
            st.dataframe(df)
        with fig_col2:
            st.markdown("### CPU Usage")
            fig2 = px.line(df, x = 'Timestamp',y="CPU")
            fig2.update_layout(yaxis_range=[0,100])
            st.write(fig2)
        with fig_col3:
            st.markdown("### Memory Usage")
            fig3 = px.line(df, x = 'Timestamp',y="Memory")
            fig3.update_layout(yaxis_range=[0,100])
            st.write(fig3) 
        st.markdown("### Detailed Data View")
        
        time.sleep(1)