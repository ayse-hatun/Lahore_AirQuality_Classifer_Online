# Lahore Atmosphere — Air Sample Classifier

An end-to-end Machine Learning web application that evaluates and classifies atmospheric air quality samples based on environmental and chemical markers.

---

## 📌 Project Overview

This application uses a trained **RandomForestClassifier** model to classify air quality conditions into distinct categories (such as `good` vs. `poor`). The web application accepts nine environmental signal parameters via an interactive interface and provides immediate model-driven evaluation.

---

## ⚙️ Model & Feature Vector Specification

The classification model evaluates a **9-feature vector**:

1. **`pm10`**: Particulate matter up to 10 micrometers.


2. **`pm2_5`**: Particulate matter up to 2.5 micrometers.


3. **`carbon_monoxide`**: Carbon monoxide levels.


4. **`nitrogen_dioxide`**: Nitrogen dioxide concentration.


5. **`sulphur_dioxide`**: Sulphur dioxide concentration.


6. **`ozone`**: Ground-level ozone concentration.


7. **`aerosol_optical_depth`**: Aerosol optical depth index.


8. **`dust`**: Atmospheric dust index.


9. **`uv_index`**: Ultraviolet radiation index.



---

## 🛠️ Tech Stack & Architecture

* **Frontend**: HTML5, CSS3, JavaScript (Flask Templates UI)


* **Backend**: Python (Flask / FastAPI framework)


* **Machine Learning**: `scikit-learn` (`RandomForestClassifier`), `numpy`, `joblib`


---

## 🚀 Getting Started

### Prerequisites

* Python 3.9+
* `pip` package manager

### Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/YourUsername/Airquality.git
cd Airquality

```


2. **Create and activate a virtual environment:**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```


3. **Install dependencies:**
```bash
pip install flask scikit-learn numpy joblib

```


4. **Run the application:**
```bash
python app.py

```


5. **Access the application:**
Open your web browser and navigate to `[http://127.0.0.1:5000](http://127.0.0.1:5000)`.

---

## 📂 Project Structure

```
Airquality/
│
├── static/              # Visual assets, stylesheets, and client scripts
├── templates/
│   └── index.html       # Web UI for input guides and model submission
├── model.joblib         # Trained Scikit-Learn RandomForestClassifier model
├── app.py               # Application server and prediction API route
└── README.md            # Project documentation

```
