import os
# import re
# from nltk.downloader import download as nltk_download
# from nltk.corpus import words as nltk_words
from flake8.api import legacy as flake8
from radon import complexity, raw, metrics

import constants


class Elegance:
    # region Default Settings
    def __init__(self, ignore: list[str] = constants.IGNORE, max_line_length: int = constants.MAX_LINE_LENGTH):
        """
        Initializes dictionary and the style guide.
        """
        # nltk_download('words')
        # word_list = nltk_words.words()
        # self.word_set = set(word_list)
        self.style_guide = None
        self.set_style_guide(ignore, max_line_length)

    def set_style_guide(self,
                        ignore: list[str] = constants.IGNORE,
                        max_line_length: int = constants.MAX_LINE_LENGTH) -> None:
        """
        Resets the style guide.
        """
        self.style_guide = flake8.get_style_guide(ignore=ignore, max_line_length=max_line_length)
    # endregion

    # region PEP8 Violation Check
    def get_flake8_report(self, file_path: str = None) -> flake8.Report:
        """
        Checks the elegance of a file.

        :param file_path: str: file path
        :returns: flake8.api.legacy.Report
        """
        # set the file path to working directory if file path is None
        if file_path is None:
            file_path = os.getcwd()
        return self.style_guide.input_file(file_path)

    def get_PEP8_metrics(self, files: list[str], violation: str = '') -> list[list[str]]:
        """
        Returns the PEP8 violations of a list of code files.

        :param files: list of file paths
        :param violation: PEP8 violation to check (e.g. 'E', 'W', 'C')
        :returns: list[list[str]]
        """
        assert len(files) > 0, 'length of files must be greater than 0'
        reports = []
        for file in files:
            report = self.get_flake8_report(file)
            reports.append(report.get_statistics(violation))
        return reports
    # endregion

    # region Cyclomatic Complexity Check
    def get_cyclomatic_metrics(self, codes: list[str]) -> list[list[int]]:
        """
        Returns the cyclomatic complexities of a list of codes.

        :param codes: strings of raw code
        :returns: list[list[int]]
        """
        depths = []
        for code in codes:
            elements = complexity.cc_visit(code)
            depths.append([element.complexity for element in elements])
        return depths
    # endregion

    # region Halstead Metrics Check
    def get_halstead_metrics(self, codes: list[str]) -> list[list[float]]:
        """
        Returns the Halstead metrics of a list of codes.

        :param codes: strings of raw code
        :return: list[list[volume, difficulty, effort]]
        """
        halstead = []
        for code in codes:
            element = metrics.h_visit(code)
            halstead.append([element.total.volume, element.total.difficulty, element.total.effort])
        return halstead
    # endregion

    # region Raw Metrics Check
    def get_raw_metrics(self, codes: list[str]) -> list[list[int]]:
        """
        Returns the raw metrics of a list of codes.

        :param codes: strings of raw code
        :returns: list[list[int]]
        """
        raw_metrics = []
        for code in codes:
            analyzed = raw.analyze(code)
            raw_metrics.append([analyzed.loc, analyzed.sloc, analyzed.comments])
        return raw_metrics
    # endregion

    def get_mi_metrics(self, codes: list[str]) -> list[float]:
        """
        Returns the MI metrics of a list of codes.

        :param codes: strings of raw code
        :returns: list[float]
        """
        return [metrics.mi_visit(code, True) for code in codes]

    # region Name Check
    # def check_name_dictionary_word(self, word: str) -> bool:
    #     """
    #     Checks if a word is correct variable name.
    #
    #     :param word: str: variable name to check
    #     :returns: bool: True if the word is a correct variable name
    #     """
    #     assert len(word) > 0, 'length of word must be greater than 0'
    #     # dictionary word check
    #     if word not in self.word_set:
    #         return True
    #     else:
    #         return False
    #
    # def check_name_dictionary(self, words: list[str]) -> list[bool]:
    #     """
    #     Checks if a list of words are correct variable names.
    #
    #     :param words: list[str]: list of variable names to check
    #     :returns: list[bool]: True if the word is a correct variable name
    #     """
    #     return [self.check_name_dictionary_word(word) for word in words]
    #
    # def check_sequential_word(self, word: str) -> bool:
    #     """
    #     Checks if a word has triple consecutive characters.
    #
    #     :param word: str: variable name to check
    #     :returns: bool: True if the word has triple consecutive characters
    #     """
    #     return True if re.search(r'(.)\1\1', word) else False
    #
    # def check_sequential(self, words: list[str]) -> list[bool]:
    #     """
    #     Checks if a list of words have triple consecutive characters.
    #
    #     :param words: list[str]: list of variable names to check
    #     :returns: list[bool]: True if the word has triple consecutive characters
    #     """
    #     return [self.check_sequential_word(word) for word in words]
    #
    # def check_name_correctness(self, words: list[str]) -> list[bool]:
    #     """
    #     Checks if a list of words are correct variable names.
    #
    #     :param words: list[str]: list of variable names to check
    #     :returns: list[bool]: True if the word is a correct variable name
    #     """
    #     dictionary_check = self.check_name_dictionary(words)
    #     sequential_check = self.check_sequential(words)
    #     return [(dictionary | sequential) for dictionary, sequential in zip(dictionary_check, sequential_check)]
    # endregion
