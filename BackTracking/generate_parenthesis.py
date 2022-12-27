def generate_parenthesis(n):
    answer = []
    dfs("", 0, 0, n, answer)
    return answer


def dfs(s, open_, close, total, answer):

    if len(s) == total*2:
        answer.append(s)
        return

    if open_ < total:
        dfs(s+"(", open_+1, close, total, answer)
    if close < open_:
        dfs(s+")", open_, close+1, total, answer)


def paths_in_grid(n):
    answer = []

    def backtrack(path, horizontal, vertical):
        if horizontal == vertical == n:
            answer.append(path)
            return

        if horizontal < n:
            backtrack(path+"_", horizontal+1, vertical)
        if vertical < horizontal:
            backtrack(path+"|", horizontal, vertical+1)

    backtrack("",0,0)
    return answer

print(generate_parenthesis(3))

from pprint import pprint
pprint(paths_in_grid(3))