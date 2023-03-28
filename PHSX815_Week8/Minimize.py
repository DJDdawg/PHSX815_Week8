#Minimize a function using Scipy minimize packages

#import packages
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import sys

def quadratic(x, a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    squared = a*x**2 + b*x + c
    return squared
    
def quadraticextreme(x, a, b, c): #calculate critical point
    a = float(a)
    b = float(b)
    c = float(c)
    xextreme = -b/(2*a)
    return xextreme
    
def minofquadratic(x, a, b, c): #calculate minimum/maximum value
    a = float(a) 
    b = float(b)
    c = float(c)
    quadmin = -b*b/(4*a) + c
    return quadmin

if __name__ == "__main__":
    
    #initialize 
    lowerbound = -1
    upperbound = 1
    	
    a = 1 #must be positive in order for a minimum to exist, otherwise is a maximum.
    b = 1
    c = 1
    
    N = 1000
    	
    # read the user-provided seed from the command line
    if '-a' in sys.argv:
    	p = sys.argv.index('-a')
    	a = float(sys.argv[p+1])
        
    if '-b' in sys.argv:
        p = sys.argv.index('-b')
        b = float(sys.argv[p+1])
        
    if '-c' in sys.argv:
        p = sys.argv.index('-c')
        c = float(sys.argv[p+1])
    
    if '-lowerbound' in sys.argv:
        p = sys.argv.index('-lowerbound')
        lowerbound = float(sys.argv[p+1])
        
    if '-upperbound' in sys.argv:
        p = sys.argv.index('-upperbound')
        upperbound = float(sys.argv[p+1])
    
    if '-N' in sys.argv:
        p = sys.argv.index('-N')
        N = int(sys.argv[p+1])   
        
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   -a [number]	coefficient of quadratic term. Must be positive.")
        print ("   -b [number]  coefficient of linear term")
        print ("   -c [number]  y-intercept")
        print ("   -lowerbound [number]  Lower Bound of graph")
        print ("   -upperbound [number]  Upper Bound of graph")
        print ("   -N [number]  Number of points plotted in graph")
        print
        sys.exit(1)
    
    #create array of x-values
    x = np.linspace(lowerbound, upperbound, num=N)
        
    #calculate analytical solution
    analmin =  minofquadratic(x, a, b, c)
    analx = quadraticextreme(x, a, b, c)
    
    print(f"The analytical minimum of the quadratic curve is y = {analmin} at x = {analx}")
    
    #Scipy Minimize
    def f(x):
        return a*x**2 + b*x + c #constants are defined previously

    result = optimize.minimize_scalar(f) #minimize
    print(f'Scipi minimization was successful: {result.success}') # check if solver was successful

    x_min = result.x
    print(f'x-value found to minimize function: {x_min}')
    print(f'minimal value: {f(x_min)}')

    #plot function
    plt.plot(x, quadratic(x, a, b, c), label = f'curve $f(x) = ax^2 + bx + c$') 
    plt.plot(analx, analmin, color = 'red', marker = 'o', label = 'analytical minimum point')
    plt.plot(x_min, f(x_min), color = 'green', marker = 'v', label = 'numerical minimum point')
    
    plt.legend(loc = 'upper left')
    
    plt.xlabel('x')
    plt.ylabel('f(x)') 
    plt.title('Minimum of a Quadratic Curve')
    
    plt.grid()
    plt.show()
