import streamlit as st
import time

st.set_page_config(page_title="My集中タイマー", page_icon="⏰")

# 音を鳴らすための設定
def play_sound(url):
    sound_html = f"""
    <audio autoplay>
    <source src="{url}" type="audio/mp3">
    </audio>
    """
    # st.emptyの場所に差し込むことで、確実に音を鳴らそうと試みます
    st.components.v1.html(sound_html, height=0)

st.title("⏰ 残り時間がわかるタイマー")

tab1, tab2 = st.tabs(["集中モード", "休憩モード"])

with tab1:
    st.subheader("25分間集中！")
    if st.button("集中スタート！"):
        # 開始音
        play_sound("https://actions.google.com/sounds/v1/foley/beeps_short_half_second.ogg")
        
        timer_text = st.empty()  # 時間を表示する場所
        bar = st.progress(0)    # ゲージを表示する場所
        
        total_seconds = 25 * 60 # 25分
        
        for i in range(total_seconds, -1, -1):
            # 分:秒 の形式に計算
            mins, secs = divmod(i, 60)
            timer_text.header(f"残り {mins:02d}:{secs:02d}")
            
            # 進捗バーの更新
            progress = (total_seconds - i) / total_seconds
            bar.progress(progress)
            
            time.sleep(1) # 1秒待つ
            
        st.balloons()
        play_sound("https://actions.google.com/sounds/v1/alarms/alarm_clock_short.ogg")
        st.success("お疲れ様でした！")

with tab2:
    st.subheader("5分間休憩")
    if st.button("休憩スタート！"):
        play_sound("https://actions.google.com/sounds/v1/foley/beeps_short_half_second.ogg")
        
        timer_text = st.empty()
        total_seconds = 5 * 60
        
        for i in range(total_seconds, -1, -1):
            mins, secs = divmod(i, 60)
            timer_text.header(f"休憩残り {mins:02d}:{secs:02d}")
            time.sleep(1)
            
        st.snow()
        play_sound("https://actions.google.com/sounds/v1/alarms/bugle_tune.ogg")
        st.success("休憩終了！")

