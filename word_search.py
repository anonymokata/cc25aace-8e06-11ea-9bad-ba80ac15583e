import os
import sys

class WordSearchProblem:
    def __init__(self, file_path = "text_files/input.txt"):
        self.puzzle = []
        self.word_list = []
        self.__parse_file(file_path)
    
    def get_puzzle(self):
        return self.puzzle
    
    def get_word_list(self):
        return self.word_list

    def __parse_file(self, file_path):
        if self.__is_file_path_valid(file_path) and not self.__is_file_empty(file_path):
            with open(file_path, "r") as file_obj:
                self.__generate_word_list(file_obj.readline())
                self.__generate_puzzle(file_obj)  
        else:
            sys.exit()

    def __is_file_path_valid(self, file_path):
        if not os.path.isfile(file_path):
            raise ValueError("FILE DOES NOT EXIST")
        
        return True
    
    def __is_file_empty(self, file_path):
        if os.path.getsize(file_path) == 0:
            raise ValueError("FILE IS EMPTY")

        return False
    
    def __generate_word_list(self, line):
        for word in line.strip().split(","):
            if word not in self.word_list:
                self.word_list.append(word)

        self.word_list.sort()

    def __generate_puzzle(self, file_obj):
        for line in file_obj:
            self.puzzle.append(line.strip().split(","))