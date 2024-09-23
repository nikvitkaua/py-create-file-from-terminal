import sys
import os
from datetime import datetime


def create_file() -> None:
    try:
        user_input = sys.argv

        if "-d" in user_input:
            key_dir_index = user_input.index("-d")
            key_file_index = user_input.index("-f")
            path_way = "/".join(user_input[key_dir_index + 1 : key_file_index])
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
                        file.write("\n")
                        asking_user = False
                        break

                    file.write(new_line + "\n")
    except ValueError as e:
        return f"Error: {e}"


if __name__ == "__main__":
    create_file()
