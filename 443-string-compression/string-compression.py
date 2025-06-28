class Solution:
    def compress(self, chars: List[str]) -> int:
        write, read = 0,0
        while read < len(chars):
            letter = chars[read]
            countOcc = 0
            while read < len(chars) and chars[read] == letter:
                countOcc += 1
                read += 1
            chars[write] = letter
            write += 1
            if countOcc > 1:
                for c in str(countOcc):
                    chars[write] = c
                    write += 1
        return write