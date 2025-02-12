'''
Given a string s containing just the characters '(', ')', '{', '}', '[', '];, determine if the input string is valid
An input string is valid if:
    1. Open brackets must be closed by the same type of brackets
    2. Open brackets must be closed in the correct order

    if its valid we can return true if not false

example: 1
input: s = "()"
Output = true

example: 2
input: s = "(){}[]"
Output = true

example: 3
input: s = "([)]" // not in order
Output = false

solution:
now, how do we create an algorithm for this problem. first thing we notice is that we have to start with opening parentheses (, {, or [
but we can't start with a closing parentheses like ), }, ]. this is never going to be valid.
once, we start with opening parentheses we can add as many opening parentheses as we want as long as we are closing them. ((()))
we have 4 open and 4 closing that come after it, they shoudl match other. As they match each, we cancel them out and remove them from our 
consideration or list. once we get to another closing parentheses we see if it is being applied to any opening parentheses, we can remove them as well.
we keep removing them until we are done. If we have empty list at the end, then we know we can return true because we closed all our opening parentheses.
Also, notice as we add closing parentheses [()], we have to remove from the beginning of our list. Now lets say after removing these we got 
[]. so, we are always gonna be removing from the top of the list or the top of the stack. Thats basically a hint for us to use a stack data structure.
Because as we are closing a parentheses ), we are always gonna be popping from the top. a closing parentheses is always gonna be matched to the most recent
opening parentheses. Lets, say we have these [{( opening parentheses in a row and we have ) right after that. 
How do we know they match each other (every closing with the correct opening) 
For eg: ) -> ( , ] -> [, and } -> {
this is basically gonna be our hashmap. this is gonna help us determine if a closing parentheses matches an open parentheses; basically the correct type
Lets, say we have this [{() this closing paretheses, we go up in our hashmap and check if this closing parentheses matches this open parentheses and see if it is in 
top of the stack, we can cross (pop) from the stack. same process repeats. Now, that we have empty list, that means all the parentheses match each other in the correct order.

FYI: this algorithm is big O(n), because we have to go through all the input character once. this is also taking big O(n) memory because we are using stack which could be upto the size of input n.
'''
class validParentheses:
    def validParentheses(self, s: str) -> bool:
        stack = [] 
        closeToOpen = { ")" : "(", "}" : "{", "]" : "["}

        # building the stack and popping from it
        for c in s: # iterating through every character in the input string
            if c in closeToOpen: # check if it is a closing parentheses
                if stack and stack[-1] == closeToOpen[c]: # in python stack[-1i is the last value we just added in the top of our stack; it is a closing parehteses we wanna make sure that our stack is not empty because we cannot cancel our closing parehthese to our empty stack and if the value at the top of our stack is the matching opening parentehses
                    stack.pop() # if these match each other, we can remove from the top of the stack and then continue going
                else: #if they don't match each other
                    return False
            else: #if we don't get a closing parenthese or get an opening paretheses
                stack.append(c) # we can take that character and add to out stack, we keep going
        
        # remember at the end once we gone throught, we can only return true if stack is empty
        return True if not stack else False