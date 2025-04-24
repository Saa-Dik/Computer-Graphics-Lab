# 6. Write a program using PROLOG LISP to reverse a list.
def reverse_list(lst):
    # Base case: empty list or single element
    if not lst:
        return []
    else:
        # Recursive step: reverse tail and append head to the end
        return reverse_list(lst[1:]) + [lst[0]]

# Test the function
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print("Original:", original_list)
print("Reversed:", reversed_list)
