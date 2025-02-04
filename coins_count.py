import timeit

def measure_time(search_func, count, coins):
    start_time = timeit.default_timer()
    searched_data = search_func(count, coins)
    execution_time = timeit.default_timer() - start_time
    return searched_data, execution_time


def find_coins_greedy(sum, coins):
    current_sum = sum
    coins_count = {}

    for coin in coins:
        num = current_sum // coin
        if num > 0:
            coins_count[coin] = num
            current_sum -= num * coin
        if current_sum == 0:
            break
            
    return coins_count


def find_min_coins(sum, coins):
    min_coins_required = [0] + [float('inf')] * sum
    coin_used = [0] * (sum + 1)

    for i in range(1, sum + 1):
        for coin in coins:
            if i >= coin and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1
                coin_used[i] = coin

    total_coins = {}
    current_sum = sum

    while current_sum > 0:
        coin = coin_used[current_sum]
        total_coins[coin] = total_coins.get(coin, 0) + 1
        current_sum -= coin

    return total_coins

print(f"\nFind coins by greedy algorithm: {measure_time(find_coins_greedy, 573412, [50, 25, 10, 6, 5, 1])}")

print(f"\nFind coins by dynamic programming: {measure_time(find_min_coins, 573412, [50, 25, 10, 6, 5, 1])}\n")