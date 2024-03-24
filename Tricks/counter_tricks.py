from collections import defaultdict, Counter

print("LETTER COUNTING")
s = "mississippi"

count_dict = defaultdict(int)

for c in s:
    count_dict[c] += 1

print(count_dict)
print("Sort dict")
print("By char/key")
count_dict = dict(sorted(count_dict.items()))
print(count_dict)

print("By value/frequency")
count_dict = dict(sorted(count_dict.items(), key=lambda x:x[1]))
print(count_dict)

print("By value/frequency in descending")
count_dict_sorted = dict(sorted(count_dict.items(), key=lambda x:-x[1]))
print(count_dict_sorted)
count_dict_sorted_again = dict(sorted(count_dict.items(), key=lambda x:x[1], reverse=True))
print(count_dict_sorted_again)

print("DOING IT IN PYTHONIC WAY WITH COUNTER")
print()
c = Counter(s)
print(c.most_common())
print(f"Most common element is {c.most_common(1)[0][0]}")
print(f"Highest frequency is {c.most_common(1)[0][1]}")

print("UPDATING COUNTS")
c.update("missouri")
print(c.most_common())

print("COUNTER WITH DICT")
sales = {"apple": 25, "orange":15, "banana":12}
sales_counter = Counter(sales)
tuesday_sales = {"apple": 4, "orange": 7, "tomato": 4}
sales_counter.update(tuesday_sales)
print(sales_counter.most_common())

print("Treating counter as dict")
for k,v in sales_counter.items():
    print(f"{k} -> {v}")

print("Pairing it up with zip")
items, freq = zip(*sales_counter.most_common())
print(items)
print(freq)

print("Getting K most occurring elements")
print(c)
highest_frequency = c.most_common(1)[0][1]
most_frequent_elements = [ele[0] for ele in c.most_common() if ele[1] == highest_frequency]
print(most_frequent_elements)

print("RESTORING ELEMENTS FROM COUNTER, Used in AlgoExpert create dict question")
elements = list(c.elements())
print(elements)
print("".join(elements))

print("MATH OPERATIONS ON THE COUNTERS Treat it like dict if you want calculations on values")
sales_day1 = Counter(apple=4, orange=9, banana=6)
sales_day2 = Counter(apple=10, orange=8, banana=6)

print(f"Total Sales {sales_day1 + sales_day2}")
print(f"Increment on day 2 {sales_day2 - sales_day1}")
print(f"Minimum sales of 2 days {sales_day1 & sales_day2}")  # Useful in those anagram matching questions
print(f"Maximum sales of 2 days {sales_day1 | sales_day2}")

print("Using counter to do frequency based sorting")
l = [1,2,3,4,3,3,3,6,7,1,1,9,3,2]
counts = Counter(l)
print(sorted(l, key=lambda x:counts[x]))
print(sorted(l, key=lambda x:-counts[x]))  # Max frequency is first