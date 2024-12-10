# 📚 Discere: Interactive Learning Web App

**Discere** is a modern web application designed to make studying 📖 interactive, efficient, and fun. With customizable flashcards, study sets, and quizzes, it helps students and lifelong learners achieve their educational goals. 🎯

---

## ✨ Features

### 🔐 User Management
- **User Registration**: Sign up with an email and password to access the app's features.
- **User Login**: Secure authentication using registered credentials.
- **Password Recovery**: Easily reset your password via email.

### 📝 Flashcard Creation and Management
- **Create Flashcards**: Quickly create terms and definitions to aid learning.
- **Edit Flashcards**: Modify existing flashcards for updates or corrections.
- **Delete Flashcards**: Remove unwanted or outdated flashcards.

### 📂 Deck Organization
- **Create Decks**: Organize flashcards by subject or category.
- **Edit Decks**: Update deck titles or descriptions as needed.
- **Delete Decks**: Remove decks for streamlined organization.

### 🔄 Study Mode
- **Review Flashcards**: Flip flashcards to reveal answers.
- **Shuffle Flashcards**: Randomize the order of flashcards for variety.

### 🧠 Quiz Mode
- **Generate Quizzes**: Create quizzes based on selected flashcards.
- **Multiple-Choice and Fill-in-the-Blank Questions**: Choose from different quiz formats.
- **View Results**: Get feedback on quiz performance, including correct/incorrect answers and scores.

### 📈 Progress Tracking
- **User Profile**: View and update your account details.
- **Performance Tracking**: Monitor progress such as:
  - Flashcards reviewed
  - Quizzes taken
  - Average scores

---

## 🛠️ Tech Stack

