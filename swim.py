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

# Streamlit 应用
st.title('游泳运动员TOP60')

tabm, tabw = st.tabs(["男子游泳世界冠军TOP60", "男子游泳世界冠军TOP60"])
with tabm:
    st.subheader("男子游泳单项世界冠军TOP60")
    swim_men.insert(0, 'Index', range(1, len(df) + 1))
    st.dataframe(swim_men[["名字", '国家','出生年份','世界冠军','奥运会','世锦赛','夺冠周期']])

with tabw:
    st.subheader("女子游泳单项世界冠军TOP60")
    swim_women.insert(0, 'Index', range(1, len(df) + 1))
    st.dataframe(swim_women[["名字", '国家','出生年份','世界冠军','奥运会','世锦赛','夺冠周期']])

mean_age, std_age = calculate_normal_dist_params(swim_men['首冠年龄'])
histogram_men = create_histogram(swim_men['首冠年龄'], '男子游泳运动员首次世界冠军年纪')
normal_dist_curve_men = create_normal_dist_curve(swim_men['首冠年龄'], mean_age, std_age)

mean_age, std_age = calculate_normal_dist_params(swim_women['首冠年龄'])
histogram_women = create_histogram(swim_women['首冠年龄'], '女子游泳运动员首次世界冠军年纪')
normal_dist_curve_women = create_normal_dist_curve(swim_women['首冠年龄'], mean_age, std_age)

col1, col2 = st.columns(2)

with col1:
    st.subheader("男子游泳运动员夺冠周期")
    tabm1, tabm2, tabm3 = st.tabs(["首冠年龄分布柱状图", "夺冠周期分布","男子TOP60夺冠周期表"])
    
    # 在第一个标签页中显示直方图
    with tabm1:
        st.plotly_chart(create_histogram(swim_data['首冠年龄'], '男子游泳世界冠军首冠年龄'))
    
    # 在第二个标签页中显示正态分布曲线
    with tabm2:
        st.plotly_chart(create_normal_dist_curve(swim_data['夺冠期'], mean_age, std_age))
    
    # 在第三个标签页中显示组合图
    with tabm3:
        st.dataframe(swim_men[["名字", '国家','出生年份','首冠年龄','首冠年份','末冠年份','夺冠期']])


st.plotly_chart(histogram_women)
st.plotly_chart(normal_dist_curve_women)
st.plotly_chart(create_combined_plot(histogram_women, normal_dist_curve_women))
