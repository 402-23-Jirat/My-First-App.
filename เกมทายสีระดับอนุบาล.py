import random
import streamlit as st
 
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
 
st.title(" เกมทายสีผสมระดับราชันย์อนุบาล😎")
 
QUESTIONS = [
    ("แดง + เหลือง", "ส้ม"),
    ("น้ำเงิน + เหลือง", "เขียว"),
    ("แดง + น้ำเงิน", "ม่วง"),
    ("น้ำเงิน + เขียว", "ฟ้า"),
    ("แดง + เหลือง + น้ำเงิน", "น้ำตาล"),
]
 
COLOR_MAP = {
    "แดง": "red",
    "เหลือง": "orange",   
    "น้ำเงิน": "blue",
    "เขียว": "green",
    "ม่วง": "violet",
    "ฟ้า": "blue",
    "น้ำตาล": "gray",    
}
 
 
def colorize(question_text):
    """แปลง 'แดง + เหลือง' ให้เป็น ':red[แดง] + :orange[เหลือง]'"""
    parts = question_text.split(" + ")
    colored_parts = []
    for part in parts:
        color_name = COLOR_MAP.get(part, None)
        if color_name:
            colored_parts.append(f":{color_name}[{part}]")
        else:
            colored_parts.append(part)
    return " + ".join(colored_parts)
 
 
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
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False
if "shuffled_questions" not in st.session_state:
    shuffled = QUESTIONS.copy()
    random.shuffle(shuffled)
    st.session_state.shuffled_questions = shuffled
 
 
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.session_state.is_ended = False
    shuffled = QUESTIONS.copy()
    random.shuffle(shuffled)
    st.session_state.shuffled_questions = shuffled
 
 
@st.dialog(" ง่ายว่ะพี่น้อง")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()
    score = 0
 
    user_answers = [ans1, ans2, ans3, ans4, ans5]
    questions = st.session_state.shuffled_questions
 
    for i, ((question_text, correct_answer), user_answer) in enumerate(
        zip(questions, user_answers), start=1
    ):
        u_ans = user_answer.strip().lower()
        if u_ans == correct_answer.lower():
            st.success(f"✅ ข้อ {i} ({question_text}): ถูกต้อง")
            score += 1
        else:
            st.error(
                f"❌ ข้อ {i} ({question_text}): "ผิดได้ไงก่อน)"
            )
 
    st.info(f" ได้คะแนนรวม: {score} คะแนน")
 
    if score == 5:
        st.success(" ราชา💪😍")
    elif 1 <= score <= 4:
        st.success(" อีกนิดเดียวพยายามหน่อย🥀 ")
    else:
        st.error(" ถามจริง🤡 ")
 
    if st.button("เล่นอีกครั้ง"):
        reset_game()
        st.rerun()
 
 
st.divider()
 
q1, q2, q3, q4, q5 = st.session_state.shuffled_questions
 
ans1 = st.text_input(
    f" {colorize(q1[0])} ",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    f" {colorize(q2[0])} ",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    f" {colorize(q3[0])} ",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    f" {colorize(q4[0])} ",
    value=st.session_state.ans4_val,
)
ans5 = st.text_input(
    f" {colorize(q5[0])} ",
    value=st.session_state.ans5_val,
)
 
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
 
if not st.session_state.is_ended:
    if st.button(" Confirmed? "):
        st.session_state.is_ended = True
        st.rerun()
 
if st.session_state.is_ended:
    show_result_dialog(ans1, ans2, ans3, ans4, ans5)
 
st.divider()
 
