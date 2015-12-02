def change_possibilities_top_down(amount_left, denominations_left):
    # base cases:
    # we hit the amount spot on. yes!
    if amount_left == 0: return 1
    # we overshot the amount left (used too many coins)
    if amount_left < 0: return 0
    # we're out of denominations
    if len(denominations_left) == 0: return 0

    print "checking ways to make %i with %s" % (amount_left, denominations_left)

    # choose a current_coin
    current_coin, rest_of_coins = denominations_left[0], denominations_left[1:]

    # see how many possibilities we can get
    # for each number of times to use current_coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_possibilities_top_down(amount_left, rest_of_coins)
        amount_left -= current_coin

    return num_possibilities

amount = 63
denoms = [1,5,10,25]
change_possibilities_top_down(amount,denoms)