import os


def search_in_url(text):
    for directory in os.listdir("/home/kapil/PycharmProjects/incrowler"):
        if os.path.isdir(directory):
            if not directory == "__pycache__":
                if not directory == ".git":
                    if not directory == ".idea":
                        print(directory)
                        with open(directory + "/crawled.txt") as file:
                            for _ in enumerate(file):
                                line = file.readline().lower()
                                if text in line:
                                    print(line)

search_term = input("enter word to be search.. ")
search_in_url(search_term)
