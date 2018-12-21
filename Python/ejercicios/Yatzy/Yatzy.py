class Yatzy:

    @staticmethod
    def chance(*dice):

        assert type(dice) == tuple

        acumulador = 0

        for die in dice:
            acumulador += die

        assert type(acumulador) == int

        return acumulador

    @staticmethod
    def yatzy(*dice):

        return 50 if dice.count(dice[0]) == 5 else 0

    @staticmethod
    def ones(* dice):

        ONE = 1
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(* dice):

        TWO = 2
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):

        THREE = 3

        return dice.count(THREE) * THREE

    def __init__(self, D1, D2, D3, D4, _5):
        self.dice = [0] * 5
        self.dice[0] = D1
        self.dice[1] = D2
        self.dice[2] = D3
        self.dice[3] = D4
        self.dice[4] = _5

    @staticmethod
    def fours(*dice):
        FOUR = 4
        return dice.count(FOUR) * FOUR

    @staticmethod
    def fives(*dice):
        FIVE = 5
        return dice.count(FIVE) * FIVE

    @staticmethod
    def sixes(*dice):
        SIX = 6
        return dice.count(SIX) * SIX

    @staticmethod
    def pairs(*dice):

        acumulador = 0
        maximum = 0

        for die in dice:
            if dice.count(die) == 2:
                if die > maximum:
                    maximum = die

        return maximum * 2

    @staticmethod
    def two_pair(*dice):
        numeroParejas = 0
        acumulador = 0
        for die in dice:
            if dice.count(die) == 2:
                numeroParejas += 1
                acumulador += die

        if numeroParejas == 4:
            return acumulador

        else:
            return 0

    @staticmethod
    def four_of_a_kind(*dice):
        if dice.count(max(dice)) >= 4:
            return  max(dice)*4
        elif dice.count(min(dice)) >= 4: 
            return min(dice)*4 
        else:
            return 0


    @staticmethod
    def three_of_a_kind(*dice):
        for die in dice:
            if dice.count(die) >= 3:
                return die* 3
        return 0

    @staticmethod
    def smallStraight(*dice):
        add = 0
        for die in dice:
            if dice.count(die) == 1 and die != 6: 
                add += die
            else:
                return 0

        return add

    @staticmethod
    def largeStraight(*dice):
        add = 0
        for die in dice:
            if dice.count(die) == 1 and die != 1: 
                add += die
            else:
                return 0

        return add

    @staticmethod
    def fullHouse(*dice):
        add=0
        pair = False
        threes = False

        for die in dice:
            if dice.count(die) == 3:
                add += die
                threes = True

            elif dice.count(die) == 2:
                add += die
                pair = True
        if pair and threes:
            return add

        else:
            return 0



