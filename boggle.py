import copy


class boggle:
    """
        board looks like
        [
            ['A', 'B', 'C', 'D'],
            ['A', 'B', 'C', 'D'],
            ['A', 'B', 'C', 'D'],
            ['A', 'B', 'C', 'D']
        ]
        assume capital letters

        dictionary looks like
        {
            'peace': True,
            'pea': True
        }

        traveled looks like
        [
            (0,0),
            (0,1),
            (1,1)
        ]
    """
    def __init__(self, board, dictionary, prefix):
        self.board = board
        self.dictionary = dictionary
        self.prefix = prefix
        self.words = []

    def find_all(self):
        for r in range(0, 4):
            for c in range(0, 4):
                self.find('', [], r, c)
        return self.words

    def find(self, string, traveled, row, column):
        string = string + self.board[row][column]

        traveled.append((row, column))
        print string

        # real words, not palindromes/repeats
        if string in self.dictionary and string not in self.words:
            self.words.append(string)

        # stop if 4-letter prefix does not have real word potential
        if len(string) == 4 and string not in self.prefix:
            return

        # travel in all available untraveled directions
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                if (row+r >= 0 and row+r < len(self.board)) and \
                   (column+c >= 0 and column+c < len(self.board[0])) and \
                   not (r == 0 and c == 0) and \
                   (row+r, column+c) not in traveled:
                        # give each path its own traveled object with same data
                        new_traveled = copy.copy(traveled)

                        self.find(string, new_traveled, row+r, column+c)


def main():
    board = [
        ['E', 'C', 'E', 'P'],
        ['L', 'A', 'G', 'O'],
        ['L', 'E', 'H', 'N'],
        ['E', 'S', 'S', 'O']
    ]

    dictionary = {
        # not in board
        "MONKEY": True,
        "PEAK": True,
        "HELLO": True,

        # in board: 23
        "LESSON": True,
        "PEACE": True,
        "CALLS": True,

        "PEA": True,
        "ELLE": True,
        "HOPE": True,
        "GO": True,
        "HEAL": True,
        "ALE": True,
        "HOG": True,
        "SEE": True,
        "LAG": True,
        "LEG": True,
        "HE": True,
        "GAL": True,
        "HELL": True,
        "SELL": True,
        "GEL": True,
        "NOPE": True,
        "SON": True,
        "PEG": True,
        "CALL": True,
        "PEAL": True,
    }

    prefix = {
        "PEAC": True,
        "LESS": True,
        "HELL": True,
        "SELL": True,
        "CALL": True,
    }

    my_boggle = boggle(board, dictionary, prefix)

    words = my_boggle.find_all()

    print words
    print "number of found words: " + str(len(words))

main()
