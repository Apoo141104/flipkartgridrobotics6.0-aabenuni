# 🛠️ Flipkart Grid 6.0 Robotics Challenge – Aabenuni Team

Welcome to the official repository for our submission to the **Flipkart Grid 6.0 Robotics Challenge**.  
This project focuses on automating product quality assessment using computer vision and machine learning techniques.

---

## 🧠 Project Overview

Our solution aims to streamline the quality control process in warehouses by:

- 🏷️ **Brand and Product Classification**: Identifying products and their respective brands from images.
- 🔍 **Optical Character Recognition (OCR)**: Extracting textual information from product images for verification purposes.

By leveraging these techniques, we aim to enhance the efficiency and accuracy of product quality checks.

---

## 📁 Repository Structure

📦 flipkartgridrobotics6.0-aabenuni
```bash
├── brandandproductclassification.ipynb # Brand and product classification notebook
├── fruitqualitypredictionmodel.ipynb # Jupyter notebook for fruit quality prediction model
├── ocr.py # OCR script for text extraction
├── downloadimages.py # Script to download images
├── datasetpqc/ # Product quality check dataset
├── Processed_image_fruits/ # Processed fruit product images
├── labelled/ # Labeled training images
└── test_image.jpg # Sample image for testing
```
---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.7+
- pip (Python package installer)

### 🛠️ Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/Apoo141104/flipkartgridrobotics6.0-aabenuni.git
cd flipkartgridrobotics6.0-aabenuni
```

2. **(Optional) Create a Virtual Environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install Dependencies**:
```bash
pip install -r requirements.txt
```
###🧪 Usage

###🔍 Brand and Product Classification
1. **Launch the Jupyter Notebook**:
```bash
jupyter notebook brandandproductclassification.ipynb
```
2. **Follow the steps in the notebook to**:
Load and preprocess the dataset.
Train the classification model.
Evaluate the model's performance.
##📝 Optical Character Recognition (OCR)
**Run the OCR script using**:
```bash
python ocr.py
```
This will process test_image.jpg and output the extracted text.

##🍏 Fruit Quality Prediction Model
**Launch the Jupyter Notebook for fruit quality prediction**:
```bash
jupyter notebook fruitqualitypredictionmodel.ipynb
```
###📊 Results
<img width="725" alt="image" src="https://github.com/user-attachments/assets/2a25e361-bb58-4550-96a4-9b6ff1dadfec" />
<img width="725" alt="image" src="https://github.com/user-attachments/assets/ca2f194c-20dd-493d-95e1-cdd030d2b796" />
product_classification_model_model_performance

<img width="482" alt="image" src="https://github.com/user-attachments/assets/4cee71cc-5abf-4586-9486-4b36e3743605" />
<img width="482" alt="image" src="https://github.com/user-attachments/assets/b9b332aa-2ba8-4d8c-85c4-fe906d2c521c" />
Fruit_freshness_classification_model_performance



