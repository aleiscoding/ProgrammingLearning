import sys

NUM_BITS = 17
WORD_LENGTH = 16

def oaat(key, length, bits):
    hash = 0
    for i in range(length):
        hash += ord(key[i])
        hash += (hash << 10)
        hash ^= (hash >> 6)
    hash += (hash << 3)
    hash ^= (hash >> 11)
    hash += (hash << 15)
    return hash & ((1 << bits) - 1)

def read_line():
    line = sys.stdin.readline().strip()
    return line

class WordNode:
    def __init__(self):
        self.word = None
        self.next = None

def in_hash_table(hash_table, find, find_len):
    word_code = oaat(find, find_len, NUM_BITS)
    wordptr = hash_table[word_code]
    while wordptr:
        if len(wordptr.word) == find_len and wordptr.word[:find_len] == find:
            return True
        wordptr = wordptr.next
    return False

def identify_compound_words(words, hash_table, total_words):
    for i in range(total_words):
        word = words[i]
        length = len(word)
        for j in range(1, length):
            if in_hash_table(hash_table, word[:j], j) and \
            in_hash_table(hash_table, word[j:], length-j):
                print(word)
                break

def main():
    words = [None] * (1 << NUM_BITS)
    hash_table = [None] * (1 << NUM_BITS)
    total = 0
    word = read_line()
    while word:
        words[total] = word
        wordptr = WordNode()
        length = len(word)
        word_code = oaat(word, length, NUM_BITS)
        wordptr.word = words[total]
        wordptr.next = hash_table[word_code]
        hash_table[word_code] = wordptr
        word = read_line()
        total += 1
    identify_compound_words(words, hash_table, total)

if __name__ == '__main__':
    main()
