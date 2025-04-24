# 7. Write a program using PROLOG/LISP to implement Hill Climbing Algorithm. 
def f(x):
    return -x**2 + 10  # Peak at x=0

def get_neighbors(x, step=0.1):
    return [x - step, x + step]

def hill_climb(current, precision=0.001, step=0.1):
    current_value = f(current)
    neighbors = get_neighbors(current, step)
    neighbor_values = [f(n) for n in neighbors]

    max_value = max(neighbor_values)
    best_neighbor = neighbors[neighbor_values.index(max_value)]

    if max_value > current_value:
        return hill_climb(best_neighbor, precision, step)
    else:
        return current, current_value

# Start hill climbing from an initial point
start = 5
result = hill_climb(start)
print(f"Local maximum at x = {result[0]:.4f}, f(x) = {result[1]:.4f}")
