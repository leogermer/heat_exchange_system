from csv import DictReader
from typing import List
from math import pi
import pylab
from runge_kutta import RK4

parameter: List[float] = []  # list which will contain all operation constants of the project


with open('data.csv') as archive:
    reader_csv = DictReader(archive, delimiter=',')
    for line in reader_csv:
        parameter.append(float(line['Value']))

# Unpacking the list with the constants in a csv file as example (data.csv)
m, rho, cp, ct, vis, a_pool, v_pool, a_plate, v_plate, d_plate, t_inf, t_plate, t_oper, t0_p, t0_hc = parameter

m = m/3600  # Mass flow in kg/s

# Determining the convective coeficientes

as_plate = pi*(d_plate**2)/4    # Section area of the heat exchanger
u = m/(rho*as_plate)      # Water flow velocity inside the heat exchanger
nre = rho*u*d_plate/vis   # Reynolds Number
npr = cp*vis/ct     # Prandtl Number
hconv_n = 5     # Natural Convection Coeficient (standard: aproximated)
gnu = 0.037*(nre**0.8)*(npr**0.3)    # Nusselt Number   (standard: Nusselt empiric equations for plates)
hconv_f = gnu*ct/d_plate      # Forced Convection Coeficient

# System Ordinary Differencial Equations (energy balances):
# with tp as pool temperature and thc as heat exchanger temperature.

dt1 = lambda t, thc, tp: (1/(rho*v_pool*cp)) * (m*cp*(thc-tp) - hconv_n*a_pool*(tp-t_inf))
dt2 = lambda t, thc, tp: (1/(rho*v_pool*cp)) * (m*cp*(tp-thc) + hconv_f*a_plate*(t_plate-thc))

sol = RK4(dt2, dt1)  # Solving with numeric method Runge-Kutta 4th Order
t, y = sol.solve([t0_p, t0_hc], 1, t_oper*3600)  # ([Initial paramaters], step size, total time (seconds))

pylab.grid()
pylab.plot(t, y[0], label='Heat Exchanger Temperature')
pylab.plot(t, y[1], label='Pool Temperature')
pylab.title('Heat Exchange System Solution')
pylab.legend(loc='lower right')
pylab.xlabel("Time (hours)")
pylab.ylabel("Temperatures (°C)")
pylab.show()
