class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        #check, if lenght of s not prime, then s for sure is not valid
        #and we should return False
        if len(s)&1:
            return False

        # dictionary for linking oppening and closing brackets
        oppeningAndClosing = {'{':'}', '[':']', '(':')'}

        for char in s:
            #if char is oppening bracket we append it to the top of stack
            if char in oppeningAndClosing:
                stack.append(char)
            #if we meet closing bracket, we need to check, if we have oppened brackets in the stack
            elif len(stack) > 0:
                # if we actually have the oppened bracket in the stack, we check
                # is the last oppened bracket the same type as our closing
                if oppeningAndClosing[stack[-1]] == char:
                    # if we are the same, then just pop the top item from stack 
                    stack.pop(-1)
                else:
                    # if they are not the same, it means that the order of closing brackets is broken
                    return False
            else:
                # if stack length is 0, its means no oppening brackets in there
                # and we have we closing one... the order of closing brackets is broken
                return False
            
        # and we have one last option to check
        # some kind of checksum. if number of closing and oppening brackets were the same, we will have empty stack
        if len(stack) == 0:
            return True
        # if we had met more oppening brackets, than closing, we return False
        return False

    
sol = Solution()
print(sol.isValid("(("))
