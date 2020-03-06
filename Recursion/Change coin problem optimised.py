# using recursion
def coin_recursion(target, coins):

    min_coins = target  # just setting some default value

    if target in coins:
        return 1

    for money in [c for c in coins if c <= target]:

        num_coins = 1 + coin_recursion(target-money, coins)

        if num_coins < min_coins:
            min_coins = num_coins

    return min_coins


# DYNAMIC APPROACH USING MEMOIZATION

def dynamic_coin_rec(target, coins, cache_results):

    min_coins = target

    if target in coins:
        # saving for future uses in same value of target, faster access with cost of storage
        cache_results[target] = 1
        return 1

    elif cache_results[target] > 0:
        return cache_results[target]

    else:
        for money in [c for c in coins if c <= target]:

            num_coins = 1 + dynamic_coin_rec(target-money, coins, cache_results)

            if num_coins < min_coins:
                min_coins = num_coins

            cache_results[target] = min_coins

    return min_coins


print(coin_recursion(3,[1,5,10]))

target = 60
cache = [0]*(target+1)
print(dynamic_coin_rec(target,[1,5,10,25],cache))
