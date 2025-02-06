def solve(num_heads, num_legs):   
    x = (4 * num_heads - num_legs) // 2
    y = num_heads - x

    if x >= 0 and y >= 0 and 2 * x + 4 * y == num_legs:
        return f"Chickens: {x}, Rabbits: {y}"
    else:
        return "No solution exists"

print(solve(35, 94))