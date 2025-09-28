# 🌱 Plant Disease Detection AI

An **AI-powered web application** that helps **farmers, gardeners, and researchers** detect plant diseases instantly using just an **image of a leaf**.  
Built with **TensorFlow**, **Flask**, and a clean **HTML/CSS/JS frontend**, this project combines **deep learning with real-world usability**.

---

## 🚀 Features

- 📸 **Image Upload** – Upload a plant leaf image for instant detection.  
- 🧠 **Deep Learning Model** – Powered by TensorFlow/Keras (`.keras` CNN model trained on plant disease datasets).  
- 📊 **Prediction Confidence** – Displays probability scores for each class.  
- 🌐 **User-Friendly Interface** – Fully responsive, clean web interface.  
- 📚 **Disease Insights** – Provides detailed descriptions and preventive measures for detected diseases.  

---

## 🛠️ Tech Stack

- 🌐 **Frontend:** HTML, CSS, JavaScript  
- 🔙 **Backend:** Flask (Python)  
- 🧠 **AI Model:** TensorFlow / Keras (`plant_disease_model.keras`)  
- 🗄️ **Database (Optional):** SQLite/MySQL for storing disease info & user queries  

---

## 📂 Project Structure

plant-disease-detection/
│── app.py # Flask backend
│── model/
│ └── plant_disease_model.keras # Trained AI model
│── static/
│ ├── style.css # Styling
│ └── js/
│ └── main.js # Frontend logic
│── templates/
│ └── index.html # Web UI
│── requirements.txt # Dependencies
│── README.md # Documentation

text

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repo
git clone https://github.com/MrShadow009/Plant-Disease-Recognition-System.git
cd Plant-Disease-Recognition-System

text

### 2️⃣ Create Virtual Environment
On Linux/Mac
python3 -m venv venv
source venv/bin/activate

On Windows
python -m venv venv
venv\Scripts\activate

text

### 3️⃣ Install Dependencies
pip install -r requirements.txt

text

### 4️⃣ Run the App
python app.py

text

### 5️⃣ Open in Browser  
👉 Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🌿 How It Works

1. User uploads a plant leaf image.  
2. AI model processes the image using a **Convolutional Neural Network (CNN)**.  
3. The model predicts the **disease type** and shows **confidence percentages**.  
4. (Optional) Disease details + remedies are displayed for better decision-making.  

---

## 🎯 Future Enhancements

- 📱 Mobile-friendly **PWA version** (installable on smartphones).  
- 🗂️ Integration with **larger multi-crop datasets**.  
- ☁️ **Cloud deployment** on Heroku, AWS, or Vercel.  
- 🧑‍🌾 Farmer dashboard with **disease history tracking**.  
- 🔔 **Push notifications** for disease updates & prevention tips.  

---

## 📸 Demo Screenshot

*(Insert your web app screenshot here)*  

---

## 🤝 Contributing

Contributions are welcome!  

- Fork the repo  
- Create a new branch (`feature-xyz`)  
- Commit your changes  
- Open a pull request  

For major changes, please open an issue first to discuss your intentions.  

---

## 📜 License

This project is **open-source**.  
Feel free to **use, modify, and share** with proper attribution.

---

## 🌟 Acknowledgements

- **TensorFlow** team – for the CNN framework  
- **Open plant disease datasets** – for training the model  
- Inspired by real-world needs of **farmers and agri-tech** initiatives  

---

### 💡 Showcase Your Project

If you’re deploying this app, tag it with `#PlantDiseaseAI` and inspire others! 🌿
