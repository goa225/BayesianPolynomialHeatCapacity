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

# Data for MnL1 0T
T1 = np.array([50.00075556,44.7468,40.04573333,35.83864444,32.0733,28.70317778,25.68755556,22.98875556,20.57365556,18.41221111,16.47863333,14.74746667,13.19798889,11.81146667,10.57077778,9.454156667,8.465425556,7.577906667,6.781743333,6.06772,5.430562222,4.860612222,4.348963333,3.893225556,3.483867778,3.117983333,2.790607778,2.496885556,2.234637778,2.000072222])
c1 = np.array([21.03945799,19.29454114,17.63113797,15.97764541,14.40078588,12.92545999,11.48201775,10.08420361,8.718347899,7.493877594,6.342200113,5.269263191,4.306759502,3.442032446,2.700307514,2.074423106,1.587467911,1.16252088,0.832115729,0.576882414,0.398843936,0.263849919,0.170160705,0.107435073,0.067991573,0.044227334,0.028637251,0.019465138,0.013949659,0.010717815])

# Data for MnL1 1T
T2 = np.array([50.00075556,44.7468,40.04573333,35.83864444,32.0733,28.70317778,25.68755556,22.98875556,20.57365556,18.41221111,16.47863333,14.74746667,13.19798889,11.81146667,10.57077778,9.454156667,8.465425556,7.577906667,6.781743333,6.06772,5.430562222,4.860612222,4.348963333,3.893225556,3.483867778,3.117983333,2.790607778,2.496885556,2.234637778,2.000072222])
c2 = np.array([21.50226557,19.29871468,17.69006214,16.06196568,14.44412591,12.9250035,11.48806833,10.0735125,8.71188147,7.468656602,6.304901413,5.244042386,4.295745811,3.460462678,2.735428982,2.152942611,1.649102426,1.24221978,0.934935603,0.699954857,0.542310434,0.441985171,0.392129757,0.377297418,0.391772599,0.42384523,0.472608927,0.526838566,0.586913391,0.648743636])

# Data for MnL1 2T
T3 = np.array([50.00013333, 44.7476, 40.0459, 35.83903333, 32.07423333, 28.70423333, 25.68773333, 22.98953333, 20.57386667, 18.41256667, 16.47856667, 14.74723333, 13.19773333, 11.81176667, 10.57053333, 9.453776667, 8.465123333, 7.577803333, 6.781243333, 6.069426667, 5.4291, 4.860393333, 4.349843333, 3.893393333, 3.483406667, 3.117996667, 2.790206667, 2.496883333, 2.234456667, 1.999953333])
c3 = np.array([21.55645099,19.27950175,17.67907483,16.06069311,14.43893861,12.93327638,11.50191642,10.0868871,8.746617467,7.47588197,6.336784009,5.318000625,4.384312203,3.554073206,2.85498956,2.288559015,1.818506039,1.45115909,1.178732439,0.974940385,0.848684252,0.789923843,0.765610303,0.768991479,0.793041854,0.812559702,0.83593619,0.842869636,0.845383883,0.836468892])

# Fit and plot data for MnL1 0T
T1_fitted, c1_fitted = fit_and_plot(T1, c1, 'MnL1 0T')

# Fit and plot data for MnL1 1T
T2_fitted, c2_fitted = fit_and_plot(T2, c2, 'MnL1 1T')

# Fit and plot data for MnL1 2T
T3_fitted, c3_fitted = fit_and_plot(T3, c3, 'MnL1 2T')


# Output the fitted data at the same x-values as the experimental data
for t, c in zip(T1_fitted, c1_fitted):
    print(f"T: {t}, Fitted Data: {c}")

for t, c in zip(T2_fitted, c2_fitted):
    print(f"T: {t}, Fitted Data: {c}")

for t, c in zip(T3_fitted, c3_fitted):
    print(f"T: {t}, Fitted Data: {c}")
    