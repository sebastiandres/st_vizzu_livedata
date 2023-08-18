import streamlit as st
import numpy as np
import time
import psutil
import matplotlib.pyplot as plt

c1, c2 = st.columns(2)
sel = c1.selectbox('Data origin', ['Random', 'CPU usage'])
c2.caption(''); c2.caption('')

if c2.button("Plot live data"):
    plot = st.line_chart()
    i=1
    while True:
        x = i
        if sel == 'Random':
            y = np.random.random_integers(101)
        else:
            y = psutil.cpu_percent()
        plot.add_rows([[y]])
        time.sleep(0.25)
        i += 1
