class User:
    """
    Represents a user who receives notifications.
    """

    SUPPORTED_LOCALES = {"en", "hi", "te"}

    def __init__(self, name, email, locale):

        # Validate name
        if not isinstance(name, str) or not name.strip():
            raise ValueError("User name cannot be empty.")

        # Validate email
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("Invalid email address.")

        # Validate locale
        if not isinstance(locale, str) or not locale.strip():
            raise ValueError("Locale cannot be empty.")

        self.name = name.strip()
        self.email = email.strip()

        # Unknown locales automatically fall back to English
        if locale not in self.SUPPORTED_LOCALES:
            self.locale = "en"
        else:
            self.locale = locale

    def __str__(self):
        return (
            f"User("
            f"name='{self.name}', "
            f"email='{self.email}', "
            f"locale='{self.locale}')"
        )