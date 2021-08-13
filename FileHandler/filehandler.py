from typing import List
from FileHandler.textfile import TextFile


def handle(file: str) -> TextFile:
    """
    :param file:
    A string that represents a name or a location of the text file.
    :return:
    A TextFile instance that contains information about the text file. Refer
    textfile.py for information about class TextFile.

    Returns a TextFile instance by taking a file name or a route as a string
    object
    """
    try:
        opened_file = open(file, "r")
        lines_lst = opened_file.read().splitlines()
        opened_file.close()
        text_instance = TextFile(lines_lst)
        return text_instance
    except OSError:
        print("Cannot open: " + file)

# def calculate_percentage(file: TextFile, search_res: List[str]):
    """
    1. Split the result list elements into single words.
    2. Compare word to word at each index of TextFile._all_lines and search
       result.
    3. Divide the total number of words (whichever less) by the number of 
       matching
    4. Multiply that number with 100 and return.
    """


if __name__ == '__main__':
    test = handle("../test.txt")
    print(test.get_all_lines())
