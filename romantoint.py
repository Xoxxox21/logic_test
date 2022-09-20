class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        hasil =0
        for i in range(len(s)):
            if i==0:
                hasil = hasil + symbol[s[i]]
            elif symbol[s[i]] > symbol[s[i-1]]:
                hasil = hasil - symbol[s[i-1]]
                hasil = hasil + (symbol[s[i]]-symbol[s[i-1]])
            else:
                hasil = hasil + symbol[s[i]]
        return hasil