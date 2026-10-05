# 🏡 California AI House Price Predictor

An interactive **Machine Learning web application** that predicts California house prices using a trained **Linear Regression model** and provides an easy-to-use interface built with **Streamlit**.

The application converts machine learning predictions into a simple user experience where users can enter property and neighborhood details, receive an estimated house price, and understand the factors influencing the prediction.

---

# 🚀 Live Demo

```
https://california-house-price-predictor-ml-model.streamlit.app/
```

---

# 📌 Project Overview

Buying or evaluating a house requires understanding multiple factors such as location, income level, house characteristics, and neighborhood conditions.

This project uses Machine Learning to estimate house prices based on California housing data.

The goal of this project is to demonstrate:

- End-to-end Machine Learning deployment
- Model integration with a web application
- User-friendly ML interface design
- Real-world prediction workflow

---

# ✨ Features

## 🤖 Machine Learning Prediction

- Trained Linear Regression model
- Model saved using Joblib
- Real-time prediction using user inputs
- Automatic feature handling from saved metadata

---

## 🎨 User-Friendly Interface

- Modern Streamlit dashboard
- Clean and minimal UI
- Interactive input controls
- Helpful descriptions and examples
- Prediction result visualization

---

## 📊 Prediction Insights

The application provides:

- Estimated house price
- Input summary table
- AI-based interpretation messages
- Prediction explanation for users

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- Pandas
- NumPy

## Model

- Linear Regression

## Deployment Framework

- Streamlit

## Model Serialization

- Joblib

## UI Styling

- Streamlit Components
- Custom CSS

---

# 📂 Project Structure

```
California-House-Price-Predictor/

│
├── app.py
│
├── california_1.joblib
│
├── requirements.txt
│
├── README.md
│
└── static/
│    │
│    └── style.css
│    
└── templates/
    │
    └── index.html
```

---

# 📦 Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/california-house-price-predictor.git
```

Move into project folder:

```bash
cd california-house-price-predictor
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

Start Streamlit:

```bash
streamlit run app.py
```

Application will open:

```
http://localhost:8501
```

---

# 📥 Model Information

The trained model is stored as:

```
california_1.joblib
```

The file contains:

```python
{
    "model": trained_model,
    "columns": feature_columns
}
```

Example:

```python
joblib.dump(
    {
        "model": model,
        "columns": columns
    },
    "california_1.joblib"
)
```

---

# 📊 Model Features

The model uses the following input features:

| Feature | Description |
|---|---|
| MedInc | Median income of neighborhood |
| HouseAge | Average age of houses |
| AveRooms | Average number of rooms |
| Population | Neighborhood population |
| AveOccup | Average household occupancy |
| Longitude | Geographic location |

---

# 🧠 Machine Learning Workflow

The project follows a complete ML pipeline:

```
Data Collection
        |
        ↓
Data Cleaning
        |
        ↓
Exploratory Data Analysis
        |
        ↓
Feature Selection
        |
        ↓
Model Training
        |
        ↓
Model Evaluation
        |
        ↓
Model Serialization
        |
        ↓
Streamlit Deployment
```

---

# 📈 Future Improvements

Possible enhancements:

### Model Improvements

- Try advanced algorithms:
  - Random Forest
  - Gradient Boosting
  - XGBoost

- Hyperparameter tuning

- Model comparison dashboard


### Explainable AI

Add:

- SHAP explanations
- Feature importance charts
- Prediction confidence


### Application Improvements

- User authentication
- Save prediction history
- Interactive California map
- Download prediction report
- Deploy on cloud

---

# 🐛 Troubleshooting

## Model Loading Error

Make sure:

```
california_1.joblib
```

exists in the project folder.

---

## Feature Mismatch Error

Error:

```
X has n features but model expects m features
```

Solution:

Ensure input features match:

```python
obj["columns"]
```

from the saved model.

---

## Package Version Warning

If you see:

```
InconsistentVersionWarning
```

install the same scikit-learn version used during training:

```bash
pip install scikit-learn==1.7.2
```

---

# 👨‍💻 Author

**Vikrant**

Machine Learning | Python | Data Science | AI Enthusiast

---

# ⭐ Support

If you found this project useful:

- Give it a ⭐ on GitHub
- Share feedback
- Suggest improvements

---

# 📜 License

This project is created for educational and portfolio purposes.