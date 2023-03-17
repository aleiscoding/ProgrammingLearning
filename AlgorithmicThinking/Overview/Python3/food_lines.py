MAX_LINES = 100

def shortest_line_index(lines, n):
    shortest = 0
    for j in range(1, n):
        if lines[j] < lines[shortest]:
            shortest = j
    return shortest

def solve(lines, n, m):
    for i in range(m):
        shortest = shortest_line_index(lines, n)
        print(lines[shortest])
        lines[shortest] += 1

def main():
    lines = [0] * MAX_LINES
    n, m = map(int, input().split())
    for i in range(n):
        lines[i] = int(input())
    solve(lines, n, m)
    return 0

main()
