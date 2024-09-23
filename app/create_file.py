import sys
import os
from datetime import datetime


class OrderError(Exception):
    """Raise when order of command is incorrect"""


def create_file() -> None:
    try:
        user_input = sys.argv

        if "-d" in user_input and "-f" in user_input:
            if user_input.index("-d") > user_input.index("-f"):
                raise OrderError(
                    "Command must be like:"
                    "'python create_file.py"
                    "-d {dir_name or path} -f {file_name}'"
                )

        if "-d" in user_input:
            key_dir_index = user_input.index("-d")
            path_way = user_input[key_dir_index + 1]
            os.makedirs(path_way, exist_ok=True)
            os.chdir(path_way)

        if "-f" in user_input:
            key_file_index = user_input.index("-f")
            file_name = user_input[key_file_index + 1]

            with open(file_name, "a") as file:
                file.write(datetime.now().strftime("%m-%d-%Y %H:%M:%S") + "\n")

                asking_user = True

                while asking_user:
                    new_line = input("Enter content line: ")

                    if new_line == "stop":
                        asking_user = False
                        break

                    file.write(new_line + "\n")
    except ValueError as e:
        return f"Error: {e}"


if __name__ == "__main__":
    create_file()
