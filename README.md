# 🏀 Meetup Clique

A comprehensive web-based management system for university basketball clubs, built with Django. This platform enables administrators to manage club activities while allowing students to discover, join, and participate in basketball events, training sessions, and tournaments.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [User Roles](#user-roles)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Models](#database-models)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## 🎯 Overview

Meetup Clique is a full-stack web application for the "Beranang Buckets" basketball club, designed to streamline basketball club management at the university level. The platform serves as a hub for prospective students interested in basketball to explore club activities while providing existing members with tools to organize meetups, track training schedules, and manage tournament participation.

**Development Context:** Web Application Development (WAD) Course Project  
**Target Audience:** University basketball clubs and student athletes  
**Primary Goal:** Promote basketball culture and facilitate student engagement

## ✨ Features

### 👥 Member Management
- Complete CRUD operations for member profiles
- Student registration and authentication
- Profile customization and management
- Member directory with search functionality

### 📅 Event Organization
- Create and manage basketball meetups
- Schedule training sessions
- Organize and track tournaments
- Event calendar with upcoming activities
- RSVP and attendance tracking

### 🏆 Tournament Management
- Tournament creation and bracket management
- Team registration and lineup management
- Match scheduling and results tracking
- Tournament history and statistics

### 👤 User Profile System
- Personalized user profiles
- Edit profile information
- View participation history
- Track personal statistics

### 🔐 Role-Based Access Control
- Admin dashboard for club management
- Student portal for self-service features
- Secure authentication and authorization
- Permission-based feature access

## 👥 User Roles

### Administrator
**Capabilities:**
- ✅ Manage all club members
- ✅ Create and manage events (meetups, training, tournaments)
- ✅ Approve or reject member registrations
- ✅ View comprehensive club statistics
- ✅ Manage club announcements and updates
- ✅ Full CRUD operations on all resources

### Student/Member
**Capabilities:**
- ✅ Register and create personal profile
- ✅ View upcoming events and activities
- ✅ Create and join meetups
- ✅ Register for training sessions
- ✅ Sign up for tournaments
- ✅ Update own profile information
- ✅ View club information and history

## 📸 Screenshots

### Landing Page
*Showcase of club activities and upcoming events*

### Member Dashboard
*Personalized dashboard with profile and event management*

### Event Calendar
*Interactive calendar displaying all club activities*

> **Note:** Screenshots will be added soon. The application features a clean, responsive design optimized for both desktop and mobile devices.

## 🛠️ Technologies Used

### Backend
- **Django 4.x** - High-level Python web framework
- **Python 3.x** - Core programming language
- **SQLite** - Lightweight database for development
- **Django ORM** - Object-Relational Mapping for database operations

### Frontend
- **HTML5** - Structure and semantics
- **CSS3** - Styling and responsive design

### Development Tools
- **Django Admin** - Built-in administration interface
- **Django Authentication** - User authentication system

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Setup Instructions

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd meetup_clique
```

2. **Create a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install Django:
```bash
pip install django
```

4. **Run database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser (admin account)**
```bash
python manage.py createsuperuser
```
Follow the prompts to set username, email, and password.

6. **Run the development server**
```bash
python manage.py runserver
```

7. **Access the application**
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## 🚀 Usage

### For Administrators

1. **Log in to Admin Panel**
   - Navigate to `/admin/`
   - Use superuser credentials

2. **Manage Members**
   - Add new members manually
   - Approve pending registrations
   - Edit or remove member profiles

3. **Create Events**
   - Add new meetups, training sessions, or tournaments
   - Set dates, times, and locations
   - Manage event participants

4. **Monitor Activity**
   - View club statistics
   - Track event attendance
   - Generate reports

### For Students/Members

1. **Register an Account**
   - Click "Register" on homepage
   - Fill in required information
   - Submit for approval (if required)

2. **Browse Events**
   - View upcoming meetups and training
   - Check tournament schedules
   - See event details

3. **Manage Profile**
   - Update personal information
   - View participation history
   - Track statistics

4. **Create Meetups**
   - Schedule casual basketball sessions
   - Invite other members
   - Coordinate location and time

## 📁 Project Structure

```
meetup_clique/
├── basketball_club/           # Main Django app
│   ├── migrations/           # Database migrations
│   ├── static/              # Static files (CSS, JS, images)
│   ├── templates/           # HTML templates
│   ├── admin.py            # Admin interface configuration
│   ├── models.py           # Database models
│   ├── views.py            # View functions/classes
│   ├── urls.py             # URL routing
│   └── apps.py             # App configuration
├── meetup_clique/           # Django project settings
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── manage.py               # Django management script
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

## 🗄️ Database Models

### Key Models

**Students Model**
- `studentid` (CharField, primary_key)
- `nomonjersey` (CharField)
- `studentname` (TextField)
- `semester` (IntegerField)
- `phonenumber` (CharField)
- `email` (CharField)
- `password` (CharField)

**Lecturers Model**
- `lecturerid` (CharField, primary_key)
- `lecturername` (TextField)
- `lecturernumber` (CharField)
- `lectureremail` (CharField)
- `lecturerpasword` (CharField)

**Meetups Model**
- `M_title` (CharField)
- `M_description` (TextField)
- `M_date` (DateField)
- `M_time` (TimeField)
- `M_location` (TextField)

**Tournament Model**
- `tittle` (CharField)
- `date` (DateField)
- `time` (TimeField)
- `location` (CharField)

> **Note:** See `basketball_club/models.py` for the detailed schema.

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- ✅ Full-stack web development with Django
- ✅ MVC (Model-View-Controller) architecture
- ✅ Database design and ORM operations
- ✅ User authentication and authorization
- ✅ CRUD operations implementation
- ✅ RESTful routing principles
- ✅ Responsive web design
- ✅ Form handling and validation
- ✅ Admin interface customization

## 🚧 Future Enhancements

Potential features for future development:
- [ ] Email notifications for event updates
- [ ] Real-time chat for team coordination
- [ ] Mobile app version (React Native/Flutter)
- [ ] Integration with university student portal
- [ ] Advanced statistics and analytics dashboard
- [ ] Payment integration for tournament fees
- [ ] Social media sharing capabilities
- [ ] Player performance tracking
- [ ] Team formation and management system
- [ ] Live score updates during tournaments

## 👨‍💻 Developer

**Naqib Hazian**
- GitHub: [@naqibhazian](https://github.com/naqibhazian)
- LinkedIn: [Naqib Hazian](https://linkedin.com/in/naqibhazian)

## 📄 License

This project is licensed under the MIT License - feel free to use it for learning purposes.

## 🙏 Acknowledgments

- **Web Application Development Course** - Project foundation and guidance
- **Django Documentation** - Comprehensive framework reference
- **University Basketball Club** - Inspiration and use case validation

---

⭐ **Promoting basketball culture and student engagement through technology!** 🏀

*Built to help prospective students discover basketball opportunities and streamline club management.*