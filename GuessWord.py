import time
import streamlit as st

st.title("⏱️🤡 เกมทายคำ")

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
def reset_game():
    st.session_state.ans1_val = ""  
    st.session_state.ans2_val = ""  
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()  
    st.session_state.is_ended = False  



@st.dialog("📊 ง่ายว่ะพี่น้อง")
def show_result_dialog(ans1, ans2):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()


    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")


    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")
        
    if u_ans3 == "bible":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")
    if u_ans4 == "corn":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")





    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 4:
        st.success("🎉 Piece of Cake!")
    else:
        st.error("💀 Cry Baby!")



st.button(" เริ่ม ", on_click=reset_game)


if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(20 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()


ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)

ans3 = st.text_input(
    "ข้อ 3: Christian's Thing. ",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: I like  _orn. ",
    value=st.session_state.ans4_val,
)
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4




if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button(" แน่ใจ? "):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()


if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4)

st.divider()
st.write("นางจิรัศมิ์ จิกเวียง เลขที่ 23ม.4/2")


