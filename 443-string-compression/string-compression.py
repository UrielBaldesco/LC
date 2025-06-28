class Solution:
    def compress(self, chars: List[str]) -> int:
        r, i = 0,0
        while i < len(chars):
            currChar = chars[i] #first instance of each section
            print(currChar)
            currOcc = 0
            while i < len(chars) and chars[i] == currChar:
                currOcc += 1
                i += 1
                print(currOcc, i)
            chars[r] = currChar #After counting, the character is written at index r:

            print('r', r)
            print('chars[r]', chars[r])
            r += 1
            if currOcc > 1:
                for c in str(currOcc):
                    chars[r] = c
                    r += 1        
        return r
