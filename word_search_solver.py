from word_search_problem import WordSearchProblem

class WordSearchSolver:
    def __init__(self, problem):
        self.problem = problem
    
    def solve_puzzle(self):
        answer = []
        found_words = []
        for row in range(0, len(self.problem.puzzle)):
            for col in range(0, len(self.problem.puzzle[row])):
                for word in self.problem.word_list:
                    if word[0] == self.problem.puzzle[row][col] and word not in found_words:
                        directions = self.get_possible_directions(word, row, col)
                        result = self.check_directions(directions, word, row, col)
                        if result != "":
                            answer.append(result)
                            found_words.append(word)
                    
                    if word[-1] == self.problem.puzzle[row][col] and word not in found_words:
                        directions = self.get_possible_directions(word, row, col)
                        result = self.check_directions(directions, word[::-1], row, col, True)
                        if result != "":
                            answer.append(result)
                            found_words.append(word)

        return "\n".join(sorted(answer))
    
    def get_possible_directions(self, word, row, col):
        directions = []

        if row >= len(word) - 1:
            directions.append("UP")

        if len(self.problem.puzzle) - row >= len(word) - 1:
            directions.append("DOWN")

        if col >= len(word) - 1:
            directions.append("LEFT")

            if "DOWN" in directions:
                directions.append("DOWN_LEFT")
            
            if "UP" in directions:
                directions.append("UP_LEFT")
            
        if len(self.problem.puzzle) - col >= len(word) - 1:
            directions.append("RIGHT")

            if "DOWN" in directions:
                directions.append("DOWN_RIGHT")
            
            if "UP" in directions:
                directions.append("UP_RIGHT")

        return directions
    
    def check_directions(self, directions, word, row, col, is_reversed = False):
        coordinates = []
        if "UP" in directions:
            count = 0
            for i in range (row, row - len(word), -1):
                if self.problem.puzzle[i][col] == word[count]:
                    coordinates.append("(" + str(col) + "," + str(i) + ")")
                    count += 1
                else:
                    coordinates = []
                    break
        
        if "DOWN" in directions and len(coordinates) != len(word):
            count = 0
            for i in range (row, row + len(word)):
                if self.problem.puzzle[i][col] == word[count]:
                    coordinates.append("(" + str(col) + "," + str(i) + ")")
                    count += 1
                else:
                    coordinates = []
                    break
        
        if "LEFT" in directions and len(coordinates) != len(word):
            count = 0
            for i in range (col, col - len(word), -1):
                if self.problem.puzzle[row][i] == word[count]:
                    coordinates.append("(" + str(i) + "," + str(row) + ")")
                    count += 1
                else:
                    coordinates = []
                    break
        
        if "RIGHT" in directions and len(coordinates) != len(word):
            count = 0
            for i in range (col, col + len(word)):
                if self.problem.puzzle[row][i] == word[count]:
                    coordinates.append("(" + str(i) + "," + str(row) + ")")
                    count += 1
                else:
                    coordinates = []
                    break
        
        if "UP_RIGHT" in directions and len(coordinates) != len(word):
            count = 0
            j = col
            for i in range (row, row - len(word), -1):
                if self.problem.puzzle[i][j] == word[count]:
                    coordinates.append("(" + str(j) + "," + str(i) + ")")
                    count += 1
                    j += 1
                else:
                    coordinates = []
                    break
        
        if "UP_LEFT" in directions and len(coordinates) != len(word):
            count = 0
            j = col
            for i in range (row, row - len(word), -1):
                if self.problem.puzzle[i][j] == word[count]:
                    coordinates.append("(" + str(j) + "," + str(i) + ")")
                    count += 1
                    j -= 1
                else:
                    coordinates = []
                    break
        
        if "DOWN_RIGHT" in directions and len(coordinates) != len(word):
            count = 0
            j = col
            for i in range (row, row + len(word)):
                if self.problem.puzzle[i][j] == word[count]:
                    coordinates.append("(" + str(j) + "," + str(i) + ")")
                    count += 1
                    j += 1
                else:
                    coordinates = []
                    break

        if "DOWN_LEFT" in directions and len(coordinates) != len(word):
            count = 0
            j = col
            for i in range (row, row + len(word)):
                if self.problem.puzzle[i][j] == word[count]:
                    coordinates.append("(" + str(j) + "," + str(i) + ")")
                    count += 1
                    j -= 1
                else:
                    coordinates = []
                    break
        
        if is_reversed:
            coordinates.reverse()
            word = word[::-1]

        return "" if len(coordinates) == 0 else word + ": " + ",".join(coordinates)