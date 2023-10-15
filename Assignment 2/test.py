# %%
import numpy as np
import matplotlib.pyplot as plt

# Set parameters
alpha = 1.612
xmin = 1
num_samples = 3409

# Generate random samples
samples = (np.random.pareto(alpha, num_samples) + 1) 

# Plot the samples
_ = plt.hist(samples, bins=2, density=True)
plt.title(f'Power Law Distribution (α={alpha}, xmin={xmin})')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.show()

# %%
