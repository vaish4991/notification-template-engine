import logging
import re

from template_loader import load_template


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def render_template(template, values):
    """
    Replaces placeholders dynamically.
    Raises an error if any required placeholder value is missing.
    """

    placeholders = re.findall(r"\{\{(.*?)\}\}", template)

    for placeholder in placeholders:

        key = placeholder.strip()

        if key not in values:
            raise KeyError(
                f"Missing value for placeholder '{key}'."
            )

        template = template.replace(
            "{{" + key + "}}",
            str(values[key])
        )

    return template


def send_notification(user, event, data):
    """
    Generates a localized notification.
    """

    if user is None:
        raise ValueError("User cannot be None.")

    if not isinstance(data, dict):
        raise ValueError("Notification data must be a dictionary.")

    template = load_template(
        user.locale,
        event
    )

    values = {
        "name": user.name,
        "date": data.get("date"),
        "time": data.get("time")
    }

    if values["date"] is None:
        raise ValueError("Date is required.")

    if values["time"] is None:
        raise ValueError("Time is required.")

    message = render_template(
        template,
        values
    )

    logging.info(
        f"Notification generated for {user.name}"
    )

    return message