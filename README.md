Simulation of a heat exchanger in a photovoltaic/pool system
======================
![alt text](https://www.imagemhost.com.br/images/2020/07/28/grafico.md.png)




This is an implementation of the fourth-order Runge-Kutta method
to solve systems of ODEs for a specific case:

A system of heat exchange, envolving three components: pool, heat exchanger, photovoltaic plate.

Particular Hypotesis Considered:

- The pool looses energy by natural convection;
- The heat exchanger looses energy by forced convection;
- The system recicurlates back from the pool to the heat exchanger.

Differential Equations to solve:

![alt text](https://www.imagemhost.com.br/images/2020/07/28/diff.png)

The idea is that the heat exchanger is glued under the solar plate and heats up the inside flowing water.
That water will heat up a pool and will recirculate back to the heat exchanger.

This software works extracting data from a csv file to predict temperature behaviour of
the pool and the heat exchanger plotted against time.

Notes:
-The temperature of the photovoltaic plate is set to 35ºC throughout the simulation.
-The file containing the data of your paramethers must be in csv format.

========================

Technologies Used:
- Python 3 (language)
- CSV files (storaging parameters)
- matplotlib (plotting)
- OOP (encapsulation of numerical method)

=========================
Feel free to use and adapt to your case.

To run this program you should have Python 3+ installed as shown in the link below:
(`https://realpython.com/installing-python/#step-1-download-the-python-3-installer`)

with the following modules:
-matoplotlib -> `pip install matplotlib`



Feel free to use and adapt to your case.
