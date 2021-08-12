from typing import List, Optional


class TextFile:
    """ An instance that contains information about the text file to check plagiarism


    === Private Attributes ===
    _num_lines: Total number of lines that the text file contains.
    _curr_line: The line of the text file that the program is currently pointing at.
    _curr_ind: The index of _curr_line attribute.
    _all_lines: A list of every line in the text file in order.
    """
    _num_lines: int
    _curr_line: Optional[str]
    _curr_ind: Optional[int]
    _all_lines: List[str]

    def __init__(self, lines_lst: List[str]) -> None:
        """ Initialize an instance that contains information about the text file passed to lines_lst as
        list of strings."""
        self._num_lines = len(lines_lst)
        self._all_lines = lines_lst
        if len(lines_lst) == 0:
            self._curr_line, self._curr_ind = None, None
        else:
            self._curr_line, self._curr_ind = lines_lst[0], 0

    # === getters ===

    def get_num_lines(self) -> int:
        """ Returns the total number of lines that the text file contains
        """
        return self._num_lines

    def get_all_lines(self) -> List[str]:
        """ Returns a list of every line in the text file in order.
        """
        return self._all_lines

    def get_curr_line(self) -> Optional[str]:
        """ Returns the line of the text file that the program is currently pointing at.
        """
        return self._curr_line

    def get_curr_index(self) -> Optional[int]:
        """ Returns the index of _curr_line attribute.
        """
        return self._curr_ind

    def next_line(self) -> None:
        """ Update _curr_line and _curr_ind with the next line in order and its index.

        If the text file contains no contents, this function does not do anything.

        If the text file reached the last line, it goes back to the first line."""
        curr_ind = self._curr_ind
        if curr_ind is not None:
            curr_ind += 1
            if curr_ind >= len(self._all_lines):
                curr_ind = 0
            self._curr_ind = curr_ind
            self._curr_line = self._all_lines[curr_ind]

