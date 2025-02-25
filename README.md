# DRF Authentication System

🚧 **Project Status:** In Development 🚧

## 📌 Overview
DRF Authentication System is a Django Rest Framework (DRF)-based authentication system that provides secure user registration, login, email verification, password reset, and JWT authentication.

## 🛠️ Features
- User registration with email and password
- Email verification with activation code
- JWT-based authentication (login/logout)
- Password reset functionality
- Rate limiting to prevent abuse
- API documentation using Swagger

## 🏗️ Technologies Used
- Python 3
- Django Rest Framework (DRF)
- Simple JWT for authentication
- PostgreSQL (planned for production)
- Docker (planned for deployment)

## 📂 Project Structure
```
DRF_Authentication_System/
│-- authentication/         # Authentication app
│   ├── models.py           # User and Activation models
│   ├── serializers.py      # API serializers
│   ├── views.py            # API views
│   ├── urls.py             # API endpoints
│-- auth_system/            # Main Django project
│-- requirements.txt        # Dependencies
│-- README.md               # Project documentation
```

## 🚀 Installation & Setup
1. Clone the repository:
   ```sh
   https://github.com/mahmoudshaker123/DRF_Authentication_System.git
   cd DRF_Authentication_System
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run the development server:
   ```sh
   python manage.py runserver
   ```

## 📌 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Authenticate user and get JWT |
| POST | `/api/auth/logout/` | Logout and invalidate JWT |
| POST | `/api/auth/verify-email/` | Verify user email |
| POST | `/api/auth/password-reset/` | Send password reset email |
| POST | `/api/auth/password-reset/confirm/` | Reset password |

## 📝 TODO
- [ ] Implement email verification
- [ ] Deploy to Fly.io
- [ ] Add Docker support
- [ ] Write unit tests

## 📜 License
This project is licensed under the MIT License.

---
💡 **Contributors:** Feel free to open issues and submit pull requests!

