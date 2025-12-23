import streamlit as st
import time

st.set_page_config(page_title="集中タイム", page_icon="⏳")

st.title("⏳ 集中タイマー")
st.write("25分の集中と、5分の休憩を繰り返しましょう。")

# タブでモードを切り替え
tab1, tab2 = st.tabs(["集中モード", "休憩モード"])

with tab1:
    st.subheader("25分間、目の前のことに集中！")
    if st.button("25分タイマー開始"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for percent_complete in range(100):
            # 25分間を100分割して進める（デモ用に短くしたい場合は 15.0 を 0.1 とかにしてね）
            time.sleep(15.0) 
            progress_bar.progress(percent_complete + 1)
            status_text.text(f"集中度: {percent_complete + 1}%")
            
        st.balloons()
        st.success("お疲れ様です！5分間の休憩に入りましょう。")

with tab2:
    st.subheader("ゆっくり休みましょう")
    if st.button("5分タイマー開始"):
        st.info("休憩中です...")
        time.sleep(5) # 実際は300秒ですが、動作確認用に短くしています
        st.snow()
        st.success("休憩終了！さあ、次へ進みましょう。")
