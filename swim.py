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
    fig = px.histogram(data, x=data, nbins=30, title=f'Histogram for {name}')
    fig.update_layout(bargap=0.3, bargroupgap=0.2)
    return fig

# 计算正态分布曲线
def create_normal_dist_curve(data, mean, std):
    x = np.linspace(min(data), max(data), 100)
    y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines', name='Normal Dist Curve')])
    fig.update_layout(title='Normal Distribution Curve')
    return fig

# 绘制组合图
def create_combined_plot(histogram, normal_dist_curve):
    combined_fig = go.Figure()
    for data in histogram.data + normal_dist_curve.data:
        combined_fig.add_trace(data)
    combined_fig.update_layout(title_text="Histogram and Normal Distribution Curve")
    return combined_fig

# Streamlit 应用
st.title('First Championship Age Analysis')

mean_age, std_age = calculate_normal_dist_params(swim_men['首冠年龄'])
histogram_men = create_histogram(swim_men['首冠年龄'], '男子游泳运动员首次世界冠军年纪')
normal_dist_curve_men = create_normal_dist_curve(swim_men['首冠年龄'], mean_age, std_age)

# 显示图表
st.plotly_chart(create_combined_plot(histogram_men, normal_dist_curve_men))

mean_age, std_age = calculate_normal_dist_params(swim_women['首冠年龄'])
histogram_women = create_histogram(swim_women['首冠年龄'], '男子游泳运动员首次世界冠军年纪')
normal_dist_curve_women = create_normal_dist_curve(swim_women['首冠年龄'], mean_age, std_age)

# 显示图表
st.plotly_chart(create_combined_plot(histogram_women, normal_dist_curve_men))




st.plotly_chart(histogram_women)
st.plotly_chart(normal_dist_curve_women)
st.plotly_chart(create_combined_plot(histogram_women, normal_dist_curve_women))
