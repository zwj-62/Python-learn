"""Streamlit 环境验证脚本：验证 streamlit + pandas + numpy + altair + openai 全套可用"""
import sys
import platform

import numpy as np
import pandas as pd
import altair as alt
import openai
import streamlit as st

st.set_page_config(page_title="Streamlit 环境验证")

st.title("Streamlit 环境验证通过")

st.write("Python:", platform.python_version(), "|", sys.executable)
st.write("streamlit:", st.__version__)
st.write("numpy:", np.__version__)
st.write("pandas:", pd.__version__)
st.write("altair:", alt.__version__)
st.write("openai:", openai.__version__)

# 数据处理 + 图表渲染验证
df = pd.DataFrame({"x": np.arange(1, 11), "y": np.arange(1, 11) ** 2})
st.dataframe(df)
st.altair_chart(
    alt.Chart(df).mark_line().encode(x="x", y="y").properties(title="y = x^2"),
    use_container_width=True,
)

st.success("全部组件正常：数据计算、表格、图表渲染均成功")
