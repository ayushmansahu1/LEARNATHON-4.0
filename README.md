# LEARNATHON-4.0
LEARNATHON 4.0 GIET UNIVERSITY,GUNUPUR-AYUSHMAN SAHU,ABINASH CHOUDHURY & PRIYANSHU SEKHAR NANDA TEAM(SC2)4_TEAM NO.-16
# 🚗 AI Auto Insurance Fraud Detection System  

An **AI-powered fraud detection system** that uses **supervised learning** and a **Random Forest classifier** to detect fraudulent auto insurance claims.  

## 📌 Features  
✅ Detects fraudulent insurance claims using historical data  
✅ Implements **Random Forest** for high accuracy  
✅Implements **Gradient booassting techniques** 
✅ Handles data preprocessing, feature selection & scaling  
✅ Provides model evaluation metrics (Accuracy, Precision, Recall, F1-score)  
✅ Can be integrated into insurance claim processing workflows  

## 🛠️ Tech Stack  
- reactjs
- Scikit-learn  
- Python,Pandas, NumPy  
- Matplotlib / Seaborn for visualization  
- Jupyter Notebook (for experimentation)  

## 📂 Project Structure  
├── data/ # Dataset (claims data)
├── notebooks/ # Jupyter notebooks for EDA & model training
├── models/ # Saved trained models
├── fraud_detection.py # Main model training & prediction script
└── README.md # Project documentation


## 🚀 How It Works  
1. **Data Preprocessing** – Cleans & prepares insurance claim data  
2. **Feature Scaling & Selection** – Normalizes features for better model performance  
3. **Model Training** – Trains a **Random Forest Classifier**  
4. **Fraud Detection** – Predicts whether a new claim is **Fraudulent** or **Legit**  
5. **Evaluation** – Generates metrics & visualizations  

## ▶️ Quick Start  
```bash
**# Clone this repo
git clone https://github.com/ayushmansahu1/LEARNATHON-4.0/edit/main/README.md

# Navigate into the folder
cd auto-fraud-detection

# Install dependencies
pip install -r requirements.txt

# Run training script
python fraud_detection.py
📊 Example Output
Accuracy: ~95%

Precision/Recall: Balanced for fraud cases

Feature Importance: Highlights key claim factors

🔮 Future Enhancements
Deploy as a REST API

Add Explainable AI (XAI) for decision transparency

Integrate with live insurance systems**
