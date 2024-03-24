from collections import defaultdict


def accountsMerge(accounts):
    names = {}
    graph = defaultdict(set)
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            graph[acc[1]].add(email)
            graph[email].add(acc[1])
            names[email] = name

    print(names)
    print("==================================")
    print(graph)


accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accountsMerge(accounts)