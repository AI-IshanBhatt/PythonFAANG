from collections import Counter

a = [4,3,2,7,8,2,3,1]
N = len(a)

i = 0

# a[i] is 2, we want to put it at 1st location. 1 is 2-1

while i < N:
    if i+1 != a[i]:
        while i+1 != a[i]:
            if a[a[i]-1] == a[i]:
                i += 1
                break
            a[a[i]-1], a[i] = a[i], a[a[i]-1]
    else:
        i += 1
print(a)

text = "nlaebolko"
c, t = Counter('balloon'), Counter(text)
res = 0
while not c-t:
    x = c-t
    t -= c
    res += 1


answer = list(set(range(1,9)) - set(a))
print(answer)