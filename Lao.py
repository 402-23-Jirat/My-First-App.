import streamlit as st

st.title(" เกมทายสีผสม")

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""

def reset_game():
    st.session_state.ans1_val = ""  
    st.session_state.ans2_val = ""  
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""  



@st.dialog(" ง่ายว่ะพี่น้อง")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()

    
    if u_ans1 == "ส้ม":
        st.success("✅ ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ผิดได้ไงเด็กอนุบาลยังตอบถูกเลย (คุณตอบ '{u_ans1}')")


    if u_ans2 == "เขียว":
        st.success("✅  ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    
    if u_ans3 == "ม่วง":
        st.success("✅  ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    
    if u_ans4 == "ฟ้า":
        st.success("✅ ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    
    if u_ans5 == "น้ำตาล":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ไม่ถูกต้อง (คุณตอบ '{u_ans5}')")


    st.info(f" ได้คะแนนรวม: {score} คะแนน")

    if score == 5:
        st.success(" ราชา")
    elif 1 ≥ score ≥ 4 :
        st.Success(" อีกหน่อย Gng ")
    else :
        st.error(" โง่ ")


st.divider()


ans1 = st.text_input(
    "\033[32m" + " แดง + เหลือง ",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    " น้ำเงิน + เหลือง ",
    value=st.session_state.ans2_val,
)

ans3 = st.text_input(
    "แดง + น้ำเงิน ",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "น้ำเงิน + เขียว",
    value=st.session_state.ans4_val,
)

ans5 = st.text_input(
    " แดง + เหลือง + น้ำเงิน",
    value=st.session_state.ans5_val,
)

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button(" Confirmed? "):
        st.session_state.is_ended = True
        st.rerun()



if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5)

st.divider()

