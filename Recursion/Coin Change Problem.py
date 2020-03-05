def rec_coin(target, coins):

    min_coins  = target

    if target in coins:
        return 1

    for chutta in [paisa for paisa in coins if paisa <= target]:

        num_coins = 1 + rec_coin(target-chutta, coins)

        if num_coins < min_coins:
            min_coins = num_coins

    return min_coins


all_coins = [1,5,10]
total = 15
print(rec_coin(total, all_coins))

'''
OUTPUT: 2 indicates we need minimum of 2 coins change to make total of 15 from given changes of coin
5+10=15 so len(5,10) is 2 
'''