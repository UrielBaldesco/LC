class Solution:
    def compress(self, chars: List[str]) -> int:
        write, read = 0,0
        while read < len(chars):
            letter = chars[read]
            count = 0
            while read < len(chars) and chars[read] == letter:
                read += 1
                count += 1
            chars[write] = letter
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        
        return write