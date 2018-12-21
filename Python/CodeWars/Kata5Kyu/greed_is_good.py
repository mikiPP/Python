"""Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules.
 You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point"""


def score(dice):
    sum = 0
    Triple = False
    Single = False
    Triples = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}

    for die in dice:
        if dice.count(die) >= 3 and Triple == False:
            if die in Triples:
                Triple = True
                sum += Triples[die]
        elif dice.count(die) < 3 or (dice.count(die) == 4 and Single == False):
            if die == 1:
                sum += 100
            elif die == 5:
                sum += 50
            Single = True
    return sum


if __name__ == '__main__':

    assert score([2, 3, 4, 6, 2]) == 0
    assert score([4, 4, 4, 3, 3]) == 400
    assert score([2, 4, 4, 5, 4]) == 450
