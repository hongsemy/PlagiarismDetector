from textfile import TextFile


def handle(file: str) -> TextFile:
    """
    :param file:
    A string that represents a name or a location of the text file.
    :return:
    A TextFile instance that contains information about the text file. Refer textfile.py for
    information about class TextFile.

    Returns a TextFile instance by taking a file name or a route as a string object
    """
    try:
        opened_file = open(file, "r")
        lines_lst = opened_file.readlines()
        opened_file.close()
        text_instance = TextFile(lines_lst)
        return text_instance
    except OSError:
        print("Cannot open: " + file)
