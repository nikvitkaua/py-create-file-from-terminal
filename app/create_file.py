import sys
import os
from datetime import datetime


def create_file() -> None:
    user_input = sys.argv

    for key in user_input:
        if key == "-d":
            key_index = user_input.index(key)
            path_way = user_input[key_index + 1]

            os.makedirs(path_way, exist_ok=True)
            os.chdir(path_way)
        elif key == "-f":
            key_index = user_input.index(key)
            file_name = user_input[key_index + 1]

            with open(file_name, "w") as file:
                file.write(datetime.now().strftime("%m-%d-%Y %H:%M:%S") + "\n")

                asking_user = True

                while asking_user:
                    new_line = input("Enter content line: ")

                    if new_line == "stop":
                        asking_user = False
                        break

                    file.write(new_line + "\n")


if __name__ == "__main__":
    create_file()
