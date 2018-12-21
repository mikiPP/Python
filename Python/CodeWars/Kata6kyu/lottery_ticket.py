def bingo(ticket, win):

    Letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    ValueLetter = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
                   76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]

    Dictionary = dict(zip(Letter, ValueLetter))
    miniPoints = 0

    for list in ticket:

        for letter in list[0]:
            valueForLetter = Dictionary[letter]

            if int(list[1]) == valueForLetter:
                miniPoints += 1
                break

    if miniPoints < win:
        return "Loser!"
    else:
        return "Winner!"

if __name__ == '__main__':
    

    assert bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2) == 'Loser!'
    assert bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1) == 'Winner!'
    assert bingo([['HGTYRE', 74], ['BE', 66], ['JKTY', 74]], 3) == 'Loser!'
