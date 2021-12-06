input_file = "4/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()

class Board():
    winning_combinations = {
        frozenset([0, 1, 2, 3, 4]), frozenset([5, 6, 7, 8, 9]), frozenset([10, 11, 12, 13, 14]),
        frozenset([15, 16, 17, 18, 19]), frozenset([20, 21, 22, 23, 24]), frozenset([0, 5, 10, 15, 20]), 
        frozenset([1, 6, 11, 16, 21]), frozenset([2, 7, 12, 17, 22]), frozenset([3, 8, 13, 18, 23]), 
        frozenset([4, 9, 14, 19, 24])
    }
    def __init__(self, board, idd):
        self.id = idd
        self.board = tuple((x for line in board for x in line))
        self.number_set = set([])
        for line in board:
            for el in line:
                self.number_set.add(el)
        self.called = set([])
        self.has_won = False

    def __repr__(self):
        res = f"Board number {self.id}:\n"
        for i, n in enumerate(self.board):
            res += str(n) + ' '
            if i % 5 == 4:
                res += '\n'
        return res + '\n'

    def call_number(self, n):
        if n not in self.number_set:
            return
        self.called.add(self.board.index(n))

    def is_in_winning_state(self):
        return any((combo.issubset(self.called) for combo in self.winning_combinations))

    def calculate_score(self, last_called_number):
        uncalled = [self.board[i] for i in range(len(self.board)) if i not in self.called]
        score = sum(uncalled) * last_called_number
        return score


bingo_numbers = [int(x) for x in data[0].split(",")]

bingo_boards_wip = data[2:] + [""]

current_board = []
bingo_boards = []
counter = 0
for i, line in enumerate(bingo_boards_wip):
    if i % 6 != 5:
        current_board += [[int(x) for x in line.split()]]
    else:
        bingo_boards += [Board(current_board, counter)]
        current_board = []
        counter += 1
end = False
for number in bingo_numbers:
    for board in bingo_boards:
        board.call_number(number)
        if board.is_in_winning_state():
            print(board)
            print(board.called)
            print(board.calculate_score(number))
            end = True
            break
    if end:
        break

### Part two
last_winner = None
last_called_number = None
for number in bingo_numbers:
    for board in bingo_boards:
        if not board.has_won:
            board.call_number(number)
            if board.is_in_winning_state():
                board.has_won = True
                last_winner = board
                last_called_number = number

print(last_winner)
print(last_winner.called)
print(last_winner.calculate_score(last_called_number))
