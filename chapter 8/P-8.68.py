"""
Write a program that can play Tic-Tac-Toe effectively. (See Section 5.6.)
To do this, you will need to create a game tree T, which is a tree where
each position corresponds to a game configuration, which, in this case,
is a representation of the Tic-Tac-Toe board. (See Section 8.4.2.) The
root corresponds to the initial configuration. For each internal position p
in T, the children of p correspond to the game states we can reach from
p’s game state in a single legal move for the appropriate player, A (the
first player) or B (the second player). Positions at even depths correspond
to moves for A and positions at odd depths correspond to moves for B.
Leaves are either final game states or are at a depth beyond which we do
not want to explore. We score each leaf with a value that indicates how
good this state is for player A. In large games, like chess, we have to use a
heuristic scoring function, but for small games, like Tic-Tac-Toe, we can
construct the entire game tree and score leaves as +1, 0, −1, indicating
whether player A has a win, draw, or lose in that configuration. A good
algorithm for choosing moves is minimax. In this algorithm, we assign a
score to each internal position p in T, such that if p represents A’s turn, we
compute p’s score as the maximum of the scores of p’s children (which
corresponds to A’s optimal play from p). If an internal node p represents
B’s turn, then we compute p’s score as the minimum of the scores of p’s
children (which corresponds to B’s optimal play from p).
"""
from collections import deque
from LinkedTree import LinkedTree
from copy import deepcopy


def __str__(self):
    rows = ['|'.join(self._board[r]) for r in range(3)]
    return '\n-----\n'.join(rows)


class TicTacToeBot():
    def __init__(self):
        self.undo_commands = []
        self._board = [[' '] * 3 for _ in range(3)]
        self._player = 'X'
        self._opponent = 'O'
        self.active_tour = 'X'

    def minmax(self):
        print('For bot', self.active_tour)
        return self._minmax(self.active_tour)

    def _minmax(self, tour):
        score = self.score()
        if score != 0:
            return score, None

        best = 879, None
        values = []
        for y in range(3):
            for x in range(3):
                if self._board[y][x] == ' ':
                    move = (x, y)
                    self._board[y][x] = tour
                    val, best_move = self._minmax(self.next_tour(tour))
                    values.append((val, move))
                    self._board[y][x] = ' '

                    if val < best[0]:
                        best = (val, move)
        if len(values) == 0:
            return score, None
        if tour == self._player:
            return max(values, key=lambda item: item[0])
        else:
            return min(values, key=lambda item: item[0])

    def next_tour(self, tour):
        if tour == self._opponent:
            return self._player
        return self._opponent

    def change_player(self):
        if self.active_tour == self._player:
            self.active_tour = self._opponent
        else:
            self.active_tour = self._player

    def __str__(self):
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)

    def _is_win(self, mark):
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or
                mark == board[1][0] == board[1][1] == board[1][2] or
                mark == board[2][0] == board[2][1] == board[2][2] or
                mark == board[0][0] == board[1][0] == board[2][0] or
                mark == board[0][1] == board[1][1] == board[2][1] or
                mark == board[0][2] == board[1][2] == board[2][2] or
                mark == board[0][0] == board[1][1] == board[2][2] or
                mark == board[0][2] == board[1][1] == board[2][0])

    def score(self):
        if self._is_win(self._player):
            return 10
        elif self._is_win(self._opponent):
            return -10
        else:
            return 0

    def mark(self, x, y):
        if not 0 <= y <= 2 and 0 <= y <= 2:
            raise ValueError('Invalid board position')
        if self._board[y][x] != ' ':
            raise ValueError('Board position occupied')
        self._board[y][x] = self.active_tour
        self.change_player()

    def won(self):

        if self._is_win(self._player):
            return True, self._player
        elif  self._is_win(self._opponent):
            return True, self._opponent
        elif [node for x in self._board for node in x].count(' ') == 0:
            return True, 'Tie'
        else:
            return False, None

bot = TicTacToeBot()


def bot_move():
    print(bot.active_tour, 'Tour')
    _, (x, y) = bot.minmax()
    print(bot.active_tour, 'Tour')
    bot.mark(x, y)


def player_move():
    num = int(input(bot.active_tour + ' -> '))
    moves = {1: (0, 2),
             2: (1, 2),
             3: (2, 2),
             4: (0, 1),
             5: (1, 1),
             6: (2, 1),
             7: (0, 0),
             8: (1, 0),
             9: (2, 0)}
    x, y = moves[num]
    # x, y = num % 3, num // 3
    bot.mark(x, y)


while True:
    try:
        print()
        print(bot)
        player_move()
        print()
        print(bot)
        end, message = bot.won()
        if end:
            print('Bravo! {} won the game!'.format(message))
            exit()
        else:
            pass

        bot_move()
        end, message = bot.won()
        if end:
            print('Bravo! {} won the game!'.format(message))
            exit()
        else:
            pass

    except ValueError:
        print('Board position occupied!')
