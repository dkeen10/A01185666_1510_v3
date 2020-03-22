# regex: (?<=(\s))the(?=[\s\W$])


def open_file(file_name):
    return open(file_name)


def count_words(file_name):
    current_file = open_file(file_name)
    with current_file as file_object:
        content = file_object.read()
        print(content)


def top_ten_words(file_name):
    count_words(file_name)


def main():
    files = ["little_women.py", "moby_dick.py", ""]
    top_ten_words(files[1])


if __name__ == "__main__":
    main()
