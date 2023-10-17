import numpy as np
from scipy.stats import norm
from sklearn.mixture import GaussianMixture
from matplotlib import pyplot as plt

data = [22.2, 15.1, 15.9, 30.7, 16.2, 41.0, 40.3, 35.5, 34.3, 52.3, 42.2, 25.2, 17.3, 54.6, 40.4, 32.6, 24.0, 22.3, 30.9, 37.0, 21.1, 23.7, 19.7, 21.0, 16.4, 34.3, 18.1, 26.8, 12.1, 7.3, 15.5, 10.7, 59.4, 30.5, 8.0, 44.0, 27.3, 16.0, 12.4, 18.1, 18.1, 34.2, 10.3, 33.8, 34.2, 0.8, 32.2, 11.8, 26.1, 24.1]
data = np.array(data)
# # Generate artificial data with two Gaussian components
# np.random.seed(0)
# data = np.concatenate([np.random.normal(0, 1, 50), np.random.normal(5, 1, 50)])

# Fit a Gaussian mixture model using the EM algorithm
model = GaussianMixture(n_components=2)
model.fit(data.reshape(-1, 1))

# Print the estimated means and covariance matrices
print("Means:", model.means_)
print("Covariances:", model.covariances_)
xlst = np.linspace(min(data), max(data), 1000)
print(xlst)
normal = norm.ppf(xlst, model.means_, model.covariances_)
print(normal[0])
# fig , ax = plt.subplots()
# ax.plot(xlst, normal)
# plt.show()
