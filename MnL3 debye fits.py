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

# Data for MnL3 0T
T1 = np.array([50.00113333,44.74716667,40.0461,35.8388,32.07336667,28.704,25.68843333,22.99006667,20.57416667,18.413,16.47863333,14.74753333,13.19783333,11.81173333,10.57116667,9.457753333,8.46604,7.57405,6.78209,6.068126667,5.43206,4.86179,4.35149,3.89323,3.48371,3.117353333,2.790136667,2.49726,2.234646667,1.999886667])
c1 = np.array([23.68672539,21.48451587,19.75555147,17.90310835,16.03951563,14.31880846,12.49086775,10.84076252,9.291742089,7.82713416,6.470248143,5.317581374,4.361596176,3.471058611,2.745152534,2.111278569,1.606995162,1.199707489,0.881104523,0.638323971,0.448429095,0.309841585,0.214558989,0.1498001,0.104233063,0.072109702,0.051638133,0.038522527,0.030277484,0.025514635])

# Data for MnL3 1T
T2 = np.array([50.00113333,44.74716667,40.0461,35.8388,32.07336667,28.704,25.68843333,22.99006667,20.57416667,18.413,16.47863333,14.74753333,13.19783333,11.81173333,10.57116667,9.457753333,8.46604,7.57405,6.78209,6.068126667,5.43206,4.86179,4.35149,3.89323,3.48371,3.117353333,2.790136667,2.49726,2.234646667,1.999886667])
c2 = np.array([24.3732621,21.50529249,19.81339803,18.12413739,16.12683833,14.31292097,12.47644822,10.81079974,9.252698124,7.796080669,6.371847344,5.246440557,4.300782378,3.46688373,2.773207964,2.204131985,1.66765353,1.276130382,0.974617277,0.759285443,0.605497334,0.500230714,0.441398981,0.419723959,0.426107836,0.449177138,0.494305417,0.546628891,0.60468064,0.663509495])

# Data for MnL3 2T
T3 = np.array([50.00113333,44.74716667,40.0461,35.8388,32.07336667,28.704,25.68843333,22.99006667,20.57416667,18.413,16.47863333,14.74753333,13.19783333,11.81173333,10.57116667,9.457753333,8.46604,7.57405,6.78209,6.068126667,5.43206,4.86179,4.35149,3.89323,3.48371,3.117353333,2.790136667,2.49726,2.234646667,1.999886667])
c3 = np.array([24.38516226,21.49182003,19.8141418,18.07785493,16.12257949,14.33625327,12.47292668,10.81550781,9.222705515,7.836171625,6.393453287,5.336145311,4.404541175,3.559129502,2.898644318,2.350557847,1.830432082,1.475053617,1.214565426,1.032270433,0.900976955,0.834772514,0.8158133,0.817021089,0.831624721,0.843038508,0.861743306,0.870283462,0.867670798,0.856097128])

# Fit and plot data for MnL3 0T
T1_fitted, c1_fitted = fit_and_plot(T1, c1, 'MnL3 0T')

# Fit and plot data for MnL3 1T
T2_fitted, c2_fitted = fit_and_plot(T2, c2, 'MnL3 1T')

# Fit and plot data for MnL3 2T
T3_fitted, c3_fitted = fit_and_plot(T3, c3, 'MnL3 2T')


# Output the fitted data at the same x-values as the experimental data
for t, c in zip(T1_fitted, c1_fitted):
    print(f"T: {t}, Fitted Data: {c}")

for t, c in zip(T2_fitted, c2_fitted):
    print(f"T: {t}, Fitted Data: {c}")

for t, c in zip(T3_fitted, c3_fitted):
    print(f"T: {t}, Fitted Data: {c}")
    