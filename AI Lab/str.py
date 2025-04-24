def compare_strings(str1, str2):
    if str1 == str2:
        return "Strings are equal"
    elif str1 < str2:
        return "First string is less than second"
    else:
        return "First string is greater than second"

# Example usage
print(compare_strings("apple", "banana"))   # Output: First string is less than second
print(compare_strings("hello", "hello"))    # Output: Strings are equal
print(compare_strings("zebra", "apple"))    # Output: First string is greater than second
