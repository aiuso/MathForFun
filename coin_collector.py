import random

"""
Find min number of coins to make n cents
"""

n = random.randint(1, 100)

coins = {
    'quarter': 25,
    'dime'  : 10,
    'nickel': 5,
    'penny' : 1
}


def calc_coins(n):
    wallet = []
    value = 0
    while n != 0:
        if n >= coins.get('quarter'):
            wallet.append('quarter')
            value += 25
            n -= 25
        elif n >= coins.get('dime'):
            wallet.append('dime')
            value += 10
            n -= 10
        elif n >= coins.get('nickel'):
            wallet.append('nickel')
            value += 5
            n -= 5
        else:
            wallet.append('penny')
            value += 1
            n -= 1
    print(f'The following coins are in your wallet: {wallet}')
    print(f'You have a total of {len(wallet)} coins that are worth {value}.')


calc_coins(n)



