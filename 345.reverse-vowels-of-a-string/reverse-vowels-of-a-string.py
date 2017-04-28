class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        
        """
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
    