import unittest
from word_search_problem import WordSearchProblem
from word_search_solver import WordSearchSolver

class TestWordSearchProblemCase(unittest.TestCase):
    def test_invalid_file_path_error_thrown(self):
        with self.assertRaisesRegex(ValueError, "FILE DOES NOT EXIST"): 
            WordSearchProblem("text_files/imaginary_file.txt")

    def test_empty_file_error_thrown(self):
        with self.assertRaisesRegex(ValueError, "FILE IS EMPTY"): 
            WordSearchProblem('text_files/empty_file.txt')
    
    def test_word_map_generator_maps_all_search_words(self):
        problem = WordSearchProblem('text_files/sample_1.txt')
        word_map = problem.get_word_list()
        expected_result = ['BONES','KHAN','KIRK','SCOTTY','SPOCK','SULU','UHURA']

        self.assertEqual(word_map, expected_result)
    
    def test_word_map_generator_maps_all_search_words_once(self):
        problem = WordSearchProblem('text_files/duplicate_words.txt')
        word_map = problem.get_word_list()
        expected_result = ['BONES','KHAN','KIRK','SCOTTY','SPOCK','SULU','UHURA']

        self.assertEqual(word_map, expected_result)
    
    def test_puzzle_generator_gets_all_letters(self):
        problem = WordSearchProblem("text_files/sample_1.txt")
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
    
class TestWordSearchSolverCase(unittest.TestCase):
    def test_word_search_sample_1(self):
        problem = WordSearchProblem('text_files/sample_1.txt')
        solver = WordSearchSolver(problem)
        expected_result = "BONES: (0,6),(0,7),(0,8),(0,9),(0,10)\nKHAN: (5,9),(5,8),(5,7),(5,6)\nKIRK: (4,7),(3,7),(2,7),(1,7)\nSCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)\nSPOCK: (2,1),(3,2),(4,3),(5,4),(6,5)\nSULU: (3,3),(2,2),(1,1),(0,0)\nUHURA: (4,0),(3,1),(2,2),(1,3),(0,4)"
        self.assertEqual(solver.solve_puzzle(), expected_result)

    def test_word_search_sample_2(self):
        problem = WordSearchProblem('text_files/sample_2.txt')
        solver = WordSearchSolver(problem)
        expected_result = "AIR: (1,2),(2,1),(3,0)\nAVATAR: (0,2),(0,3),(0,4),(0,5),(0,6),(0,7)\nEARTH: (5,6),(4,6),(3,6),(2,6),(1,6)\nELEMENTS: (0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)\nFIRE: (7,5),(6,4),(5,3),(4,2)\nFOUR: (7,4),(7,3),(7,2),(7,1)\nWATER: (7,0),(6,1),(5,2),(4,3),(3,4)"
        self.assertEqual(solver.solve_puzzle(), expected_result)

    def test_word_search_sample_3(self):
        problem = WordSearchProblem('text_files/sample_3.txt')
        solver = WordSearchSolver(problem)
        expected_result = "KING: (5,2),(4,3),(3,4),(2,5)\nPAUPER: (0,0),(1,0),(2,0),(3,0),(4,0),(5,0)\nPRINCE: (4,5),(4,4),(4,3),(4,2),(4,1),(4,0)\nQUEEN: (0,2),(1,2),(2,2),(3,2),(4,2)"
        self.assertEqual(solver.solve_puzzle(), expected_result)


if __name__ == '__main__':
    unittest.main()
