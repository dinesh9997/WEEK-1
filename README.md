# 🌊 Water Quality Prediction & Safety Assessor
[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Edunet Foundation](https://img.shields.io/badge/Internship-Edunet%20Foundation-orange.svg)](https://edunetfoundation.org/)

An advanced Machine Learning application that predicts water pollutants based on Year and Station ID, then automatically assesses whether the water is safe for human consumption based on international health standards.

This project was successfully developed by **Gujju Dinesh** as part of the **Green Skills AI Technology Internship** on **Edunet Foundation** (an AICTE Virtual Internship sponsored by Shell, June–July 2025).

🚀 **Live Interactive Demo:** [https://dinesh9997-week-1-app-umfu9f.streamlit.app/](https://dinesh9997-week-1-app-umfu9f.streamlit.app/)

---

## 🔍 Project Overview

Access to clean, safe drinking water is one of the most critical global environmental and health concerns. Early detection of water pollution is vital for timely ecological intervention.

This project utilizes supervised machine learning—specifically a **Multi-Output Random Forest Regressor**—to predict concentrations of multiple chemical and biological pollutants simultaneously.

### 🌟 Key Features
* **Multi-Target Regressor:** Predicts multiple pollutant concentrations simultaneously using a unified Random Forest backbone.
* **Instant Safety Evaluation:** Automatically compares predicted metrics against standard safety thresholds (e.g. O2, NO3, SO4, CL) to give a definitive "SAFE" or "NOT SAFE" assessment.
* **Streamlit Interface:** High-end, interactive, and responsive web app deployed to the cloud for real-time predictions.

---

## 🌊 Predicted Water Quality Parameters & Safety Standards

The application predicts the concentrations of 6 major chemical/biological water quality indicators. It automatically flags them if they cross standard health limits:

| Parameter | Standard / Safe Range | Health Impact / Description |
| :--- | :--- | :--- |
| **O2 (Dissolved Oxygen)** | `6.5 - 14.0 mg/L` | Critical for aquatic life; abnormal values indicate biological contamination. |
| **NO3 (Nitrate)** | `0.0 - 50.0 mg/L` | High levels cause methemoglobinemia ("blue baby syndrome"). |
| **NO2 (Nitrite)** | `0.0 - 3.0 mg/L` | Highly toxic chemical compound indicating industrial or waste runoff. |
| **SO4 (Sulfate)** | `0.0 - 250.0 mg/L` | Excess causes laxative effects and salty taste. |
| **PO4 (Phosphate)** | `0.0 - 0.5 mg/L` | High levels cause eutrophication and algae blooms. |
| **CL (Chloride)** | `0.0 - 250.0 mg/L` | High concentrations give a salty taste and corrode pipes. |

---

## 🧪 Tech Stack & Libraries Used

* **Python 3.12**
* **Streamlit** – Web framework for local development and cloud deployment
* **Scikit-Learn** – Model building (`MultiOutputRegressor`, `RandomForestRegressor`) and preprocessing
* **Pandas & NumPy** – High-performance data structures and numerical operations
* **Joblib** – Python model serialization and loading

---

## 📈 Machine Learning Pipeline & Model Details

The model architecture utilizes a **Multi-Output Regressor wrapper** wrapped around a **RandomForestRegressor** to output multiple continuous values (pollutant concentrations) for a given `Year` and `Station ID`.

* **Pretrained Models:** 
  * `water_quality_model.pkl` (Random Forest Multi-Output Regressor)
  * `model_columns.pkl` (Feature Columns Mapper)

---

## 💻 Running the App Locally

### 1. Clone the Repository
```bash
git clone https://github.com/dinesh9997/WEEK-1.git
cd WEEK-1
```

### 2. Install Dependencies
Ensure you have Python 3.12+ installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Start the Streamlit Application
```bash
python -m streamlit run app.py
```
Open the local URL shown in the terminal (usually http://localhost:8501) to access the app in your browser.

---

## 👤 Author & Acknowledgment

* **Author:** Gujju Dinesh
* **Internship Sponsor:** Shell & Edunet Foundation (Green Skills AI Internship, June–July 2025)
* **Virtual Platform:** AICTE


