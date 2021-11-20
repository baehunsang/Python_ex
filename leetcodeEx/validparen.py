def isValid( s: str) -> bool:
        stack = []
        table = {')': '(', '}': '{', ']':'['}
        for char in s:
            if(char in table):
                t = stack.pop()
                if(table[char] != t):
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
        
print(isValid("([]){[]}"))
