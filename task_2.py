from collections import deque

def is_palindrome(text: str) -> bool:
    formatted_text = text.lower().replace(" ", "")
    char_deque = deque(formatted_text)

    while len(char_deque) > 1:
        left_char = char_deque.popleft()
        right_char = char_deque.pop()

        if left_char != right_char:
            return False   
         
    return True

# Example usage:
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Hello"))  # False