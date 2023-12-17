# This file contains the Results class, which is used to store the results of the
# calculations and to print the best results.

class Results:
    def __init__(self):
        self.results_data = []

    def add(self, n, N, diff):
        self.results_data.append({'n': n, 'N': N, 'diff': diff})

    def sort(self):
        self.results_data.sort(key=lambda x: x['diff'])

    def print_best(self, n):
        for i in range(0, n):
            print(self.results_data[i])

# {'n': 225, 'N': 82184, 'diff': 5.921826868870994e-06}
            