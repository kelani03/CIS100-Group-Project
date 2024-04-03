import random

class ShapeMash:
    def __init__(self):
        self.board_size = 8
        self.shapes = ['▲', '■', '★', '●']  # Unicode characters for triangle, square, star, circle
        self.levels = 10
        self.goal_score = 100
        self.score = 0

    def initialize_board(self):
        return [[random.choice(self.shapes) for _ in range(self.board_size)] for _ in range(self.board_size)]

    def draw_board(self, board):
        print("\n" + "-" * 34)
        for row in board:
            line_to_draw = " | ".join(row)
            print("|", line_to_draw, "|")
            print("-" * 34)

    def get_move(self):
        input("Tap 'Play' to start Level: ")
        return "play"

    def match_shapes(self, board):
        matched_positions = set()
        for i in range(self.board_size):
            for j in range(self.board_size):
                shape = board[i][j]
                if shape == ' ':
                    continue
                # Check horizontally
                count = 1
                for k in range(j + 1, self.board_size):
                    if board[i][k] == shape:
                        count += 1
                    else:
                        break
                if count >= 3:
                    for k in range(j, j + count):
                        matched_positions.add((i, k))
                # Check vertically
                count = 1
                for k in range(i + 1, self.board_size):
                    if board[k][j] == shape:
                        count += 1
                    else:
                        break
                if count >= 3:
                    for k in range(i, i + count):
                        matched_positions.add((k, j))
        return matched_positions

    def update_board(self, board, matched_positions):
        for i, j in matched_positions:
            board[i][j] = random.choice(self.shapes)
            self.score += 10  # Increase score for each matched shape
        return board

    def continue_game(self):
        return self.score < self.goal_score and self.levels > 0

    def play_level(self):
        print("\nLevel", 11 - self.levels)
        board = self.initialize_board()
        self.draw_board(board)
        move = self.get_move()
        matched_positions = self.match_shapes(board)
        while matched_positions:
            board = self.update_board(board, matched_positions)
            self.draw_board(board)
            matched_positions = self.match_shapes(board)
        self.levels -= 1

    def play(self):
        print("Welcome to Shape Mash!")
        while self.continue_game():
            self.play_level()
        print("Game Over! Your final score:", self.score)

if __name__ == "__main__":
    game = ShapeMash()
    game.play()