- **Frontend**:
  - ![HTML](https://img.shields.io/badge/-HTML5-orange?logo=html5&logoColor=white) ![CSS](https://img.shields.io/badge/-CSS3-blue?logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/-JavaScript-yellow?logo=javascript&logoColor=white)
- **Backend**:
  - ![Python](https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white) ![Django](https://img.shields.io/badge/-Django-green?logo=django&logoColor=white)
- **Database**:
  - ![SQLite](https://img.shields.io/badge/-SQLite-lightblue?logo=sqlite&logoColor=white)
- **Version Control**:
  - ![Git](https://img.shields.io/badge/-Git-orange?logo=git&logoColor=white)

---
## 📂 Resources

### Gantt Chart
- [Resources/Project Discere_Gantt Chart.xlsx](./Resources/Project%20Discere_Gantt%20Chart.xlsx)

### ERD
- ![ERD_Project Discere](https://github.com/user-attachments/assets/cbb6a30c-1098-437a-bf54-14c20dfb2731)


### UI/UX Design - Figma
- [Resources/Figma Compilation](./Resources/Figma%20Compilation/)

---

## 🚀 Installation and Setup

### Prerequisites
- 🐍 Python (version 3.8 or later)
- 📦 SQLite (pre-installed with Python)
- 🖥️ Git

### Steps to Run Locally

1. **📥 Clone the Repository**
   ```bash
   git clone https://github.com/y4na/Discere.git
   cd discere
2. **🌐 Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **📦 Install Dependencies**
   ```bash
   pip install -r requirements.txt
4. **🛠️ Run Database Migrations**
   ```bash
   python manage.py migrate
5. **▶️ Start the Development Server**
   ```bash
   python manage.py runserver
6. **🌟 Access the Application**
   ```bash
   Open your browser and navigate to: http://127.0.0.1:8000/.

---

## 🎯 Future Features (Planned)
- 🌙 **Dark Mode**: A toggleable dark theme for better accessibility and reduced eye strain.
- 🤝 **Collaborative Decks**: Enable multiple users to collaborate on shared decks in real-time.
- 📱 **Mobile App Integration**: Extend Discere's functionality to iOS and Android platforms for on-the-go learning.
- 🏆 **Gamification**: Introduce badges, rewards, and progress milestones to motivate users.
- 🌐 **Multilingual Support**: Add support for multiple languages to make Discere accessible worldwide.
- 📊 **Advanced Analytics**: Provide detailed performance reports, trends, and recommendations based on user activity.

---

## 📜 License

This project is licensed under the **MIT License**. 📝  
You are free to use, modify, and distribute this software as long as proper attribution is given.  
See the [LICENSE](LICENSE) file for more details.

---

## 🏆 Credits

- **👨‍💻 Developers**:
  <table style="border: none">
    <tr>
      <td align="center">
        <img src="https://scontent.fceb8-1.fna.fbcdn.net/v/t39.30808-6/350920215_1199430287400023_3206461578258133432_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeEgm1uDl50hb2Y4uW-fKdV7ib4jCcAYUKOJviMJwBhQo_RJyAFjf_7Vldi3--N-3KBgFP9y-lX3vVPK5hz1aLDs&_nc_ohc=X65VHjnkNZ0Q7kNvgHGRCVH&_nc_zt=23&_nc_ht=scontent.fceb8-1.fna&_nc_gid=AxKgiVIdfQQjTZShrV32McY&oh=00_AYBY8LdMnaZot3lIWETr3QLNh_OztuWj1VvbmDkYgpiItw&oe=675D9AFB" width="100px;" alt="Brix C. Bitayo"/><br />
        <sub><b><a href="https://github.com/satorime" target="_blank">Brix C. Bitayo</a></b></sub>
      </td>
      <td align="center">
        <img src="https://scontent.fceb8-1.fna.fbcdn.net/v/t39.30808-6/447281557_7414729571970537_809916978661235860_n.jpg?stp=cp6_dst-jpg_tt6&_nc_cat=106&ccb=1-7&_nc_sid=6ee11a&_nc_eui2=AeFiJy-rxS-aCrEWvlT0XaJwftv8jVjegCp-2_yNWN6AKs5rpau2wKAPY93Hugdnu3ecy450yRpkU8PnuKnYJGza&_nc_ohc=o_nDnq2BiOUQ7kNvgHVHoNN&_nc_zt=23&_nc_ht=scontent.fceb8-1.fna&_nc_gid=AHtqSgC32IFRICLEZYT7Q5O&oh=00_AYCmmlvb8NxsFAi6ttKNO45DFbJvCDgtuCNufhhGUXNVBg&oe=675D8283" width="100px;" alt="Jake R. Clarin"/><br />
        <sub><b><a href="https://github.com/Ariase26" target="_blank">Jake R. Clarin</a></b></sub>
      </td>
      <td align="center">
        <img src="https://scontent.fceb8-1.fna.fbcdn.net/v/t39.30808-1/447292533_7811653475540068_4928920792056669158_n.jpg?stp=dst-jpg_s200x200_tt6&_nc_cat=108&ccb=1-7&_nc_sid=0ecb9b&_nc_eui2=AeED-ie3lkAVILEj9pBMMXv250pAGofbKDnnSkAah9soOeOeu782AgtFIPSpRCi_y4XZCoZcwq2W_7W1jwlGUuko&_nc_ohc=8ARGPPsgGe8Q7kNvgE-XEX_&_nc_zt=24&_nc_ht=scontent.fceb8-1.fna&_nc_gid=ARPIYS79VkyyM19lwwUYucq&oh=00_AYA8iwEPH8oeB_vBYeb3pmb8Fe3K2_loRxn8nBk0VWvHTA&oe=675D987B" width="100px;" alt="Yllana Mikhaila B. Paragoso"/><br />
        <sub><b><a href="https://github.com/y4na" target="_blank">Yllana Mikhaila B. Paragoso</a></b></sub>
      </td>
    </tr>
  </table>

- **🎨 Design Inspiration**: Inspired by the need for modern, interactive learning tools.  
- **📢 Acknowledgments**: Special thanks to the open-source community for their contributions to the tech stack.

---

### 🌟 Let's Make Learning Fun Together!

We believe that education should be engaging and accessible to everyone! 🎓  
If you have suggestions, ideas, or feedback, feel free to:  
- Submit an issue under the **Issues** tab 📋  
- Create a pull request with your proposed changes 🌱  

Together, we can enhance **Discere** and empower learners worldwide! 🌍🚀

