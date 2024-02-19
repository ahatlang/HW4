#functionregion
def improved_euler_method(f, g, x0, y0, v0, h, x_end):
    """
    Step 1: solve a second-order ODE w/ improved Euler method
    :param f: derivative function y, dy/dx
    :param g: derivative of function v, dv/dx (where v = dy/dx)
    :param x0: initial condition
    :param y0: initial condition
    :param v0: initial condition
    :param h: step size
    :param x_end: value of desired x
    :return: values of x,y, and v
    """
    x = x0
    y = y0
    v = v0
    while x < x_end:
        #predictors
        yp = y + h * f(x, y, v)
        vp = v + h * g(x, y, v)

        #correctors
        y += h * (f(x, y, v) + f(x + h, yp, vp)) / 2
        v += h * (g(x, y, v) + g(x + h, yp, vp)) / 2
        x += h
    return y, v


def runge_kutta_method(f, g, x0, y0, v0, h, x_end):
    """
    Step 2: solve a second-order ODE w/ Runge-Kutta method
    :param f: derivative function y, dy/dx
    :param g: derivative of function v, dv/dx (where v = dy/dx)
    :param x0: initial condition
    :param y0: initial condition
    :param v0: initial condition
    :param h: step size
    :param x_end: value of desired x
    :return: values of x,y, and v
    """
    x = x0
    y = y0
    v = v0
    while x < x_end:
        #compute slopes
        k1_y = h * f(x, y, v)
        k1_v = h * g(x, y, v)

        k2_y = h * f(x + 0.5 * h, y + 0.5 * k1_y, v + 0.5 * k1_v)
        k2_v = h * g(x + 0.5 * h, y + 0.5 * k1_y, v + 0.5 * k1_v)

        k3_y = h * f(x + 0.5 * h, y + 0.5 * k2_y, v + 0.5 * k2_v)
        k3_v = h * g(x + 0.5 * h, y + 0.5 * k2_y, v + 0.5 * k2_v)

        k4_y = h * f(x + h, y + k3_y, v + k3_v)
        k4_v = h * g(x + h, y + k3_y, v + k3_v)

        #update y and v using weighted avg slopes
        y += (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
        v += (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6
        x += h
    return y, v


#defining the ODE system
def f(x, y, v):
    """
    Step 3: defines derivative function of y dy/dx
    for this dy/dx = v
    """
    return v


def g(x, y, v):
    """
    Step 4: defines derivative function v dv/dx
    for this dv/dx = y + x
    """
    return y + x
#endregion

#print/interfaceregion
#chatgpt was used for this section
print("For the initial value problem y’’- y = x")

#requesting initial conditions and step size from the user
y0 = float(input("Enter the value of y at x=0: "))
v0 = float(input("Enter the value of y’ at x=0: "))
h = float(input("Enter the step size for the numerical solution: "))

#loop to allow user to query multiple x values
continue_calculation = 'Y'
while continue_calculation.upper() == 'Y':
    x_end = float(input("At what value of x do you want to know y and y’? "))

    y_improved_euler, v_improved_euler = improved_euler_method(f, g, 0, y0, v0, h, x_end)
    y_runge_kutta, v_runge_kutta = runge_kutta_method(f, g, 0, y0, v0, h, x_end)

    print(f"At x={x_end:.3f}")
    print(f"For the improved Euler method: y={y_improved_euler:.3f}, and y’={v_improved_euler:.3f}")
    print(f"For the Runge-Kutta method: y={y_runge_kutta:.3f}, and y’={v_runge_kutta:.3f}")

    continue_calculation = input("Do you want to compute at a different x? (Y/N) ")
#endregion
