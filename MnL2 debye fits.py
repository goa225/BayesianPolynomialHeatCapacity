from matplotlib import pyplot
import numpy as np
from scipy import integrate
from scipy.optimize import curve_fit
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Constants
R = 8.314

# Define the fit equation
def func(T, T_d):
    fn = lambda y: y**4 * np.exp(y) / (np.exp(y) - 1)**2
    debye_int = np.array([integrate.quad(fn, 0, T_d / t)[0] for t in T])
    debye = 9 * R * (T / T_d)**3 * debye_int
    return debye

# Define a function to fit and plot data for a given set of T and c
def fit_and_plot(T, c, title):
    coefs, _ = curve_fit(func, T, c)
    print(f"Fitted T_d for {title}:", coefs[0])
    
    # Plot on linear scale
    fitted_data = func(T, *coefs)
    plt.plot(T, fitted_data, label='Fitted Curve')
    pyplot.scatter(T, c, label='Experimental Data')
    pyplot.xlabel('$T [K]$')
    pyplot.ylabel('$C$')
    pyplot.legend()
    pyplot.title(title)
    plt.show()
    
    # Plot on log scales
    T_fit = np.linspace(min(T), max(T), 1000)
    c_fit = func(T_fit, *coefs)
    plt.loglog(T_fit, c_fit, label='Fitted Curve')
    pyplot.scatter(T, c, label='Experimental Data')
    pyplot.xlabel('$T [K]$')
    pyplot.ylabel('$C$')
    pyplot.legend()
    pyplot.title(f'Log-log {title}')
    plt.show()

    return T, fitted_data

# Data for MnL2 0T
T1 = np.array([50.00013333, 44.7476, 40.0459, 35.83903333, 32.07423333, 28.70423333, 25.68773333, 22.98953333, 20.57386667, 18.41256667, 16.47856667, 14.74723333, 13.19773333, 11.81176667, 10.57053333, 9.453776667, 8.465123333, 7.577803333, 6.781243333, 6.069426667, 5.4291, 4.860393333, 4.349843333, 3.893393333, 3.483406667, 3.117996667, 2.790206667, 2.496883333, 2.234456667, 1.999953333])
c1 = np.array([22.08379086, 20.07544981, 18.23170495, 16.41185425, 14.68717889, 12.93916982, 11.3211065, 9.746009588, 8.24973166, 6.848170978, 5.583297233, 4.460193436, 3.505323166, 2.709883848, 2.073215444, 1.544077915, 1.155962561, 0.850369369, 0.617182014, 0.448046081, 0.312930811, 0.217806486, 0.150428755, 0.104207859, 0.071028275, 0.049123353, 0.034898911, 0.026462842, 0.021706581, 0.019327093])

# Data for MnL2 1T
T2 = np.array([50.00013333, 44.7476, 40.0459, 35.83903333, 32.07423333, 28.70423333, 25.68773333, 22.98953333, 20.57386667, 18.41256667, 16.47856667, 14.74723333, 13.19773333, 11.81176667, 10.57053333, 9.453776667, 8.465123333, 7.577803333, 6.781243333, 6.069426667, 5.4291, 4.860393333, 4.349843333, 3.893393333, 3.483406667, 3.117996667, 2.790206667, 2.496883333, 2.234456667, 1.999953333])
c2 = np.array([22.32425225,20.05745109,18.17458308,16.50164871,14.72597645,12.96340695,11.32102381,9.738845431,8.244449356,6.828043629,5.566602124,4.459512613,3.508599871,2.728669176,2.111835006,1.618590296,1.225520508,0.93939529,0.726219112,0.581305212,0.474762477,0.414500103,0.390630682,0.395066403,0.416461956,0.453552291,0.507283945,0.568929073,0.63356805,0.697586036])

# Data for MnL2 2T
T3 = np.array([50.00013333, 44.7476, 40.0459, 35.83903333, 32.07423333, 28.70423333, 25.68773333, 22.98953333, 20.57386667, 18.41256667, 16.47856667, 14.74723333, 13.19773333, 11.81176667, 10.57053333, 9.453776667, 8.465123333, 7.577803333, 6.781243333, 6.069426667, 5.4291, 4.860393333, 4.349843333, 3.893393333, 3.483406667, 3.117996667, 2.790206667, 2.496883333, 2.234456667, 1.999953333])
c3 = np.array([22.32028121,20.0680592,18.26682928,16.42616133,14.73824884,12.97641506,11.34301017,9.759938996,8.281013771,6.843522394,5.606813642,4.546925547,3.605781338,2.832403411,2.241851094,1.770825341,1.408344485,1.151562857,0.983480766,0.866808958,0.802827349,0.782061577,0.790649356,0.815162941,0.848954421,0.874176088,0.901040296,0.917716248,0.918310489,0.909441776])

# Fit and plot data for MnL2 0T
T1_fitted, c1_fitted = fit_and_plot(T1, c1, 'MnL2 0T')

# Fit and plot data for MnL2 1T
T2_fitted, c2_fitted = fit_and_plot(T2, c2, 'MnL2 1T')

# Fit and plot data for MnL2 2T
T3_fitted, c3_fitted = fit_and_plot(T3, c3, 'MnL2 2T')


# Output the fitted data at the same x-values as the experimental data
for t, c in zip(T1_fitted, c1_fitted):
    print(f"T: {t}, Fitted Data: {c}")

for t, c in zip(T2_fitted, c2_fitted):
    print(f"T: {t}, Fitted Data: {c}")

for t, c in zip(T3_fitted, c3_fitted):
    print(f"T: {t}, Fitted Data: {c}")
    