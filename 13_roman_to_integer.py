class Solution:
    def romanToInt(self, s):
        self.s = s

        equiv = {
                'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
                }
        current = 0
        result = 0

        for lett in range(len(s)):
            if s[lett] not in equiv:
                return 'Please give valid roman numerals.'

            else:
                if lett == len(s)-1:
                    current = equiv[s[lett]]
                elif equiv[s[lett]] >= equiv[s[lett+1]]:
                    current = equiv[s[lett]]
                else:
                    current = 0-equiv[s[lett]]

                result += current

        return result
