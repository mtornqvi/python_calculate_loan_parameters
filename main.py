# the number of outstanding loan installments (min, max)
from Results import Results
import numpy as np

nmin = 216
nmax = 217
# the amount of the remaining loan (euros) (min, max)
Nmin = 79300.00
Nmax = 80000.00

# the monthly interest rate
p=(4.98/100)/12

# the monthly payment
A=562.66

# Prepare the results object with fields: n, N, diff
results = Results()

# Iterate 
for n in range(nmin,nmax, 1):
    for N in np.arange(Nmin, Nmax, 0.001):
       calc = ((1+p)**n)*p*N/(((1+p)**n)-1)
       results.add(n, N, abs(calc-A))

results.sort()
results.print_best(5)

