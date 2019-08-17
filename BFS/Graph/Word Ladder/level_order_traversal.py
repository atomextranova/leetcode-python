
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        char_dict = set('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(','))
        visited = set()
        queue = [start]
        transformation_length = 1
        while queue:
            length = len(queue)
            for _ in range(length):
                current_word = queue.pop(0)
                if current_word == end:
                    return transformation_length
                if current_word in visited:
                    continue
                visited.add(current_word)
                word_candidates = self.get_word_candidates(current_word, dict, char_dict, end)

                for word in word_candidates:
                    if word == end:
                        return transformation_length + 1
                    if word in visited:
                        continue
                    queue.append(word)
                    # Should not add here
                    # visited.add(current_word)
            transformation_length += 1
        return 0

    def get_word_candidates(self, word, dict, char_dict, end):
        word_candidates = []
        for index, s in enumerate(word):
            left_part = word[:index]
            righ_part = word[index+1:]
            word_part_list = [left_part, None, righ_part]
            for char in char_dict:
                word_part_list[1] = char
                word_candidate = ''.join(word_part_list)
                if word_candidate in dict or word_candidate == end:
                    word_candidates.append(word_candidate)
        return word_candidates

sol = Solution()
print(sol.ladderLength("hit",
"cog",
["hot","dot","dog","lot","log"]))