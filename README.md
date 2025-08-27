# 🎵 Music Recommendation System using Machine Learning

This is a **content-based music recommendation system** built using **Python, Pandas, NumPy, and Scikit-learn**.  
The system recommends **100 similar songs** based on user input and displays album images/posters using **Streamlit**.

---

## 📂 Project Structure

MRSF/
│── datamusic.csv # Dataset containing music details
│── MRS.ipynb # Jupyter Notebook (model training & testing)
│── mrsa.py # Deployment script (Streamlit app)
│── musicrec.pkl # Pickled DataFrame with songs metadata
│── similarities.pkl # Pickled similarity matrix


---

## 🚀 Features

- ✅ Recommends **100 similar songs** based on the input track.  
- ✅ Displays **album images/posters** for better UI experience.  
- ✅ Built using **Content-Based Filtering** with similarity matrix.  
- ✅ Deployed with **Streamlit** for an interactive web interface.  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

git clone https://github.com/Kavya8344/Music-recommendation-system-using-machine-learning.git
cd Music-recommendation-system-using-machine-learning
2️⃣ Create virtual environment (optional but recommended)
bash
Copy code
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Linux/Mac
3️⃣ Install dependencies
bash

pip install -r requirements.txt
▶️ Running the App
Start the Streamlit app:

bash

streamlit run mrsa.py
Then open your browser at: http://localhost:8501

📊 Working
User enters a song name.

The system finds the song in the dataset.

Computes similarity using precomputed similarities.pkl.

Displays 100 similar songs with album posters in a clean grid layout.

🛠️ Tech Stack
Python 3.x

Pandas, NumPy

Pickle (for model storage)

Streamlit (for deployment/UI)

📷 Sample UI
<img width="1920" height="1047" alt="sampel ui" src="https://github.com/user-attachments/assets/bb45b557-4031-4ab4-bc43-094da6b93069" />

👩‍💻 Author
Kavya8344

📜 License
This project is licensed under the MIT License.


