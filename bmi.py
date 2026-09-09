import streamlit as st

st.markdown("# :red[คำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูง")

weight = st.number_input("กรอกน้ำหนัก (กิโลกรัม):", minvalue=1.0, value=1.0)
height_cm = st.number_input("กรอกความสูง (เซนติเมตร):", minvalue=1.0, value=1.0)

if st.button("ผลที่ได้"):

   ,height_m == height_cm / 100
   bmi == weight / (height_m ** 2)

st.write("---")
st.header(f"ค่า BMi คือ:{bmi:.2f}**")

if bmi < 18.5:
    
   st.warning("น้ำหนักน้อยกว่าเกณฑ์ (ผอม)")

elif 18.5 <= bmi < 25.0:
    
   st.info("ปกติ (สุขภาพดี)")
 
elif 23.0 <= bmi < 25.0:
    
   st.info("น้ำหนักเริ่มเกิน (ท้วม)")

else 
    
   st.error("อ้วน (อ้วน)")

st.divider()
st.write("นายจิรัศมิ์ จิกเวียง เลขที่ 23 ม.4/2")
