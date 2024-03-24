sum_ = 0
with open("aoc_input_1") as f:
    for line in f:
        digits = [c for c in line if c.isdigit()]
        digits = int("".join([digits[0], digits[-1]]))
        sum_ += digits

print(sum_)

sum_ = 0
words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

with open("aoc_input_1") as f:
    lines = f.readlines()

    # lines = ["eightwo", "two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

    final_answer = []
    for line in lines:
        answer = []
        for i in range(len(line)):
            if line[i].isdigit():
                answer.append(line[i])
            else:
                for w in words:
                    if w == line[i: i+len(w)]:
                        answer.append(words[w])
        final_answer.append(answer)

    for idx, answer in enumerate(final_answer, start=1):
        digits = int("".join([answer[0], answer[-1]]))
        sum_ += digits

print(sum_)