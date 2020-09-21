def substringk(s, k):
    if not s or k == 0:
        return []

    letter, result = {}, set()
    start = 0

    for i, char in enumerate(s):
        if char in letter:
            start = max(start, letter[char] + 1)
        letter[char] = i
        if i - start + 1 == k:
            result.add(s[start:i + 1])
            # Optional
            start += 1
    return sorted(result)


# ["abc", "bca", "cab"]
print(substringk("abcabc", 3) == sorted(["abc", "bca", "cab"]))

# ["bac", "cab"]
print(substringk(s="abacab", k=3) == sorted(["bac", "cab"]))
# ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
print(substringk(s="awaglknagawunagwkwagl", k=4) == sorted(["wagl", "aglk", "glkn",
                                                     "lkna", "knag", "gawu",
                                                     "awun", "wuna", "unag",
                                                     "nagw", "agwk", "kwag"]))
