from scipy.interpolate import barycentric_interpolate
from math import sin

x = np.linspace(-1, 1, 1000)
error = 1
n = 1
rzad = []
wynik = []
print("             Norma błędu   ", "     Badany rząd\n")

a = 1
fun_4 = lambda x, a: 1 / (1 + 2 * a * x ** 2)

# dla funkcji fun_4 = lambda x,a:  1/(1+2*a*x**2), funkcji analitycznej
while a <= 100:
    error = 1
    n = 1
    print('a=', a)
    while error > 0.00001:
        inn = 10 ** n  # interpolation node numbers
        x_i = np.array([np.cos(i * np.pi / inn) for i in range(inn + 1)])
        y_i = fun_4(x_i, a)  # funkcja jednokrotnie rozniczkowalna
        w_i = [np.power(-1, i) for i in range(inn + 1)]
        w_i[0] = 0.5
        w_i[inn] = 0.5 * w_i[inn]
        yimp = bar_inter_from_lecture(x_i, y_i, w_i, x)
        error = wek_norm(fun_4(x, a), yimp)
        wynik.append(error)
        rzad.append(n)
        print("      {:.25f}      {}".format(error, n))
        n += 1

        if a == 1:
            a *= 25
        if a >= 25:
            a *= 4
        print('tu doszedlem')
    fig = plt.figure()
    ax = plt.gca()  # co to znaczy??? gca co to robi i ax???
    ax.loglog(rzad, wynik, 'o', label='blad')
    ax.loglog([1, 1e3], [1, 1e-3], label='$n^{-1}$')
    ax.legend()
