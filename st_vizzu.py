import streamlit as st
import numpy as np
import time
import psutil
#import matplotlib.pyplot as plt
import pandas as pd
from streamlit_vizzu import Config, Data, VizzuChart

c1, c2 = st.columns(2)
sel = c1.selectbox('Data origin', ['Random', 'CPU usage'])
c2.markdown(''); c2.markdown('')

# Initial configuration
if c2.button("Plot live data"):
    # Initial data
    df = pd.DataFrame({
                "time": [1,2],
                "value": [100,0,],
            })
    data = Data()
    data.add_df(df)
    # Add the chart
    chart = VizzuChart()
    chart.animate(data)
    chart.animate(
        Config.line(
            {
                "x": "time",
                "y": "value",
                "title": "Line Chart with Live Data",
                "color": "time",
            }
        )
    )
    data.add_records([[3, 100]])
    chart.animate(data)
    data.add_records([[3, 100]])
    chart.animate(data)
    data.add_records([[3, 100]])
    chart.animate(data)
    # Update
    i=4
    while i<20:
        x = i
        if sel == 'Random':
            y = np.random.random_integers(101)
        else:
            y = psutil.cpu_percent()
        data.add_records([[x, int(y)]])
        chart.animate(data)
        time.sleep(0.25)
        i += 1
    chart.show()

# Some other links
_, c1, c2, c3 = st.columns([1,2,2,2])
c1.caption("[streamlit-vizzu documentation](https://github.com/vizzu-streamlit/streamlit-vizzu/)")
c2.caption("[streamlit documentation](https://docs.streamlit.io/)")
c3.caption("[(ipy)vizzu documentation](https://ipyvizzu.vizzuhq.com/latest/)")
