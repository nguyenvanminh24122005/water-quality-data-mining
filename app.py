import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="Dự đoán chất lượng nước",
    page_icon="💧",
    layout="wide"
)

# =========================
# CSS giao diện
# =========================
st.markdown("""
<style>
.main {
    background-color: #f8fbff;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.title-box {
    background: linear-gradient(135deg, #0099cc, #00c6a7);
    padding: 24px;
    border-radius: 18px;
    color: white;
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
    margin-bottom: 20px;
}
.info-box {
    background-color: white;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    margin-bottom: 16px;
}
.result-safe {
    background-color: #e8f8ee;
    border-left: 8px solid #1f9d55;
    padding: 18px;
    border-radius: 12px;
    color: #14532d;
    font-size: 18px;
    font-weight: 600;
}
.result-unsafe {
    background-color: #fdecec;
    border-left: 8px solid #dc2626;
    padding: 18px;
    border-radius: 12px;
    color: #7f1d1d;
    font-size: 18px;
    font-weight: 600;
}
.small-note {
    font-size: 14px;
    color: #555;
}
</style>
""", unsafe_allow_html=True)

# =========================
# Load model
# =========================
@st.cache_resource
def load_model():
    return joblib.load("outputs/random_forest_model.pkl")

model = load_model()

# =========================
# Header
# =========================
st.markdown("""
<div class="title-box">
    <h1>💧 Hệ thống dự đoán chất lượng nước</h1>
    <p style="font-size:18px; margin-bottom:0;">
        Ứng dụng hỗ trợ dự đoán nước có an toàn để uống hay không dựa trên các chỉ số hóa học và vật lý của nước.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Sidebar
# =========================
with st.sidebar:
    st.header("📌 Hướng dẫn sử dụng")
    st.write("""
    - Nhập các chỉ số chất lượng nước vào biểu mẫu.
    - Nhấn **Dự đoán** để xem kết quả.
    - Kết quả chỉ mang tính **hỗ trợ tham khảo**, không thay thế kiểm định thực tế.
    """)
    
    st.header("📖 Ý nghĩa nhãn")
    st.write("""
    - **An toàn**: Nước có khả năng uống được.
    - **Không an toàn**: Nước có nguy cơ không đạt tiêu chuẩn uống.
    """)

    st.header("ℹ️ Thông tin đề tài")
    st.write("""
    **Bài tập lớn Data Mining**  
    Đề tài 9: **Phân tích chất lượng nước**
    """)

# =========================
# Mô tả nhanh
# =========================
st.markdown("""
<div class="info-box">
    <h3>Giới thiệu</h3>
    <p>
        Mô hình sử dụng thuật toán <b>Random Forest</b> để dự đoán khả năng uống được của nước
        dựa trên 9 thuộc tính đầu vào: pH, độ cứng, tổng chất rắn hòa tan, chloramines, sulfate,
        conductivity, organic carbon, trihalomethanes và turbidity.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Input
# =========================
st.subheader("🧪 Nhập thông số mẫu nước")

col1, col2, col3 = st.columns(3)

with col1:
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
    hardness = st.number_input("Độ cứng (Hardness)", min_value=0.0, max_value=500.0, value=200.0, step=1.0)
    solids = st.number_input("Tổng chất rắn hòa tan (Solids)", min_value=0.0, max_value=50000.0, value=15000.0, step=100.0)

with col2:
    chloramines = st.number_input("Chloramines", min_value=0.0, max_value=20.0, value=7.0, step=0.1)
    sulfate = st.number_input("Sulfate", min_value=0.0, max_value=500.0, value=300.0, step=1.0)
    conductivity = st.number_input("Độ dẫn điện (Conductivity)", min_value=0.0, max_value=1000.0, value=400.0, step=1.0)

with col3:
    organic_carbon = st.number_input("Organic Carbon", min_value=0.0, max_value=30.0, value=12.0, step=0.1)
    trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, max_value=150.0, value=70.0, step=0.1)
    turbidity = st.number_input("Độ đục (Turbidity)", min_value=0.0, max_value=10.0, value=4.0, step=0.1)

st.markdown('<p class="small-note">* Các giá trị mặc định chỉ mang tính minh họa.</p>', unsafe_allow_html=True)

# =========================
# Hiển thị nhanh thông tin
# =========================
st.subheader("📋 Tóm tắt thông số đầu vào")
m1, m2, m3, m4 = st.columns(4)
m1.metric("pH", f"{ph:.2f}")
m2.metric("Hardness", f"{hardness:.2f}")
m3.metric("Solids", f"{solids:.2f}")
m4.metric("Turbidity", f"{turbidity:.2f}")

# =========================
# Predict
# =========================
if st.button("🔍 Dự đoán", use_container_width=True):
    data = np.array([[
        ph,
        hardness,
        solids,
        chloramines,
        sulfate,
        conductivity,
        organic_carbon,
        trihalomethanes,
        turbidity
    ]])

    prediction = model.predict(data)[0]

    st.subheader("📌 Kết quả dự đoán")

    if prediction == 1:
        st.markdown("""
        <div class="result-safe">
            ✅ Kết quả: Nước được dự đoán là <b>AN TOÀN ĐỂ UỐNG</b>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="result-unsafe">
            ❌ Kết quả: Nước được dự đoán là <b>KHÔNG AN TOÀN ĐỂ UỐNG</b>
        </div>
        """, unsafe_allow_html=True)

    # Nếu model có predict_proba thì hiển thị thêm xác suất
    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(data)[0]
        st.subheader("📊 Độ tin cậy của mô hình")
        c1, c2 = st.columns(2)
        c1.metric("Xác suất Không an toàn", f"{prob[0]*100:.2f}%")
        c2.metric("Xác suất An toàn", f"{prob[1]*100:.2f}%")

        st.progress(float(prob[1]))

    st.subheader("📝 Nhận xét")
    if prediction == 1:
        st.success(
            "Mẫu nước này có xu hướng đạt điều kiện uống được theo mô hình dự đoán. "
            "Tuy nhiên vẫn nên kiểm tra thực tế nếu dùng trong môi trường sinh hoạt hoặc sản xuất."
        )
    else:
        st.warning(
            "Mẫu nước này có nguy cơ không đạt tiêu chuẩn uống được. "
            "Nên kiểm tra lại nguồn nước và thực hiện thêm các bước xét nghiệm hoặc xử lý cần thiết."
        )

# =========================
# Footer
# =========================
st.markdown("---")
st.caption("Ứng dụng minh họa cho bài tập lớn môn Khai phá dữ liệu - Đề tài 9: Phân tích chất lượng nước")