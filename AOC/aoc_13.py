def get_final_matching(x):
    answer = []
    for i,b in x:
        flag = True
        t = zip(*b)

        for row in t:
            p1, p2 = row[:i], row[i+2:]
            p1 = p1[::-1]
            if len(p1) < len(p2):
                p2 = p2[:len(p1)]
            elif len(p1) > len(p2):
                p1 = p1[:len(p2)]


            if p1 != p2:
                flag = False
                break
        if flag:
            answer.append(i+1)

    return answer






with open("aoc_input_13") as f:

    lines = f.readlines()

    lines.append("\n")
    boxes = []
    # print(lines)

    temp = []
    for l in lines:
        if l.strip():
            temp.append(l.strip())
        else:
            boxes.append(list(temp))
            temp.clear()

    vertical_lines = []
    horizontal_lines = []

    for box in boxes:
        for i in range(0, len(box) - 1):
            if box[i] == box[i+1]:
                horizontal_lines.append((i, box))

    for box in boxes:
        transpose = list(zip(*box))
        for i in range(0, len(transpose) - 1):
            if transpose[i] == transpose[i+1]:
                vertical_lines.append((i, transpose))



    x = get_final_matching(horizontal_lines)
    print(x)
    y = get_final_matching(vertical_lines)
    print(y)

    ans = 0
    for i in x:
        ans += (100*i)

    for i in y:
        ans += i

    print(ans)