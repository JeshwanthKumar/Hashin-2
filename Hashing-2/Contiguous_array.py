#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0:-1}    #Initialize a hashmap with the first value as {0:-1}
        rSum = 0    #Initialize rSum to 0
        maxLength = 0   #Initialize maxLength to 0
        # result=[0,0]
        for i in range(len(nums)):  #Continue the loop to the length of nums
            if nums[i] == 0:    #If an element in the array is 0, then subtract rSum with -1
                rSum -= 1
            else:   #Else add tsUm with 1
                rSum += 1
            if rSum not in hashmap: #If rSum is not in hashmap, then add the value to hashmap
                hashmap[rSum] = i
            else:   #Else check if maxLength is less than or equal to the difference of i and hashmap[rSum], if true then change the maxLenght with the difference 
                # maxLength = max(maxLength, i-hashmap[rSum])
                 if (maxLength < (i-hashmap[rSum])):
                        maxLength = i-hashmap[rSum]
                        # result[1] = i+1
                        # result[0] = (i+1) -maxLength
                 
        # print(nums[result[0]:result[1]])        
        return maxLength    #Return the maxLength
        