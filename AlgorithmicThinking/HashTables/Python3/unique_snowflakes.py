# Same code but translated into python by me. it works me thinks!
SIZE = 100000

def identical_right(snow1, snow2, start):
    for offset in range(6):
        if (snow1[offset] != snow2[(start + offset) % 6]):
            return 0
    return 1

def identical_left(snow1, snow2, start):
    for offset in range(6):
        snow2_index = start- offset
        if (snow2_index < 0):
            snow2_index = snow2_index + 6
        if (snow1[offset] != snow2[snow2_index]):
            return 0
    return 1

def are_identical(snow1, snow2):
    for start in range(6):
        if (identical_right(snow1, snow2, start)):
            return 1
        if (identical_left(snow1, snow2, start)):
            return 1
    return 0

def code(snowflake):
    return sum(snowflake) % SIZE


class SnowflakeNode:
    def __init__(self, snowflake):
        self.snowflake = snowflake
        self.next = None

def identify_identical(snowflakes):
    for i in range(SIZE):
        node1 = snowflakes[i]
        while (node1 is not None):
            node2 = node1.next
            while (node2 is not None):
                if (are_identical(node1.snowflake, node2.snowflake)):
                    print("Twin snowflakes found.")
                    return
                
                node2 = node2.next
            node1 = node1.next
        
    print("No two snowflakes are alike.")

# Need main to give AC by Judge in DMOG website.

def main():
    snowflakes = [None] * SIZE
    n = int(input())
    for _ in range(n):
        snowflake = list(map(int, input().split()))
        snowflake_node = SnowflakeNode(snowflake)
        snowflake_code = code(snowflake)
        snowflake_node.next = snowflakes[snowflake_code]
        snowflakes[snowflake_code] = snowflake_node
    identify_identical(snowflakes)

if __name__ == '__main__':
    main()
