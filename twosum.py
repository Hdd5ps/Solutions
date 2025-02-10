''' we are given an input array and sum target
we wanna find two indeces of the values that sum to the target
we are guarantted that there are exactly one solution
most easiest would be to check every combination of 2 values and see if they sum up to the target
we don't have to check every values, we have to find efficient way to takcle this problem
we don't want to repaeat anything, as it would be super inefficient
the runtime of this algorithm because it is bruteforce.
the worst case is n * each number (n)
worst case time complexity would be O(n**2)
Note: For each number for eg:, value we are looking for is the difference between the target and this value
so we are looking for the index of  4-1 = 3. So, that means this is the only value that we can add to 1 to be equal to target(4)
so we don't have to check every numbers. we just wanna know if the three exists.
The most easiest way to check would be to create hashmap of every value in our input array, so that we can instantly check if the value 3 exists.
in the hasmap, we are mapping each value to the index of each value.
index of 2 is 0
index of 1 is 1
index of 5 is 2
index of 3 is 3
now we could add every value of this array into the hashmap before we start iterating through it.
easier way to do it: if we add it the entire array into the hashmap initially, we would get to the value of 2 first right.
we wanna check the difference between target(4) and this value 2 which = 2 exists in our hashmap.
then we find 2 doest exist in our hashmap. we are not allowed to reuse the same one because they both would be the same index. can't use same value twice
so, we have to compaare the index current 2 and the 2 that is in our hashmap.
clever way: initally we say hashmap is empty. so, we get to the value 2 first, so we want to look for the difference 4-2 in our hasmap, our hasmap is empty we don't find 2
after, we visited this element, then we can add it to the hashmaps. now, that i am done with the first element
i am gonna add 2 to our hasmap and index gonna be zero.
now i am in array 1. 4-1 = 3. 3 is in array but not in hasmap. we add 1 to hasmpa index of 1 is 1
next is 5, 4-5=-1, add 5 to hasmpa with index 2, -1 also doesnpt exist in the hashmap
we move to the last value in the array
we check 4-3 = 1 exist in our hashmap. that value exist and its index is 1. now we foudn our 2 values that sum to the target.
now we wanna return their inde are gonna be 1 and 3.
the hashmap is only gonna have the value that come beforeit. but once we get to the second value, first value is gonna be inside hashmap.
since we only have to iterate throught the array once and we are adding each value to the hasmpa once, it is a constant time operation. and we are
checking if the value exists in the hashmpa which is also a constant time operation.
the time complexity therefore is big O(n). we are using extra memory right. the hasmpa isn't free.
memroy complexity is also big O(n) because we could potentially put every value to the hashmap
'''
Class twosum:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # value : index
    
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
