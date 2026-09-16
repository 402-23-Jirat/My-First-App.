import streamlit as st

st.markdown("# :red[คำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูง")

weight = st.number_input("กรอกน้ำหนัก (กิโลกรัม):", min_value=1.0, value=50.0)
height_cm = st.number_input("กรอกความสูง (เซนติเมตร):", min_value=1.0, value=160.0)

if st.button("ผลที่ได้"):

    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    st.write("---")
    st.header(f"ค่า BMI คือ: **{bmi:.2f}**")


    if bmi < 18.5:
        st.warning("น้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
    elif 18.5 <= bmi < 23.0:
        st.success("ปกติ (สุขภาพดี)")
    elif 23.0 <= bmi < 25.0:
        st.info("น้ำหนักเริ่มเกิน (ท้วม)")
    elif 25.0 <= bmi < 30.0:
        st.warning("อ้วน (ระดับ 1)")
    else:
        st.error("อ้วนมาก (ระดับ 2)")

st.divider()
st.write("นายจิรัศมิ์ จิกเวียง เลขที่ 23 ม.4/2")
