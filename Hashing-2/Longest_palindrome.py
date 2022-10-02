#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        hashset = set()     #Initialize a hashset as hashset
        count = 0   #Initialize count to 0
        
        for char in s:  #Continue the loop for all the characters in s
            if char not in hashset: #If the char is not in hashset, then add the char to hashset
                hashset.add(char)
            else:   #Else remove the char from the hashset and increment count by adding 2
                hashset.remove(char)
                count += 2
                
        if len(hashset) != 0:   #If the lenght of hashet is not equal to add 1 to the count
            count += 1
        return count    #Return count