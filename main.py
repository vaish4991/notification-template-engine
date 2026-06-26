from users import User
from notification_service import send_notification
users =[

    User(
        "Vaishnavi",
        "vaish@gmail.com",
        "en"
    ),

    User(
        "Jaya",
        "jaya1@gmail.com",
        "hi"
    ),

    User(
        "Anushka",
        "anushka3@gmail.com",
         "te"    
    )

]

event = "interview_scheduled"

data = {

    "date" : "10 July",

    "time" : "5 PM"
}

for user in users:
    message = send_notification(
        user,
        event,
        data
    )

    print("=" * 40)
    print(f"Notification for {user.name}")
    print(message)
