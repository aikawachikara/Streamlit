import streamlit as st

# 背景を白に設定
st.markdown("""
    <style>
    body {
        background-color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("----")
st.title("title")
st.write("write")
st.markdown("# Head1")
st.markdown("## Head2")
st.markdown("----")

check = st.checkbox("他のウィジェットを表示する")  # 引数に入れることでboolを返す

if check:
   st.button("ボタン")  # 引数に入れるとboolで返す
   st.selectbox("メニューリスト", ("選択肢1", "選択肢2", "選択肢3"))  # 第一引数：リスト名、第二引数：選択肢
   st.multiselect("メニューリスト（複数選択可）", ("選択肢1", "選択肢2", "選択肢3"))  # 複数選択可
   st.radio("ラジオボタン", ("選択肢1", "選択肢2", "選択肢3"))  # ラジオボタン
   st.text_input("文字入力欄")  # テキスト入力欄
   st.text_area("テキストエリア")  # テキストエリア
