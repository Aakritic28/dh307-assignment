import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from scipy.optimize import curve_fit
file_path='all_marks_2024.csv'
data=pd.read_csv(file_path)


distribution_summary = {
    'mean': data['Marks'].mean(),
    'median': data['Marks'].median(),
    'variance': data['Marks'].var(),
    'standard_deviation': data['Marks'].std(),
}

k2, p_value=stats.normaltest(data['Marks'])

distribution_type="Non-normal"
if p_value >0.05:
    distribution_type="Normal"
else:
    if abs(distribution_summary['mean']- distribution_summary['variance'])< 0.1*distribution_summary['mean']:
        distribution_type="Poisson"

unique, counts=np.unique(data['Marks'], return_counts=True)

def Gauss(x, A, B): 
    y = A*np.exp(-1*B*x**2) 
    return y 
parameters, covariance = curve_fit(Gauss, unique, counts) 
  
fit_A = parameters[0] 
fit_B = parameters[1] 
  
fit_y = Gauss(unique, fit_A, fit_B) 
plt.plot(unique, counts, 'o', label='data') 
plt.plot(unique, fit_y, '-', label='fit') 
plt.legend()
plt.show()

mark_count=data['Marks'].value_counts().sort_index()
plt.figure(figsize=(12,6))
plt.plot(mark_count.index, mark_count.values, marker='o' )
plt.title('Number of Candidates vs. Marks Obtained in NEET-UG-2024')
plt.xlabel('Marks')
plt.ylabel('Number of Candidates')
plt.grid(True)
plt.show()