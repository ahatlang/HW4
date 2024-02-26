#importsregion
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt
#endregion

#problemregion
"""
Step 1: Define function 1 & function 2
Step 2: Use 'fsolve' to find the unique roots of the two functions
Step 3: Find the points of intersection between function 1 & function 2
Step4: Create a graph to display points of intersection
"""
def func1(x):  #f(x) = x - 3*cos(x)
    return x - 3 * np.cos(x)

def func2(x):  #g(x) = cos(2x)*x^3.
    return np.cos(2 * x) * (x ** 3)

def func_intersection(x):
    """
    Define the function representing the difference between func1 and func2 to find intersections.
    """
    return func1(x) - func2(x)

def find_unique_roots(func, guesses, tol):  #chatgpt was used here
    """
    Find unique roots of a function given initial guesses and a tolerance for uniqueness.
    """
    unique_roots = []
    for guess in guesses:
        root = fsolve(func, guess)[0]
        #check uniqueness within the specified tolerance
        if not any(np.isclose(root, u_root, atol=tol) for u_root in unique_roots):
            unique_roots.append(root)
    #optionally, round the roots for cleaner output
    unique_roots = np.round(unique_roots, 5)
    return np.unique(unique_roots)

#setup for finding intersections
tolerance = 0.1  #I was getting a plethora of roots as that were very very close to eachother. A 'ignore' tolerance was set
initial_guesses = np.linspace(-10, 10, 400)  #range of initial guesses

#find unique intersection points
unique_intersections = find_unique_roots(func_intersection, initial_guesses, tolerance)
#endregion

#plottingregion
#plotting setup and execution
#chatgpt was used for this function
x_values = np.linspace(-10, 10, 400)
y1_values = func1(x_values)
y2_values = func2(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y1_values, label="f(x) = x - 3cos(x)")
plt.plot(x_values, y2_values, label="g(x) = cos(2x)x^3")
plt.scatter(unique_intersections, func1(unique_intersections), color='red', zorder=5, label='Intersections')

plt.title("Graph of f(x) and g(x) with Intersection Points")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

#set the y-axis limits to be from -100 to 100
plt.ylim(-100, 100)

plt.show()
#endregion

