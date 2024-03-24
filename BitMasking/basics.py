from collections import deque


def decimal_to_binary(n):
    answer = deque()
    while n > 0:
        # If you do it by hand whatever is reminder you put it on left when writing, that's why appendLeft works
        answer.appendleft(str(n % 2))
        n //= 2
    return answer


def check_k_bit_set(n, k):
    return (n >> k) & 1


def count_number_of_bit_set(n):
    counter = 0
    while n > 0:
        counter += (n % 2 != 0)
        n //= 2
    return counter


"""
If number is power of 2 then only 1 of it's bit is set, 16 - 10000, so N-1 is 15 - 1111, It will have all the bits set.
If we do and of N,N-1 we should get all 0s if the number is power of 2, So you avoid the loop with this approach.
"""


def is_power_of_two(n):
    return n & (n - 1) == 0


def number_swap_xor(a, b):
    print(a, b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a, b)


def remove_last_bit(n):
    return n & (n-1)  # If n has last bits 10, n-1 will have 01 anding them resets 10 to 00


def get_last_set_bit(n):
    return n & ~(n-1)  # n=28 -> 11100 n-1 -> 11011 ~(n-1) -> 00100 anding them both is 4 that is the last set bit

def set_kth_bit(n, k):
    return n | (1 << k)  # We have to set the bit so oring them with 1 << k, that's 100 if k==2, then 2nd bit becomes set

def unset_kth_bit(n, k):
    return n & ~(1 << k)  # n=20=10100 k = 2, 1 << k = 00100. ~ (1 << k) = 11011 , now and them means in any possibility kth bit is set to 0.
    # So anding them would set it 0 in N itself.


def flip_kth_bit(n, k):
    # Use xor as xor makes 0^1 = 1 and 1^1=0 thus flipping the bit
    return n ^ (1 << k)


print(decimal_to_binary(14))
print(check_k_bit_set(21, 4))
print(count_number_of_bit_set(29))
print(is_power_of_two(4095))
print(is_power_of_two(128))
print(remove_last_bit(21))
print(get_last_set_bit(28))
print(set_kth_bit(20, 5))
print(unset_kth_bit(27, 4))
print(flip_kth_bit(27, 2))