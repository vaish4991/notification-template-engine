Multi-Language Notification Template Support
Objective
This project demonstrates a simple notification system that supports multiple languages based on the user's preferred locale.
Features
User model with locale support (en, hi, te)
Locale-specific notification templates
Placeholder replacement ({{name}}, {{date}}, {{time}})
English fallback for unsupported locales
Single notification trigger for multiple users
Project Structure
notification-project/
│
├── templates/
│   ├── en/
│   ├── hi/
│   └── te/
│
├── users.py
├── template_loader.py
├── notification_service.py
└── main.py
Run
python3 main.py