def pattern_checker(strings, p):
    count = 0
    for s in strings:
        l = [i for i in s.split(".") if i]

        if len(l) == len(p):
            if all(len(i) == j for i,j in zip(l, p)):
                count += 1
    return count

def binary_list(n, needed):
    return ['{:0{}b}'.format(i, n) for i in range(2**n) if i.bit_count() == needed]


def pattern_generator(s, p):
    base = s.count("?")
    # binaries = binary_list(base)

    # print(binaries)
    hash_counts = s.count("#")
    total_hash_needed = sum(p)
    missing_hash = total_hash_needed - hash_counts
    m = {"0": ".", "1": "#"}
    answer = []

    binaries = binary_list(base, needed=missing_hash)

    for b in binaries:
        x = s
        for c in b:
            x = x.replace("?", m[c], 1)
        answer.append(x)

    return answer


with open("aoc_input_12") as f:

    lines = [l.strip() for l in f.readlines()]

    string_lines = []
    patterns = []

    for l in lines:
        s,p = l.split(" ")
        string_lines.append(s.strip())
        patterns.append([int(i) for i in p.strip().split(",")])

    answer = 0
    for s,p in zip(string_lines, patterns):
        patterns_strings = pattern_generator(s,p)
        c = pattern_checker(patterns_strings, p)
        answer += c

    print(answer)
