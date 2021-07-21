
import streamlit as st
import time
import  numpy as np
import pandas as pd


st.title('My first app')
st.write('可以将任何内容传递给write函数，文本、数据、Matplotlib 图形、Altair 图表等，***这很重要***')
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

"""
# My first app
这种注释会自动被 write 函数调用。变量也是。\n

如果你想用write，那你可以不用write。
"""
var = 'CHAINSAW MAN'
var



btn = st.sidebar.button('btn')

option = st.sidebar.selectbox(
    '人物投票',
     np.array(['reze','power','guangxi']))


red_hair = st.sidebar.slider('red_hair')

st.write(red_hair, 'is' ,red_hair)

chart_data = pd.DataFrame(
     np.random.randn(20,3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('按我变欧皇')
if pressed:
    right_column.write("好耶")


expander = st.beta_expander("蕾塞")
expander.write("好女人")

'开始处理'
# 添加一个占位符
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'搞掂，番屋企吃饭'