if __name__ == '__main__':

    # caDa DaDo

    D1 = 1
    D2 = 2
    D3 = 3
    D4 = 4
    D5 = 5
    D6 = 6

    # casos test De chance

    assert Yatzy.chance(D1, D2, D3, D4, D5) == 15
    assert Yatzy.chance(D2, D2, D2, D2, D2) == 10
    assert Yatzy.chance(D2, D3, D5, D2) == 12

    # casos test De ones

    assert Yatzy.ones(D1, D5, D2) == 1
    assert Yatzy.ones(D2, D1, D3, D3, D2) == 1
    assert Yatzy.ones(D2, D4, D4, D2) == 0
    assert Yatzy.ones(D1, D1, D1, D1) == 4

    # casos test twos

    assert Yatzy.twos(D1, D5, D2) == 2
    assert Yatzy.twos(D2, D1, D3, D3, D2) == 4
    assert Yatzy.twos(D5, D4, D4, D1) == 0
    assert Yatzy.twos(D2, D2, D2, D2) == 8

    # casos test De three

    assert Yatzy.threes(D1, D3, D3, D3, D5) == 9
    assert Yatzy.threes(D2, D1, D3, D3, D2) == 6
    assert Yatzy.threes(D3, D3, D4, D3) == 9
    assert Yatzy.threes(D3, D3, D3, D3) == 12

    # casos test De fours

    assert Yatzy.fours(D1, D5, D2, D3, D5) == 0
    assert Yatzy.fours(D2, D1, D4, D3, D4) == 8
    assert Yatzy.fours(D3, D3, D4, D3) == 4
    assert Yatzy.fours(D4, D4, D4, D4) == 16

    # casos test De fives

    assert Yatzy.fives(D1, D5, D2, D3, D5) == 10
    assert Yatzy.fives(D2, D1, D4, D3, D4) == 0
    assert Yatzy.fives(D3, D5, D5, D5) == 15
    assert Yatzy.fives(D5, D5, D5, D5) == 20

    # casos test De six

    assert Yatzy.sixes(D1, D5, D2, D3, D5) == 0
    assert Yatzy.sixes(D2, D1, D6, D3, D6) == 12
    assert Yatzy.sixes(D3, D3, D6, D3) == 6
    assert Yatzy.sixes(D6, D6, D6, D6) == 24

    # yatzy

    assert Yatzy.yatzy(D1, D1, D1, D1, D1) == 50
    assert Yatzy.yatzy(D1, D2, D3, D4, D5) == 0

    # pairs

    assert Yatzy.pairs(D1, D1, D4, D4, D5) == 8
    assert Yatzy.pairs(D1, D2, D3, D4, D6) == 0
    assert Yatzy.pairs(D3, D2, D5, D3, D4) == 6
    assert Yatzy.pairs(D5, D5, D3, D6, D6) == 12

    # two_pairs

    assert Yatzy.two_pair(D1, D1, D4, D4, D5) == 10
    assert Yatzy.two_pair(D1, D2, D3, D4, D6) == 0
    assert Yatzy.two_pair(D3, D2, D5, D3, D4) == 0
    assert Yatzy.two_pair(D5, D5, D3, D6, D6) == 22

    # Def test_four_of_a_knD():
    assert Yatzy.four_of_a_kind(D3, D3, D3, D3, D5) == 12
    assert Yatzy.four_of_a_kind(D5, D5, D5, D4, D5) == 20
    assert Yatzy.four_of_a_kind(D3, D3, D3, D3, D3) == 12
    assert Yatzy.four_of_a_kind(D3, D3, D3, D2, D1) == 0
    assert Yatzy.four_of_a_kind(D4, D4, D4, D4, D4) == 16

    # Def test_three_of_a_kinD():
    assert Yatzy.three_of_a_kind(D3, D3, D3, D4, D5) == 9
    assert Yatzy.three_of_a_kind(D5, D5, D5, D5, D5) == 15
    assert Yatzy.three_of_a_kind(D1, D3, D2, D3, D5) == 0

    # Def test smallStraight():
    assert Yatzy.smallStraight(D1, D2, D3, D4, D5) == 15
    assert Yatzy.smallStraight(D5, D5, D5, D4, D5) == 0
    assert Yatzy.smallStraight(D3, D2, D5, D1, D4) == 15
    assert Yatzy.smallStraight(D3, D3, D3, D2, D1) == 0
    assert Yatzy.smallStraight(D2, D6, D3, D5, D4) == 0


    # Def test_largeStraight():
    assert Yatzy.largeStraight(D6, D2, D3, D4, D5) == 20
    assert Yatzy.largeStraight(D5, D5, D5, D4, D5) == 0
    assert Yatzy.largeStraight(D3, D2, D5, D1, D4) == 0
    assert Yatzy.largeStraight(D3, D3, D3, D2, D1) == 0
    assert Yatzy.largeStraight(D2, D6, D3, D5, D4) == 20

    # Def test_fullHouse():
    assert Yatzy.fullHouse(D6, D6, D3, D3, D3) == 21
    assert Yatzy.fullHouse(D5, D5, D5, D4, D4) == 23
    assert Yatzy.fullHouse(D5, D5, D5, D1, D1) == 17
    assert Yatzy.fullHouse(D3, D3, D3, D2, D1) == 0
    assert Yatzy.fullHouse(D2, D1, D2, D4, D4) == 0