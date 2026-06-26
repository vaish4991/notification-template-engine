import os
def load_template(locale,event):

    file_path = os.path.join(
        "templates",
        locale,
        f"{event}.txt"

    )

    if not os.path.exists(file_path):

        file_path=os.path.join(
            "templates",
            "en",
            f"{event}.txt"
        )

    with open(file_path, "r" ,encoding="UTF-8") as file:
        return file.read()