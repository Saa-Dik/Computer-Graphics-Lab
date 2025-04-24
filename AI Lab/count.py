# 4. Write a program using PROLOG/LIST to count number of elements in a list.
def count(list):
    if not list:
        return 0
    return 1 + count(list[1:])

# Example usage
print(count(['a', 'b', 'c', 'd'])) 