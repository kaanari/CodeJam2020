T = int(input())
answer = []

for t in range(T):

    events = []
    n = int(input())
    event1 = 0
    event2 = 0
    str = ["" for x in range(n)]
    for i in range(n):
        start, end = map(int, input().split())
        events.append((start, i, end))

    events.sort(key=lambda x: x[0])

    for start, i, end in events:

        if (event1 <= start):
            event1 = end
            str[i] = "J"

        elif (event2 <= start):
            event2 = end
            str[i] = "C"

        else:
            str = "IMPOSSIBLE"
            break

    answer.append("".join(str))

for i in range(T):
    print("Case #{}: {}".format(i + 1, answer[i]))