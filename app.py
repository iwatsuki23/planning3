import streamlit as st
st.title("WizWe Planning Team")

import streamlit as st
import numpy as np

# streamlitのメソッドでmarkdown形式で表示
st.write(
    """
    # 案件状況の可視化
    グラフのイメージ-数種類*
    """
    )

# 適当なデータ作成
data = np.arange(0, 10, 0.1)

# streamlitのメソッドでデータを直線グラフに
st.line_chart(data)

import streamlit as st
import numpy as np
import pandas as pd
st.subheader('案件ごとの進捗率')
chart_data = pd.DataFrame(
     np.random.randn(7, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.dataframe(chart_data)

import streamlit as st
import numpy as np
import pandas as pd
st.subheader('NPSのイメージ')
chart_data = pd.DataFrame(
     np.random.randn(7, 3),
     columns=['a', 'b', 'c'])

st.bar_chart(chart_data)
st.dataframe(chart_data)


import pandas as pd
import matplotlib.pyplot as plt

# Matplotlibの設定を変更

# CSVファイルを読み込む
df = pd.read_csv('word_counts_2.csv', encoding='shift_jis')

df['count'] = df['count'].astype(int)
df['word'] = df['word'].astype(str)

# 出現回数でソートして上位20番目までを取得
top_20 = df.sort_values(by='count', ascending=False).head(20)

# 棒グラフを表示
st.plt.figure(figsize=(15, 8))
st.plt.bar(top_20['word'], top_20['count'])
st.plt.title('単語の出現回数（上位20）')
st.plt.xlabel('単語')
st.plt.ylabel('出現回数')
st.plt.xticks(rotation=45)
st.plt.tight_layout()
st.plt.show()
