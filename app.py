import streamlit as st

# ✅ 変更分を明示的に表示
st.markdown("### ✅ 変更分：背景を白に設定")

# 背景を白に設定（CSS）
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

check = st.checkbox("他のウィジェットを表示する")

if check:
    st.button("ボタン")
    st.selectbox("メニューリスト", ("選択肢1", "選択肢2", "選択肢3"))
    st.multiselect("メニューリスト（複数選択可）", ("選択肢1", "選択肢2", "選択肢3"))
    st.radio("ラジオボタン", ("選択肢1", "選択肢2", "選択肢3"))
    st.text_input("文字入力欄")
    st.text_area("テキストエリア")
