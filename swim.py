import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import seaborn as sns


# 读取数据
swim_men = pd.read_excel('swim.xlsx', sheet_name='Sheet1')
swim_women = pd.read_excel('swim.xlsx', sheet_name='Sheet2')

# 计算正态分布参数
def calculate_normal_dist_params(data):
    mean = np.mean(data)
    std = np.std(data)
    return mean, std

# 创建直方图
def create_histogram(data, name):
    fig = px.histogram(data, x=data, nbins=30, title=f'{name}')
    fig.update_layout(bargap=0.3, bargroupgap=0.2)
    fig.update_xaxes(title_text='首冠年龄')
    fig.update_yaxes(title_text='数量')
    return fig

# 计算正态分布曲线
def create_normal_dist_curve(data, mean, std):
    x = np.linspace(min(data), max(data), 100)
    y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines', name='Normal Dist Curve')])
    fig.update_layout(title='夺冠周期正态分布图')
    return fig

# Streamlit 应用
st.title('游泳运动员TOP60')

tabm, tabw = st.tabs(["男子游泳世界冠军TOP60", "女子游泳世界冠军TOP60"])
with tabm:
    st.subheader("男子游泳单项世界冠军TOP60")
    swim_men.insert(0, 'Index', range(1, len(swim_men) + 1))
    st.dataframe(swim_men)

with tabw:
    st.subheader("女子游泳单项世界冠军TOP60")
    swim_women.insert(0, 'Index', range(1, len(swim_women) + 1))
    st.dataframe(swim_women)

men_mean_age, men_std_age = calculate_normal_dist_params(swim_men['夺冠期'])
histogram_men = create_histogram(swim_men['首冠年龄'], '男子首冠年龄分布图')
normal_dist_curve_men = create_normal_dist_curve(swim_men['夺冠期'], men_mean_age, men_std_age)

mean_age, std_age = calculate_normal_dist_params(swim_women['夺冠期'])
histogram_women = create_histogram(swim_women['首冠年龄'], '女子首冠年龄分布图')
normal_dist_curve_women = create_normal_dist_curve(swim_women['夺冠期'], mean_age, std_age)

st.subheader("游泳运动员夺冠周期长度")
tabm1, tabw1 = st.tabs(["男子夺冠周期", "女子夺冠周期"])

# 在第一个标签页中显示直方图
with tabm1:
    st.plotly_chart(histogram_men)
    st.plotly_chart(normal_dist_curve_men)

with tabw1:
    st.plotly_chart(histogram_women)
    st.plotly_chart(normal_dist_curve_women)
