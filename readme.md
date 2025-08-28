# 👑 AcademiaMart – An Unofficial Store For Students of KKU

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge\&logo=python\&logoColor=ffdd54)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge\&logo=django)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge\&logo=firebase)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge\&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge\&logo=sqlite)
![PayPal](https://img.shields.io/badge/PayPal-003087?style=for-the-badge\&logo=paypal)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github)
![License](https://img.shields.io/badge/License-MIT-green)
![Python Version](https://img.shields.io/badge/Python-3.11-blue)
![Django Version](https://img.shields.io/badge/Django-4.2-blueviolet)

---

**AcademiaMart** is a **feature-packed ecommerce platform** built with **Django, Firebase, and modern web technologies**. Originally designed for **KKU students**, it now serves as a **professional portfolio project**, it allows users to **buy, sell, and manage products seamlessly** while providing an **intuitive, responsive, and multilingual interface**.

This project demonstrates advanced functionalities such as:

* **Secure user authentication and onboarding**
* **Product management** with image cropping, visibility duration, and developer picks
* **Personalized suggested products based on user activity**
* **Search, sort, wishlist, rating, and commenting**
* **OTP-secured purchases and PayPal integration for services**
* **Real-time notifications and analytics with Firebase**

💡 **Note:** This project is **not publicly deployed**, it is intended to demonstrate my full-stack capabilities.

---

## 🌟 Key Features & Highlights

| Feature             | Icon | Description                                             |
| ------------------- | ---- | ------------------------------------------------------- |
| User Authentication | 👤   | Secure sign-up/login with username availability check   |
| Onboarding          | 🎉   | Friendly welcome messages for first-time users          |
| Sell Products       | 🛒   | Crop images, set product duration, hide/unhide products |
| Developer’s Pick    | 🌟   | Handpicked products showcased to all users              |
| Suggested Products  | 🤖   | Personalized recommendations based on activity          |
| Search & Sort       | 🔍   | Find products quickly, sort by price/date               |
| Wishlist            | ❤️   | Add favorite items                                      |
| Rating & Comments   | 📝   | Provide feedback on products                            |
| OTP Purchase        | 🔐   | Secure product purchase verification                    |
| Notifications       | 📲   | Device notifications and tracking                       |
| Multilingual        | 🌐   | English 🇬🇧 and Arabic 🇸🇦                            |
| Payments            | 💳   | PayPal integration for website services                 |
| Analytics           | 📊   | Firebase analytics for product performance              |

> Every feature was carefully crafted to **showcase advanced web development skills**.

---

## 🛠 Tech Stack & Tools

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge\&logo=python\&logoColor=ffdd54)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge\&logo=django)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge\&logo=firebase)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge\&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge\&logo=sqlite)
![PayPal](https://img.shields.io/badge/PayPal-003087?style=for-the-badge\&logo=paypal)

* **Backend:** Python 🐍, Django 🌐
* **Database:** SQLite 🗄️
* **Frontend:** HTML5 📄, CSS3 🎨, JavaScript 💻
* **Storage & Analytics:** Firebase ⚡
* **Payments:** PayPal 💳
* **Version Control:** Git & GitHub 🏷️

---

## 📂 Project Structure

```text
ecom/
│
├── ecom/                      # Django project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── firebase/                   # Firebase configuration
│   └── firebase.json
│
├── shop/                       # Main Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── scripts.py               # Custom scripts
│   ├── image_cache/             # Cached product images
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   └── shop/
│   └── static/
│       └── shop/
│
├── staticfiles/                # Collected static files
├── db.sqlite3                   # Local database
└── manage.py                    # Django management script
```

> Includes **all default Django files** along with **custom scripts and image caching**.

---

## 💻 How to Run Locally

```bash
# Clone the repo
git clone <your-repo-link>
cd ecom

# Create virtual environment
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver

# Open in browser
http://127.0.0.1:8000
```

---

## 📸 Screenshots

## 👤 Authentication & Onboarding

* 🔐 Secure **Sign Up / Log In** with real-time **username availability check**
* ✨ Friendly **welcome & onboarding flow** for first-time users
* 📲 Personalized notifications & address selection during setup

<p align="center">
  <img src="https://i.imgur.com/2JP84AQ.png" width="250"/>
  <img src="https://i.imgur.com/PVInN21.png" width="250"/>
  <img src="https://i.imgur.com/eO7qd0h.png" width="250"/>
</p>

<p align="center">
  <img src="https://i.imgur.com/OkLBIYb.png" width="250"/>
  <img src="https://i.imgur.com/d126qKp.png" width="250"/>
  <img src="https://i.imgur.com/et9SsJT.png" width="250"/>
</p>

---

## 🏠 Homepage & Discovery

* 🎯 **Developer’s Pick** featured category
* 🌍 Full bilingual support: **English 🇬🇧** & **Arabic 🇸🇦**
* 🤖 **Smart suggestions** based on user activity
* 🔍 **Search & sorting** for seamless product discovery

<p align="center">
  <img src="https://i.imgur.com/I4P2Ryv.png" width="250"/>
  <img src="https://i.imgur.com/9ggEmFC.png" width="250"/>
  <img src="https://i.imgur.com/nI5TXrj.png" width="250"/>
</p>

<p align="center">
  <img src="https://i.imgur.com/tvCWjbB.png" width="250"/>
  <img src="https://i.imgur.com/OXdpeKJ.png" width="250"/>
  <img src="https://i.imgur.com/AZkmTBs.png" width="250"/>
  <img src="https://i.imgur.com/oMUWJ1J.png" width="250"/>
  <img src="https://i.imgur.com/YxiKzbQ.png" width="250"/>
</p>

---

## 🛍 Marketplace & Product Management

* 📦 **List products** with image cropping ✂️ and duration settings ⏱️
* 👁️ Hide/unhide or ❌ delete products anytime
* 📊 Sort by **price / date** for better visibility
* ❤️ Wishlist, ⭐ rate & 💬 comment on products
* 🔐 **OTP-secured checkout** with order history
* 🧾 Track purchased orders & sales performance

<p align="center">
  <img src="https://i.imgur.com/jnj41Om.png" width="250"/>
  <img src="https://i.imgur.com/mrLhNjt.png" width="250"/>
  <img src="https://i.imgur.com/Fb2dGZJ.png" width="250"/>
</p>

<p align="center">
  <img src="https://i.imgur.com/WEHW9o1.png" width="250"/>
  <img src="https://i.imgur.com/0fLsZbG.png" width="250"/>
  <img src="https://i.imgur.com/FAJflGk.png" width="250"/>
</p>

<p align="center">
  <img src="https://i.imgur.com/hFj5S7K.png" width="250"/>
  <img src="https://i.imgur.com/RMzhMED.png" width="250"/>
  <img src="https://i.imgur.com/I5AvK5v.png" width="250"/>
</p>

<p align="center">
  <img src="https://i.imgur.com/Q5jaSTR.png" width="250"/>
  <img src="https://i.imgur.com/ovxCuw3.png" width="250"/>
  <img src="https://i.imgur.com/6VaevD8.png" width="250"/>
</p>

<p align="center">
  <img src="https://i.imgur.com/SCA8NEG.png" width="500"/>
</p>

---

## 📢 Notifications & Communication

* 📲 **Real-time device notifications**
* 📨 Dedicated **notifications page**
* 👤 **Client details**: contact info, address, and custom messages
* ❤️ Easily view & manage **wishlisted items**

<p align="center">
  <img src="https://i.imgur.com/XhPqdcv.png" width="250"/>
  <img src="https://i.imgur.com/JFGPxb9.png" width="250"/>
  <img src="https://i.imgur.com/ALW74fQ.png" width="250"/>
</p>

---

## ⚙️ Account Settings & Admin Dashboard

* ✏️ Update **personal details** like email, address, etc.
* 📊 Track **ratings, purchases, and views** for performance insights
* 🔑 **Django Admin Dashboard** + Firebase integration for analytics

<p align="center">
  <img src="https://i.imgur.com/yw9OTtv.png" width="250"/>
  <img src="https://i.imgur.com/CJXSxOs.png" width="250"/>
  <img src="https://i.imgur.com/izPGGsC.png" width="250"/>
</p>

---

## 💳 Payments & Services

* 💳 Seamless **PayPal integration** for services
* 🔐 **OTP verification** for secure purchases

<p align="center">
  <img src="https://i.imgur.com/JViaB6o.png" width="300"/>
  <img src="https://i.imgur.com/UbsqMGT.png" width="300"/>
</p>

---

## 🏆 Skills Showcased

* Full-stack Django development
* Firebase integration (storage, analytics, auth)
* Payment gateway integration (PayPal)
* Responsive & multilingual UI/UX design
* Product management system with notifications
* OTP-secured transactions and authentication

---

## ✨ Final Words

**AcademiaMart** is a **professional-grade portfolio project**, showcasing:

* **2000+ lines of handcrafted code** 🖊️
* Full-stack **Django application** with advanced ecommerce features
* Multilingual support with clean, responsive, and modern **UI/UX design** 🌐
* Real-world features comparable to professional ecommerce platforms: notifications, developer-picked products, OTP-secured purchases
* **Portfolio-ready** to showcase technical and design skills

