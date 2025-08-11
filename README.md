# 📊 Real-Time Sentiment Analysis Dashboard

A real-time sentiment analysis tool built with **Streamlit** that fetches live tweets and classifies them as **Positive**, **Negative**, or **Neutral** using **VADER Sentiment Analysis**.

---

## 🚀 Features
- ✅ Real-time tweet fetching from Twitter (via snscrape — no paid API key required)
- ✅ Sentiment classification using **VADER**
- ✅ Interactive charts and metrics
- ✅ Web-based dashboard powered by **Streamlit**
- ✅ Free deployment on **Streamlit Community Cloud**

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Streamlit** — For the dashboard
- **snscrape** — To fetch tweets (no API key needed)
- **NLTK VADER** — For sentiment analysis
- **Pandas & Matplotlib** — For data processing & visualization

## 🚀 Live Demo
[Click here to view the deployed app](https://real-time-sentiment-analysis-dashboard-xgphavmub8ntcx46z63nuk.streamlit.app/)

---

## 📦 Installation

### 1️⃣ Clone the repository

git clone https://github.com/your-username/sentiment-dashboard.git
cd sentiment-dashboard

2️⃣ Create a virtual environment (Recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

📜 Usage
Run the Streamlit App
streamlit run app.py

Once the server starts, a local link will appear (e.g., http://localhost:8501).

📁 Project Structure
📦 sentiment-dashboard
 ┣ 📜 app.py               # Main Streamlit app
 ┣ 📜 requirements.txt     # Python dependencies
 ┣ 📜 README.md            # Project documentation
 ┗ 📂 data                 # (Optional) Store sample CSV files

🌐 Deploy on Streamlit Cloud

1.Push your project to GitHub.

2.Go to share.streamlit.io.

3.Sign in with GitHub and select your repository.

4.Set the Main file path to app.py.

5.Deploy 🚀.

👨‍💻 Author
Tanmay Borawke
📧 [tanmaymb2710@gmail.com]
🔗 https://www.linkedin.com/in/tanmay-borawke-6122-/

---
