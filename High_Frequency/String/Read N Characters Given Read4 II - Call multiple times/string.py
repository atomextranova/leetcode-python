"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
from collections import deque


class Solution:

    def __init__(self):
        self.queue = deque()

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf_length = 0
        temp_buf = deque([''] * 4)
        while (buf_length < n):
            if not self.queue:
                count = read4(temp_buf)
                if count == 0:
                    break
                for i in range(count):
                    self.queue.append(temp_buf[i])
                continue

            buf[buf_length] = self.queue.popleft()
            buf_length += 1

        return buf_length