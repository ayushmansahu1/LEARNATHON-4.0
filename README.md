# 🚗 AI Auto Insurance Fraud Detection System  

An **AI-powered fraud detection system** that uses **supervised learning** and a **Random Forest classifier** to detect fraudulent auto insurance claims.  

## 📌 Features  
✅ Detects fraudulent insurance claims using historical data  
✅ Implements **Random Forest** for high accuracy  
✅ Handles data preprocessing, feature selection & scaling  
✅ Provides model evaluation metrics (Accuracy, Precision, Recall, F1-score)  
✅ Can be integrated into insurance claim processing workflows  

## 🛠️ Tech Stack  
- Flash
- Vite
- Reactjs
- Scikit-learn  
- Pandas, NumPy  
- Matplotlib / Seaborn for visualization  
- Jupyter Notebook (for experimentation)

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
# Clone this repo
git clone https://github.com/your-username/auto-fraud-detection.git](https://github.com/ayushmansahu1/LEARNATHON-4.0/edit/main/README.md




Example Output
Accuracy: ~95%

Precision/Recall: Balanced for fraud cases

Feature Importance: Highlights key claim factors

🔮 Future Enhancements
Deploy as a REST API

Add Explainable AI (XAI) for decision transparency

Integrate with live insurance systems

## 📂 Project Structure  


# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

```js
export default tseslint.config([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...

      // Remove tseslint.configs.recommended and replace with this
      ...tseslint.configs.recommendedTypeChecked,
      // Alternatively, use this for stricter rules
      ...tseslint.configs.strictTypeChecked,
      // Optionally, add this for stylistic rules
      ...tseslint.configs.stylisticTypeChecked,

      // Other configs...
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default tseslint.config([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs['recommended-typescript'],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```
