import os
from os.path import join, isdir

matches = []  # this variable will contain list of paths containing our file.


def file_search(root: str, filename: str) -> None:
    """
    :param root: The path to search in
    :param filename: the filename to search for
    :return: None
    """
    print('Searching in:', root)
    for file in os.listdir(root):
        full_path = join(root, file)  # concatenate root with file
        if filename in file:
            matches.append(full_path)
        if isdir(full_path):
            file_search(full_path, filename)


def main():
    file_search('C:\\Users\\Tayebe Rafiei\\PycharmProjects', 'main')
    for m in matches:
        print('Matched:', m)


if __name__ == '__main__':
    main()

