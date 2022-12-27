def isHappy(n: int) -> bool:
    summer = lambda x: sum(int(i) ** 2 for i in str(x))

    slow = summer(n)
    fast = summer(summer(n))

    while slow != fast:
        slow = summer(slow)
        fast = summer(summer(fast))

    return slow == 1

print(isHappy(2))