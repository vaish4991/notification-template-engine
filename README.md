# Multi-Language Template Support

## Project Overview

This project implements a locale-aware notification template system in Python. It supports rendering notifications in the user's preferred language by loading language-specific templates.

The implementation supports the following locales:

- English (`en`)
- Hindi (`hi`)
- Telugu (`te`)

The same notification is rendered in different languages using a single notification trigger.

---

## Objective

The objective of this project is to support global users by delivering notifications in their preferred language.

The implementation includes:

- Addition of a `locale` field in the User model.
- Loading of locale-specific notification templates.
- Dynamic replacement of template placeholders.
- English fallback when an unsupported locale is requested.

---

## Features

- Locale-specific template loading
- User model with locale support
- Dynamic placeholder replacement
- English fallback mechanism
- Modular project structure
- Single notification trigger for multiple users

---

## Project Structure

```
notification-project/
│
├── templates/
│   ├── en/
│   │   └── interview_scheduled.txt
│   ├── hi/
│   │   └── interview_scheduled.txt
│   └── te/
│       └── interview_scheduled.txt
│
├── users.py
├── template_loader.py
├── notification_service.py
├── main.py
└── README.md
```

---

## Technologies Used

- Python 3
- VS Code
- Python os module

---

## Implementation

### User Model

The `User` class stores user information including:

- Name
- Email
- Preferred Locale

Example:

```python
User("Vaishnavi", "vaish@gmail.com", "en")
```

---

### Template Loader

The template loader performs the following operations:

1. Reads the user's locale.
2. Loads the corresponding template.
3. Falls back to the English template if the requested locale is unavailable.

Example:

```
templates/en/interview_scheduled.txt
templates/hi/interview_scheduled.txt
templates/te/interview_scheduled.txt
```

---

### Notification Service

The notification service:

- Loads the template.
- Replaces placeholders with actual values.
- Returns the final notification.

Example:

```python
template = load_template(user.locale, event)

message = template.replace("{{name}}", user.name)
message = message.replace("{{date}}", data["date"])
message = message.replace("{{time}}", data["time"])

return message
```

---

## Running the Project

Navigate to the project directory.

Run:

```bash
python3 main.py
```

---

## Sample Output

### English

```
Notification for Vaishnavi

Hello Vaishnavi,

Your interview has been scheduled.

Date: 10 July

Time: 5 PM

Thank you,
Interview Team
```

### Hindi

```
Notification for Jaya

नमस्ते Jaya,

आपका इंटरव्यू निर्धारित किया गया है।

दिनांक: 10 July

समय: 5 PM

धन्यवाद,
इंटरव्यू टीम
```

### Telugu

```
Notification for Anushka

హలో Anushka,

మీ ఇంటర్వ్యూ షెడ్యూల్ చేయబడింది.

తేదీ: 10 July

సమయం: 5 PM

ధన్యవాదాలు,
ఇంటర్వ్యూ టీమ్
```

---

## Testing

The following scenarios were tested successfully:

- English notification rendering
- Hindi notification rendering
- Telugu notification rendering
- Placeholder replacement
- English fallback for unsupported locales

---

## Future Scope

The current implementation can be extended to support:

- Additional languages
- Email notifications
- SMS notifications
- Database-driven template storage
- REST API integration
- HTML notification templates

---

## Author

Vaishnavi Jagdale

Internship Task

Multi-Language Template Support
