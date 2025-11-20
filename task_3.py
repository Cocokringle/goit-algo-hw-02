def is_symmetric(expression: str):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)

        elif char in closing_brackets:
            if not stack:
                return 'Is not symmetric'
            
            top_element = stack.pop()

            if bracket_map[char] != top_element:
                return 'Is not symmetric'

    if not stack:
        return 'Is symmetric'
    else:
        return 'Is not symmetric'
    

# Example usage:
examples = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}:",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for text in examples:
    result = is_symmetric(text)
    print(f"{text} {result}") 