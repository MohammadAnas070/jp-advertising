# JP Advertising

<p align="center">
  <img src="https://static.djangoproject.com/img/logos/django-logo-negative.svg" alt="Django Logo" width="200"/>
</p>

![JP Advertising Screenshot](project-screenshot.png)  
*An online advertising platform for efficient ad postings and management.*

---

## 🛠 Technologies Used
- **Frontend:** HTML, CSS, Bootstrap  
- **Backend:** Django (Python Framework)  
- **Database:** MySQL / SQLite  
- **Tools:** VS Code, Postman, Git  

---

## ✨ Features
- Responsive and user-friendly UI  
- Role-based access for **Admin**, **Agency**, and **User**  
- Secure login & registration  
- Ad posting and management system  
- Admin control for content moderation and blocking users  

---

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/MohammadAnas070/jp-advertising.git
cd jp-advertising
Create and activate virtual environment
```
2.Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies
```bash
pip install django, xhtml2pdf, mysqlclient
```

4.Apply migrations
```bash
python manage.py migrate
```

5.Create superuser
```bash
python manage.py createsuperuser
```
6.Run the server
```bash
python manage.py runserver
```

```
jp-advertising/
│
├── jp_advertising/       # Main project settings
├── apps/                 # Django apps (modules)
├── templates/            # HTML templates
├── static/               # Static files (CSS, JS, Images)
├── media/                # Uploaded media files
├── manage.py             # Django management script
├── requirements.txt      # Project dependencies
└── README.md             # Documentation
```

📄 License
This project is licensed under the MIT License.

