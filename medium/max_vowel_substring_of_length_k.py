class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowel_set = {'a','e','i','o','u'}
        vowel_count = 0
        count = 0
        for i in range(0,k):
            if s[i] in vowel_set:
                count += 1
        vowel_count = count
        for j in range(k,len(s)):
            if s[j] in vowel_set:
                count += 1
            if s[j-k] in vowel_set:
                count -= 1
            vowel_count = max(vowel_count,count)
        return vowel_count
