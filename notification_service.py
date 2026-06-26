from template_loader import load_template
def send_notification(user, event, data):

    template = load_template(user.locale ,event)

    message = template.replace("{{name}}" , user.name)

    message = message.replace("{{date}}", data["date"])

    message = message.replace("{{time}}", data["time"])
    return message