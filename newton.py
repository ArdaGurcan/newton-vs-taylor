from sympy import lambdify, diff, Symbol
from pynverse import inversefunc
from math import factorial, exp, sin, asin, cos, acos, tan, atan
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from sympy.core.sympify import sympify



x = Symbol('x')

t = 42
n = 5
p = 4

f = tan
f_inv = atan
# f = cos
# f_inv = inversefunc(f)


def d(func, n=1):
    if n == 0:
        return (func(x))

    for _ in range(int(n)):
        func = diff(func, x)

    return(lambdify(x, func))


def newtons_method(pred):
    return d(f)(f_inv(pred))*(t-f_inv(pred)) + pred


def taylor_approx(n):
    return (d(f, n)(f_inv(p))/factorial(n))*((x-f_inv(p))**n)


q = 0
y = [k for k in range(0, n+1)]

taylor = [p]
taylord = [0]
for i in range(0, n):
    q += taylor_approx(i)
    guess = lambdify(x, q)(t)
    print("Taylor guess", i+1, guess)
    a = str(guess)
    b = str(f(t))
    # b = str(1.60943791243)
    c = 0
    for j in range(min(len(a), len(b))):
        if(a[j] == b[j] and a[j] != "."):
            c+=1

    taylord.append(c)
    taylor.append(guess)

newton = [p]
newtond = [0]
for i in range(0, n):
    p = newtons_method(p)
    print("Newton guess", i+1, p)
    newton.append(p)
    a = str(p)
    b = str(f(t))
    # b = str(1.60943791243)
    c = 0
    for j in range(min(len(a), len(b))):
        if(a[j] == b[j] and a[j] != "."):
            c+=1

    newtond.append(c)

print("Actual answer", f(t))

# hide axes
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
plt.table(cellText=[[y[i],newton[i],taylor[i]] for i in range(n+1)],

                    colLabels=["Guess Number", "Newton's Method Approximation", "Taylor Series Approximation"],
                      loc='center',cellLoc='center')

fig.tight_layout()

# ax = plt.figure().gca()
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.plot(y,[f(t) for _ in range(len(y))], label="Actual Answer")
# plt.plot(y,taylord, label="Taylor Series Approximation")
# plt.plot(y,newtond, label="Newton's Method Approximation")
# plt.xlabel("Guess Number")
# plt.ylabel("Approximation Value")
# plt.title("The Approximations at Each Step for the Cube Root of 42")
# plt.title("Number of Correct Digits of Approximations at Each Step for the Cube Root of 42")
# plt.ylabel("Number of Correct Digits")
# ax.yaxis.set_major_locator(MaxNLocator(integer=True))

plt.legend()
plt.show()
