
# Maintain a min stack
# To remove a number a
# Cost = it needs a cost a * b, where b >= a
# stack = [inf]
# Whenever stack[-1] < a, pop peek, right subtree cost = peek * a
# After end loop, pop the stack until size = 1
# to calculate left subtree cost