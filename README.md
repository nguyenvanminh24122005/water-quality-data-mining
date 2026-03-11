# PHÂN TÍCH CHẤT LƯỢNG NƯỚC BẰNG KHAI PHÁ DỮ LIỆU

## 1. Giới thiệu đề tài

Đây là project bài tập lớn môn **Khai phá dữ liệu / Dữ liệu lớn** với **Đề tài 9: Phân tích chất lượng nước**.

Mục tiêu của project là phân tích các chỉ số hóa học và vật lý của nước để:

- khám phá mối quan hệ giữa các chỉ số chất lượng nước
- phân nhóm các mẫu nước theo đặc điểm tương đồng
- dự đoán nước có an toàn để uống hay không
- thử nghiệm học bán giám sát trong bối cảnh thiếu nhãn
- dự đoán một biến liên tục liên quan đến chất lượng nước

Bộ dữ liệu sử dụng là **Water Potability Dataset** từ Kaggle.

---

## 2. Bộ dữ liệu

- **Tên dataset:** Water Potability Dataset
- **Nguồn:** Kaggle
- **Biến mục tiêu:** `Potability`
  - `1`: nước an toàn để uống
  - `0`: nước không an toàn để uống

### Các thuộc tính chính

- `pH`: độ axit/kiềm của nước
- `Hardness`: độ cứng của nước
- `Solids`: tổng chất rắn hòa tan
- `Chloramines`: chất khử trùng trong nước
- `Sulfate`: nồng độ sulfate
- `Conductivity`: độ dẫn điện
- `Organic_carbon`: lượng carbon hữu cơ
- `Trihalomethanes`: hợp chất sinh ra trong quá trình khử trùng
- `Turbidity`: độ đục của nước
- `Potability`: nhãn phân lớp

---

## 3. Nội dung project

Project bao gồm các phần chính sau:

### 3.1. Phân tích dữ liệu khám phá (EDA)
- kiểm tra cấu trúc dữ liệu
- mô tả bộ dữ liệu và data dictionary
- phân tích phân bố dữ liệu
- kiểm tra giá trị thiếu
- phân tích tương quan giữa các thuộc tính

### 3.2. Khai phá luật kết hợp
- rời rạc hóa các thuộc tính liên tục
- áp dụng thuật toán **Apriori**
- tìm các luật kết hợp giữa các chỉ số chất lượng nước
- phân tích support, confidence, lift

### 3.3. Phân cụm dữ liệu
- chuẩn hóa dữ liệu
- áp dụng thuật toán **K-Means**
- chọn số cụm bằng phương pháp Elbow
- trực quan hóa cụm bằng PCA
- diễn giải đặc điểm từng cụm

### 3.4. Phân lớp
- dự đoán nước có uống được hay không
- các mô hình sử dụng:
  - Logistic Regression
  - Random Forest
- đánh giá bằng các chỉ số phân lớp

### 3.5. Học bán giám sát
- mô phỏng tình huống thiếu dữ liệu gán nhãn
- sử dụng thuật toán **Label Spreading**
- so sánh hiệu quả khi chỉ có một phần dữ liệu được gán nhãn

### 3.6. Hồi quy
- dự đoán biến liên tục `Solids`
- các mô hình sử dụng:
  - Linear Regression
  - Ridge Regression
  - Random Forest Regressor

### 3.7. Demo ứng dụng
- xây dựng ứng dụng **Streamlit**
- cho phép nhập các chỉ số nước
- dự đoán nước có an toàn để uống hay không

---

## 4. Cấu trúc thư mục project

```text
water_project/
│
├── README.md
├── requirements.txt
├── app.py
│
├── data/
│   ├── raw/
│   │   └── water_potability.csv
│   └── processed/
│       └── water_clean.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_association_rules.ipynb
│   ├── 03_clustering.ipynb
│   ├── 04_classification.ipynb
│   ├── 05_semi_supervised.ipynb
│   └── 06_regressio.ipynb
│
├── outputs/
│   ├── association_rules.csv
│   ├── classification_model_comparison.csv
│   ├── classification_results.csv
│   ├── clustering_results.csv
│   ├── random_forest_model.pkl
│   ├── regression_results.csv
│   └── semi_supervised_results.csv
│
└── scripts/
    └── predict_water.py