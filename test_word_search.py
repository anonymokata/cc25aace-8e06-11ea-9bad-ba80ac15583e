import unittest
from word_search import WordSearchProblem

class TestWordSearchProblemCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_invalid_file_path_error_thrown(self):
        with self.assertRaisesRegex(ValueError, "FILE DOES NOT EXIST"): 
            WordSearchProblem("text_files/imaginary_file.txt")

    def test_empty_file_error_thrown(self):
        with self.assertRaisesRegex(ValueError, "FILE IS EMPTY"): 
            WordSearchProblem('text_files/empty_file.txt')
    
    def test_word_map_generator_maps_all_search_words(self):
        problem = WordSearchProblem('text_files/input.txt')
        word_map = problem.get_word_list()
        expected_result = ['BONES','KHAN','KIRK','SCOTTY','SPOCK','SULU','UHURA']

        self.assertEqual(word_map, expected_result)
    
    def test_word_map_generator_maps_all_search_words_once(self):
        problem = WordSearchProblem('text_files/duplicate_words.txt')
        word_map = problem.get_word_list()
        expected_result = ['BONES','KHAN','KIRK','SCOTTY','SPOCK','SULU','UHURA']

        self.assertEqual(word_map, expected_result)
    
    def test_puzzle_generator_gets_all_letters(self):
        problem = WordSearchProblem("text_files/input.txt")
        puzzle = problem.get_puzzle()
        expected_result = [
                            ['U', 'M', 'K', 'H', 'U', 'L', 'K', 'I', 'N', 'V', 'J', 'O', 'C', 'W', 'E'],
                            ['L', 'L', 'S', 'H', 'K', 'Z', 'Z', 'W', 'Z', 'C', 'G', 'J', 'U', 'Y', 'G'],
                            ['H', 'S', 'U', 'P', 'J', 'P', 'R', 'J', 'D', 'H', 'S', 'B', 'X', 'T', 'G'],
                            ['B', 'R', 'J', 'S', 'O', 'E', 'Q', 'E', 'T', 'I', 'K', 'K', 'G', 'L', 'E'],
                            ['A', 'Y', 'O', 'A', 'G', 'C', 'I', 'R', 'D', 'Q', 'H', 'R', 'T', 'C', 'D'],
                            ['S', 'C', 'O', 'T', 'T', 'Y', 'K', 'Z', 'R', 'E', 'P', 'P', 'X', 'P', 'F'],
                            ['B', 'L', 'Q', 'S', 'L', 'N', 'E', 'E', 'E', 'V', 'U', 'L', 'F', 'M', 'Z'],
                            ['O', 'K', 'R', 'I', 'K', 'A', 'M', 'M', 'R', 'M', 'F', 'B', 'A', 'P', 'P'],
                            ['N', 'U', 'I', 'I', 'Y', 'H', 'Q', 'M', 'E', 'M', 'Q', 'R', 'Y', 'F', 'S'], 
                            ['E', 'Y', 'Z', 'Y', 'G', 'K', 'Q', 'J', 'P', 'C', 'Q', 'W', 'Y', 'A', 'K'],
                            ['S', 'J', 'F', 'Z', 'M', 'Q', 'I', 'B', 'D', 'B', 'E', 'M', 'K', 'W', 'D'],
                            ['T', 'G', 'L', 'B', 'H', 'C', 'B', 'E', 'C', 'H', 'T', 'O', 'Y', 'I', 'K'],
                            ['O', 'J', 'Y', 'E', 'U', 'L', 'N', 'C', 'C', 'L', 'Y', 'B', 'Z', 'U', 'H'],
                            ['W', 'Z', 'M', 'I', 'S', 'U', 'K', 'U', 'R', 'B', 'I', 'D', 'U', 'X', 'S'],
                            ['K', 'Y', 'L', 'B', 'Q', 'Q', 'P', 'M', 'D', 'F', 'C', 'K', 'E', 'A', 'B']
                          ]
        self.assertEqual(puzzle, expected_result)

if __name__ == '__main__':
    unittest.main()
