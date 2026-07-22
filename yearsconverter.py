import streamlit as st
st.title("แอปพลิเคชั่นแปลงปีพ.ศ.เป็นค.ศ.")

bh_year=st.number_input("กรอกปีพ.ศ.ที่ต้องการจะเปลี่ยน",value=2569)
ce_year=bh_year-543
st.header(f"ปี ค.ศ. คือ : {ce_year}")
