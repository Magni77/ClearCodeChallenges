#print("{0:b}".format(10))

soldiers = [23,-3, 32, -24]# [7, -3, -14, 6] #[21, -3, 20]
bin_solders = []
even_team = []
odd_team = []


def battle(soldiers):
    set_teams(soldiers)
    even_score = 0
    odd_score = 0
    for e in even_team:
        even_score += e
    for o in odd_team:
        odd_score += o

    if even_score > odd_score:
        print('Evens win the battle by a score   of {}:{}'.format(even_score, odd_score))
    elif odd_score > even_score:
        print('Odds win the battle by a score   of {}:{}'.format(odd_score, even_score))
    elif odd_score == even_score:
        print('Tie! {}:{}'.format(even_score, odd_score))


def set_teams(soldiers):
    for x in soldiers:
        if is_even(x):
            count = count_solders(dec_2_bin(x), 0)
            even_team.append(count)
        else:
            count = count_solders(dec_2_bin(x), 1)
            odd_team.append(count)


def dec_2_bin(num):#moze jakies wyjatki, check if int
    return "{0:b}".format(num)


def count_solders(bin_num, team):
    amount = 0
    try:
        for x in str(bin_num):
            if x == str(team):
                amount += 1
    except:
        raise NotImplementedError
    if int(bin_num) < 0:
        return -amount
    return amount


def is_even(num):
    return num % 2 == 0

battle(soldiers)
