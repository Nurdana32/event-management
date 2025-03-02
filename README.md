# Event Management  

## 🚀 Overview  
Event Management API is a RESTful service for managing events, sessions, attendees, and tracks.  

## 🔧 Technologies  
- **Django 5.0+**  
- **Django REST Framework**  
- **PostgreSQL**  
- **JWT Authentication**  

## 📌 Features  
### ✅ Event Management  
- CRUD (Create, Read, Update, Delete) operations for events  
- Event capacity management  

### ✅ Session Management  
- Schedule sessions within an event  
- Prevent overlapping session schedules in a track  

### ✅ Attendee Registration  
- Register attendees for an event  
- Prevent overbooking  

### ✅ Track Management  
- Group sessions into tracks  

---

## 🛠 Installation  

### **Prerequisites**  
- Python 3.x  
- PostgreSQL  

## 🛠 Installation  

1. **Clone the repository and enter the project folder**  
   ```bash
   git clone https://github.com/nurdana32/event-management-api.git
   cd event-management
2. **Apply database migrations**  
   ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
   
3. **Create a superuser (optional)**  
   ```bash
   python3 manage.py createsuperuser
   
4. **Start the development server**  
   ```bash
   python manage.py runserver

🚀 Future Enhancements <br />
  -Docker Support 🐳


📖 **API Documentation**
 
 You can use **postman collection and environments** at this repository or akses:
   ```bash
  http://localhost:8000/api/docs/



