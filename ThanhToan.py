

from numpy import True_
import streamlit as st



st.set_page_config(
    page_title="THANHTOAN",
    page_icon="👋",
)
import base64
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("hinh.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("");
background-size: 200%;
background-position: 30% 45%;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: 50% 45%;
background-size: 400%;
}}
[data-testid="stSidebarNav"] span {{
color:white;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True
)
st.markdown(
    f'''<style>
    .stApp {{
    background-image: url(https://img5.thuthuatphanmem.vn/uploads/2021/09/22/anh-nen-cay-tre-lam-slide_094528280.jpg);
    background-size: cover;
    }}



    </style>''',
    unsafe_allow_html=True_
)
st.write("<span style='color: white; font-size: 36px;'> ☺️ </span>",
         unsafe_allow_html=True)
st.write("<span style='color: white; font-size: 36px;'> ☺️ </span>",
         unsafe_allow_html=True)

st.write("<span style='color: blue; font-size: 36px;'> 👋 BÀI BÁO CÁO CUỐI KÌ 👋</span>",
         unsafe_allow_html=True)

st.sidebar.success("Select a demo above.")

st.markdown(

    """

    ### 👉MÔN: TRÍ TUỆ NHÂN TẠO_NhÓM 03CLC
    ### 👉GVHD: PGS.TS NGUYỄN TRƯỜNG THỊNH
    ### 👉SVTH: NGUYỄN THANH TOÀN - 20146441
    
    
"""
)



