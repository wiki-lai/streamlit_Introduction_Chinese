
import streamlit as st
import time
import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff
import cv2 as cv
import datetime


st.audio('reze.mp3')
st.video('reze.mkv')
body="import numpy as np"
st.code(body, language='python')

# df=pd.read_csv('test.csv')
# st.dataframe(df)
# st.table(df.iloc[0:5])



arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)


df = pd.DataFrame(
np.random.randn(200, 3),
columns=['a', 'b', 'c'])
df


c = alt.Chart(df).mark_circle().encode(
x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)

df = pd.DataFrame(
np.random.randn(200, 3),
columns=['a', 'b', 'c'])

st.vega_lite_chart(df, {
'mark': {'type': 'circle', 'tooltip': True},
'encoding': {
'x': {'field': 'a', 'type': 'quantitative'},
'y': {'field': 'b', 'type': 'quantitative'},
'size': {'field': 'c', 'type': 'quantitative'},
'color': {'field': 'c', 'type': 'quantitative'},
 },
},use_container_width=True)


x1=np.random.randn(200)+2
x2=np.random.randn(200)
x3=np.random.randn(200)-2

hist = [x1,x2,x3]

# group_labels=["Group1","Group2","Group3"]
# fig = ff.create_distplot(
#     hist,group_labels,bin_size=[.1, .25, .5])
#
# st.plotly_chart(fig,use_container_width=True)

image = cv.imread('image.jpg')
img= cv.cvtColor(image,cv.COLOR_BGR2RGB)
st.image(img)


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


btn = st.button('btn')

st.checkbox("让我猜猜")
st.checkbox("ohhhh")

char = st.radio(
    "你最喜爱的人物",
    ('蕾塞',"玛奇玛","姬野")
)

if char == '蕾塞':
    st.write('俺也一样')

option = st.selectbox(
    '人物投票',
     np.array(['reze','power','guangxi']))

options = st.multiselect(
 'What are your favorite colors',
['Green', 'Yellow', 'Red', 'Blue'],
['Yellow', 'Red'])

st.write('You selected:', options)



red_hair = st.slider('red_hair')

# 随机数据的图表
chart_data = pd.DataFrame(
     np.random.randn(20,3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# 生成在地图上的随机点
# 先生成1000列 0~1 的随机数，
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

values = st.slider("选择一个范围",1,100,(22,33))
st.write('你选择的范围{}'.format(values))

v = st.slider('num',55,66)
st.write('你选择的值{}'.format(v))


color = st.select_slider(
'Select a color of the rainbow',
 options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

number = st.number_input('Insert a number',step=1)
st.write('The current number is ', number)

st.text_area('Text to analyze', '''
 It was the best of times, it was the worst of times, it was
 the age of wisdom, it was the age of foolishness, it was
the epoch of belief, it was the epoch of incredulity, it
was the season of Light, it was the season of Darkness, it
 was the spring of hope, it was the winter of despair, (...)
''')

d = st.date_input(
 "选择你的生日",
 datetime.date(2021, 7, 23))
d

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)

uploaded_file = st.file_uploader("上传单个文件")
uploaded_files = st.file_uploader(
    "上传多个文件",type=['jpg','png'],
    accept_multiple_files=True)

color = st.color_picker('Pick A Color', '#00f900')



# 点击一下，显示表格

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

# 点击一下左边，右边显示信息
left_column, right_column = st.beta_columns(2)

pressed = left_column.button('按我变欧皇')
if pressed:
    right_column.write("好耶")

# 隐藏文本
expander = st.beta_expander("蕾塞")
expander.write("好女人")

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

with st.beta_container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

col1, col2 = st.beta_columns(2)

with col1:
    data = np.random.randn(10, 1)
    col1.line_chart(data,width=1000)

with col2:
    col2.write(data)

with st.spinner('Wait for it...'):
    time.sleep(2)
    st.success('Done!')
    st.balloons()

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')

st.error('This is an error')
st.warning('This is a warning')
st.success('This is a success message!')
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)




# 截断控制流
# st.stop()

# 进度条

'开始处理'
# 添加一个占位符
latest_iteration = st.empty()
# 添加一个进度条
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'搞掂，番屋企吃饭'