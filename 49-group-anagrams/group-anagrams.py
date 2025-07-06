class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = collections.defaultdict(list)
        for word in strs:
            freqarr = [0] * 26
            for ch in word:
                freqarr[ ord(ch) - ord('a') ] += 1
            key = tuple(freqarr)
            res[key].append(word)
        
        return list(res.values())

'''
map:

key is a unique freq array (26 letters with a count of each letter), value is a list of words that match this

create a result map
iterate the original list
    create a new freq array for each word in the list of words
    iterate each character in each word 
        increment the ascii index of each letter 
        --> this creates a freq array that holds the freq of characters in each word
    in the result map, make the key a tuple of the freq array
        append the word that matches the freq array 
return result



'''