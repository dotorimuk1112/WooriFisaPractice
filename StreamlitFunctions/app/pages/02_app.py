import streamlit as st
import pandas as pd  # st은 입력과 출력만 담당할 뿐 실제 로직은 나머지 파이썬 코드로 구현됩니다.

data = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)


# 입력
st.title('1. 입력버튼들')

button_result = st.button('Hit me')
print(button_result)
if button_result == 1:
    st.write(data)
    st.write(button_result)
else:
    st.write('')
st.data_editor(data)
check_result = st.checkbox('Check me out')
st.write(check_result)
if check_result == 1:
    st.write('TRUE')
else:
    st.write('FALSE')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0.0, max_value=10.0, step = 0.5)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.image('C:\ITStudy\01_python\data\갈비.jpg')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.download_button(
    label="Download data as CSV",
    data='안녕하세요',
    file_name='app_df.csv',
    mime='text/csv'
)
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')

# 출력
st.title('2. 출력메서드들')
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

# 출력
