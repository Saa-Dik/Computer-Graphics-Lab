# 5. Write a program using PROLOG/LISP whether an element is a member of list.
def member(ele, list):
    if not list:
        return False
    if ele == list[0]:
        return True
    return member(ele, list[1:])

# Example usage
print(member('b', ['a', 'b', 'c']))  
print(member('z', ['a', 'b', 'c']))  
