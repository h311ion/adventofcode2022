import heapq
import sys

if __name__ == '__main__':
    # file = open(sys.path[0] + "/day1test.txt")
    file = open(sys.path[0] + "/day1.txt")

    q = []

    line = file.readline()
    maximum, current = 0, 0
    while line != "":
        trim_line = line.rstrip()
        if trim_line == "":
            heapq.heappush(q, current)
            if len(q) > 3:
                heapq.heappop(q)
            current = 0
        else:
            current += int(trim_line)
        line = file.readline()

    heapq.heappush(q, current)
    if len(q) > 3:
        heapq.heappop(q)

    q.sort()

    print(f"first: %d\t second: %d" % (q[-1], sum(q)))
