class HelloWorld {
    static void Main() {
        Console.WriteLine("pqpqs k = 2 :" + SubstringWithKDistinctChars("pqpqs",2));
        Console.WriteLine("aabab k = 3 :" + SubstringWithKDistinctChars("aabab",3));
    }

    public static int SubstringWithKDistinctChars(string s, int K)
    {
        char[] A = s.ToCharArray();
        int left = 0, right = 0;
        Dictionary<char, int> numCount = new Dictionary<char, int>();
        int distinct = 0;
        int result = 0;
        int prefix = 0;
        while(right < A.Length)
        {
            if(numCount.ContainsKey(A[right]) && numCount[A[right]] != 0)
                numCount[A[right]]++;
            else
            {
                distinct++;
                numCount[A[right]] = 1;
            }

            if(distinct > K) //increment left pointer
            {
                numCount[A[left]]--;
                prefix = 0; // resetting the prefix since previous elements can not be used in next subset to keep k distinct elements
                distinct--;
                left++;
            }
            while(numCount[A[left]] > 1)
            {
                numCount[A[left]]--;
                left++;
                prefix++;
            }
            if(distinct == K)
                result += 1 + prefix;

            right++;
        }
        return result;
    }
}