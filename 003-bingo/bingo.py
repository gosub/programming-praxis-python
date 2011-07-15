# Bingo
# Calculate the probability of winning at Bingo
# Programming Praxis Exercise 3
# http://programmingpraxis.com/2009/02/19/bingo/

from random import sample, shuffle


class BingoCard:
    def __init__(self):
        self.card = [sample(xrange(a,b), 5) for a,b in \
                         [(1,16), (16,31), (31,46), (46,61), (61,76)]]
        self.card[2][2] = False

    def cross_out(self, number):
        for column in self.card:
            if number in column:
                idx = column.index(number)
                column[idx] = False

    def has_won(self):
        all_falses = lambda x: not(any(x))

        diag1 = (self.card[x][x] for x in xrange(5))
        diag2 = (self.card[4-x][x] for x in xrange(5))
        win_on_diag = all_falses(diag1) or all_falses(diag2)
        win_on_column = any(map(all_falses, self.card))
        rotated = zip(*self.card)
        win_on_rows = any(map(all_falses, rotated))

        return win_on_diag or win_on_column or win_on_rows

    def show(self):
        for r in xrange(5):
            for c in xrange(5):
                n = self.card[c][r]
                if n:
                    print "%2d" % n,
                else:
                    print " X",
            print


class BingoGame:
    def __init__(self, card_count):
        self.card_count = card_count
        self.reset()

    def reset(self):
        self.extraction_seq = range(1,76)
        shuffle(self.extraction_seq)
        self.turn = 0
        self.card_list = [BingoCard() for x in xrange(self.card_count)]

    def play_another_turn(self):
        if self.extraction_seq:
            extracted = self.extraction_seq.pop()
            for card in self.card_list:
                card.cross_out(extracted)
            self.turn += 1
        else:
            raise Exception("Game ran past available numbers for extraction")
            
    def has_a_winner(self):
        return any(card.has_won() for card in self.card_list)

    def turns_to_victory(self):
        while not self.has_a_winner():
            self.play_another_turn()
        return self.turn


def Simulation(card_count, repetitions):
    durations = []
    game = BingoGame(card_count)
    for i in xrange(repetitions):
        game.reset()
        durations.append(game.turns_to_victory())
    average = float(sum(durations)) / repetitions
    return average


if __name__ == '__main__':
    for cards, repetitions in [(1, 10000), (500, 100)]:
        average_game = Simulation(cards, repetitions)
        txt = "A bingo game with {0} cards lasts, on average, {1} turns."
        print txt.format(cards, average_game)

