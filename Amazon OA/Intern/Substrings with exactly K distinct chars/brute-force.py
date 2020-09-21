
def helper(string, k):
    if k == 0:
        return 0

    length = len(string)
    result = []
    for i, char in enumerate(string):
        s = set()
        s.add(char)

        for j in range(i, length):
            new_char = string[j]
            s.add(new_char)
            if len(s) == k:
                result.append(string[i:j+1])
            if len(s) > k:
                break

    return len(result)

print(helper("pqpqs", 2))
print(helper("aabab", 3))