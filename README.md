# PI calculator
This project was made during PI day to test a very expensive method to determine the value of PI in a couple of languages.

This method uses a calculation with a square within a circle and determine how many pixels are within the circle. It evaluates all the spots in one run. Usually this is done using the montecarlo method where a random spot is determined on each run and the calculation continues  indefinitly.

## Languages
I wanted to test the method and the performance on a couple of programming language. So I build the calculation code (roughly 30 LOC) in the following languages:

- Node js (javascript)
- PHP
- Python

All the code is done using core libraries. So nothing added to that. Performance wise the calculation is done the quickest in Node.js, beating PHP to second place and Python to third. 

I might do a couple of other strategies in the future. These could be tested:

- Monte carlo method
- Gregory-Leibniz series
- Nilakantha series

ref: https://www.wikihow.com/Calculate-Pi
