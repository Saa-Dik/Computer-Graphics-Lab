# 1. Write a program using PROLOG/LISP for addition and multiplication of two numbers. 

def lisp_add(a, b):
    if b == 0:
        return a
    return lisp_add(a + 1, b - 1)

def lisp_multiply(a, b):
    if b == 0:
        return 0
    return lisp_add(a, lisp_multiply(a, b - 1))

# Example usage
print("LISP-style:")
print("Addition:", lisp_add(3, 4))
print("Multiplication:", lisp_multiply(3, 4))
