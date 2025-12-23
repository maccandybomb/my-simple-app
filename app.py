import streamlit as st
import time

# 1. ブラウザのタブ設定
st.set_page_config(
    page_title="My集中タイマー", 
    page_icon="⏰",
    layout="centered"
)

# 2. 音を鳴らすための魔法（関数）
def play_sound(url):
    # ブラウザで音を再生するHTMLコード
    sound_html = f"""
    <audio autoplay>
    <source src="{url}" type="audio/mp3">
    </audio>
    """
    st.components.v1.html(sound_html, height=0)

st.title("⏰ 集中タイマー (音あり)")

tab1, tab2 = st.tabs(["集中モード", "休憩モード"])

with tab1:
    st.subheader("25分間、全力投球！")
    if st.button("集中スタート"):
        # スタート時の音（短いチャイム）
        play_sound("https://actions.google.com/sounds/v1/foley/beeps_short_half_second.ogg")
        
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(15) # 実際は15秒 × 100 = 25分
            progress_bar.progress(i + 1)
        
        st.balloons()
        # 終了時の音（ベルの音）
        play_sound("https://actions.google.com/sounds/v1/alarms/alarm_clock_short.ogg")
        st.success("25分経過！お疲れ様でした。")

with tab2:
    st.subheader("ゆっくり休憩")
    if st.button("休憩スタート"):
        play_sound("https://actions.google.com/sounds/v1/foley/beeps_short_half_second.ogg")
        
        st.info("5分間の休憩中...")
        time.sleep(300) # 300秒 = 5分
        
        st.snow()
        play_sound("https://actions.google.com/sounds/v1/alarms/bugle_tune.ogg")
        st.success("休憩終了！")

