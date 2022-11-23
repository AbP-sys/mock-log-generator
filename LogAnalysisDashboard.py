import streamlit as st 
import numpy as np
import pandas as pd 
import time 
import plotly.express as px 
import scaling_predictor
import black_listing
import generic_error_predictor

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
    df1 = black_listing.finaldata()
    df = pd.read_csv("cpulogs.txt",delimiter=" ",names=colnames)
    df['Timestamp'] = df['dd'].astype(str)+"-"+df['mmm']+"-"+df['yy'].astype(str)+" "+df['Timestamp'] 
    df = df.drop(["dd","mmm","yy","CPUp","MemP"],axis = 1)
    df = scaling_predictor.modify(df)
    df = scaling_predictor.create_indicators(df)
    time_grad = scaling_predictor.calculate(df)
    scaling_predictor.plot_data(df,time_grad)

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
        fig = scaling_predictor.plot_data(df,time_grad)
        st.pyplot(fig)

        col1, col2 = st.columns(2)
        with col1:
            black_list = black_listing.function1_authentication()
            st.dataframe(black_list)
        with col2:
            error_p = generic_error_predictor.function2_Error()
            st.dataframe(error_p)
        time.sleep(1)