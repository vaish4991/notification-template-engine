import os
import logging
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# Supported placeholders
VALID_PLACEHOLDERS = {
    "{{name}}",
    "{{date}}",
    "{{time}}"
}


def validate_template(template):
    """
    Validate template content.
    """

    # Empty template
    if not template.strip():
        raise ValueError("Template is empty.")

    # Find placeholders
    placeholders = set(
        re.findall(r"\{\{.*?\}\}", template)
    )

    # Invalid placeholder detection
    invalid = placeholders - VALID_PLACEHOLDERS

    if invalid:
        raise ValueError(
            f"Invalid placeholders found: {invalid}"
        )

    return True


def load_template(locale, event):
    """
    Loads the notification template.
    Falls back to English if locale does not exist.
    """

    if not event or not isinstance(event, str):
        raise ValueError("Invalid event name.")

    file_path = os.path.join(
        "templates",
        locale,
        f"{event}.txt"
    )

    # Locale fallback
    if not os.path.exists(file_path):

        logging.warning(
            f"Locale '{locale}' not found. Falling back to English."
        )

        file_path = os.path.join(
            "templates",
            "en",
            f"{event}.txt"
        )

    # Event validation
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Template not found for event '{event}'."
        )

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            template = file.read()

    except OSError as e:

        logging.error(
            f"Unable to read template: {e}"
        )
        raise

    # Validate template
    validate_template(template)

    logging.info(
        f"Loaded template: {file_path}"
    )

    return template