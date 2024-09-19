def lagrange_interpolation(x, y, xp):
    yp = 0
    n = len(x)
    
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += p * y[i]
    
    return yp

# Задані точки
x_values = [-3, -2, 1, 3]
f_values = [-4, 19, -8, 14]

# Точки для обчислення
x_points = [-1.5, 0.5, 1.5, 2]

# Обчислення значень функції
f_approximations = [lagrange_interpolation(x_values, f_values, xp) for xp in x_points]

for i, xp in enumerate(x_points):
    print(f"f({xp}) ≈ {f_approximations[i]:.4f}")
