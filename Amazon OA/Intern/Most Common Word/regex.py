import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_regex = r"([a-z]+)"
        # Used here re.I
        word_re = re.compile(word_regex, re.I)
        candidates = word_re.findall(paragraph.lower())
        valid = [candidate for candidate in candidates if candidate not in banned]
        return Counter(valid).most_common(1)[0][0]