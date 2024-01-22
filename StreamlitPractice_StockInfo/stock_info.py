import streamlit as st
import pandas as pd
import FinanceDataReader as fdr
import datetime
import matplotlib.pyplot as plt
import matplotlib 
from io import BytesIO
import plotly.graph_objects as go
import pandas as pd
import yfinance as yf
import streamlit as st
import datetime
import plotly.io as pio # Plotly input output
import plotly.express as px # 빠르게 그리는 방법
import plotly.graph_objects as go # 디테일한 설정
import plotly.figure_factory as ff # 템플릿 불러오기
from plotly.subplots import make_subplots # subplot 만들기
from plotly.validators.scatter.marker import SymbolValidator # Symbol 꾸미기에 사용됨
from io import BytesIO

def get_stock_info():  # 주식 정보 불러오기 함수
    base_url = "http://kind.krx.co.kr/corpgeneral/corpList.do"
    method = "download"
    url = "{0}?method={1}".format(base_url, method)
    df = pd.read_html(url, header=0, encoding='cp949')[0]
    df['종목코드'] = df['종목코드'].apply(lambda x: f"{x:06d}")
    df = df[['회사명', '종목코드']]
    return df

def get_ticker_symbol(company_name):  # df화 함수
    df = get_stock_info()
    code = df[df['회사명'] == company_name]['종목코드'].values
    ticker_symbol = code[0]
    return ticker_symbol

st.title('무슨 주식을 사야 부자가 될까?')

# Use widgets' returned values in variables
st.sidebar.title('사이드바')
stock_name = st.sidebar.text_input("종목 이름 입력", "삼성전자")
if stock_name:
    start_date, end_date = st.sidebar.date_input(
        "조회 기간 선택",
        value=[
            datetime.date.today() - datetime.timedelta(days=365),
            datetime.date.today()
        ],  # 기본 기간
        key="date_range"
    )

    ticker_symbol = get_ticker_symbol(stock_name)
    df = fdr.DataReader(ticker_symbol, start_date, end_date, exchange="KRX")
    df.index = df.index.date
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Date'}, inplace=True)
    graph = px.line(df, x='Date', y='Close', range_x=[start_date, end_date])
    csv_data = df.to_csv(index=False).encode('utf-8')
    excel_data = BytesIO()

    if st.sidebar.button('주가 확인하기'):
        st.subheader(f"[{stock_name}] 주가 데이터")
        st.dataframe(df.head())
        st.write(graph)

        # 좌측에 'CSV 형식으로 다운로드' 버튼 배치
        left_col, right_col = st.columns(2)

        with left_col:
            if st.button('CSV 형식으로 다운로드'):
                st.download_button(
                    label='',
                    data=csv_data,
                    file_name=f'{stock_name} {start_date}~{end_date} 주가 데이터.csv',
                    key='download_button_csv'
                )

        # 우측에 'Excel 형식으로 다운로드' 버튼 배치
        with right_col:
            st.download_button(
                label='Excel 형식으로 다운로드',
                data=excel_data.read(),
                file_name=f'{stock_name} {start_date}~{end_date} 주가 데이터.xlsx',
                key='download_button_excel'
            )

else:
    st.sidebar.write('확인하고자 하는 종목 이름을 입력하세요.')