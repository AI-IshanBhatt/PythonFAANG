print("Keep in mind +,| returns the updated view on underlying set")
print("LIST TRICKS")
l = [1,2]

print(l + [3])  # You could do it because of line 1
print(l)  # Above command did not modify original l, HIGHLY useful in recursions

print("ADD ITEMS IN LIST")
l.append(4)
print(l)
l += [5]  # This returns None
print(l)

print("ADDING MULTIPLE ITEMS IN LIST")
l.extend([6,7])
print(l)
l += [8,9]
print(l)

print("="*50)
print("SET TRICKS")
s = set()  # Initializing with s = {} makes it dict and s = {1} makes it set WEIRD

print(s | {1})
print(s)  # Above command does not modify original s, Highly useful in recursions

print("ADDING ITEMS IN SET")
s.add(1)
print(s)
s |= {2}
print(s)

print("ADDING MULTIPLE ITEMS IN SET")
s |= {3,4}
print(s)

print("REVERSING LIST")
print(l)
# l.reverse() this reverses list in place
print(l[::-1])
print("REVERSE PART OF LIST")
l[2:6] = l[2:6][::-1]
print(l)
# Naively you may think that l[2:6] = l[2:6].reverse() would work but it wont
# In Python slicing ALWAYS creates a copy of list and .reverse() reverses tht copy but reference to it is lost
l[2:6] = reversed(l[2:6])  # This works but upper one is cool
print(l)

print("SOME MORE FUN WITH INDEX")
string1 = "abcdefgh"
print(f"All the even index entries {string1[::2]}")
print(f"All the odd index entries {string1[1::2]}")

print("String times boolean gives original string or empty string")
print(string1*True)
print(string1*False)

print("MODIFYING DICT INSERT k,v | UPDATE | DELETE KEY")
d = {"a":10, "b":5, "d":7, "f":9, "e":15}
print(d | {"c": 20})  # This one does not add anything to original dict
print(d)
d |= {"c": 20}  # This one updates the dict
print(d)
# You may think d["c"] = 20 is easier an option,
# and it is but in some cases you need to add the value in dict and return it.
# It will be super helpful in recursion/backtracking examples, like we do with lists and sets.


