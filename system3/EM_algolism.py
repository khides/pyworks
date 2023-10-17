from matplotlib import pyplot as plt
import numpy as np
import japanize_matplotlib

data = [22.2, 15.1, 15.9, 30.7, 16.2, 41.0, 40.3, 35.5, 34.3, 52.3, 42.2, 25.2, 17.3, 54.6, 40.4, 32.6, 24.0, 22.3, 30.9, 37.0, 21.1, 23.7, 19.7, 21.0, 16.4, 34.3, 18.1, 26.8, 12.1, 7.3, 15.5, 10.7, 59.4, 30.5, 8.0, 44.0, 27.3, 16.0, 12.4, 18.1, 18.1, 34.2, 10.3, 33.8, 34.2, 0.8, 32.2, 11.8, 26.1, 24.1]
bins = 10


fig, ax = plt.subplots()
ax.hist(data, bins=bins)
ax.set_xlabel("ボール投げ記録")
ax.set_ylabel("人数")
ax.set_title("ボール投げ記録の分布")
ax.grid(False)
plt.show()




def gauss(x, mu, sigma):
    return 1 / np.sqrt(2 * np.pi * sigma**2) * np.exp(-(x - mu)**2 / (2 * sigma**2))

def ll(theta, data): #　対数尤度関数
    alpha_F = theta[0]
    mu_F = theta[1]
    mu_M = theta[2]
    sigma_F = theta[3]
    sigma_M = theta[4]
    def p(x):
        return (1 - alpha_F) * gauss(x, mu_M, sigma_M) + alpha_F * gauss(x, mu_F, sigma_F)

    LL = 0.0
    for record in data:
        LL -= np.log(p(record))

    return LL

data_max = max(data)
data_min = min(data)

def visualize(x, y, label, method_name): # 可視化
    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    ax.hist(data, bins=10)
    for i in range(len(y)):
        ax2.plot(x, y[i], label=label[i])
    ax2.legend(loc="upper right")
    ax2.set_xlim([data_min, data_max])
    ax.set_xlabel("score [m]")
    ax.set_ylabel("num of people")
    ax2.set_ylabel("num of people (estimated)")
    ax.set_title(f"estimated distribution ({method_name})")
    ax.grid(False)
    ax2.grid(False)
    plt.show()

def get_optimized_y(ml_value, x):
    y_F = ml_value.x[0] * np.array([gauss(x_, ml_value.x[1], ml_value.x[3]) for x_ in x])
    y_M = (1 - ml_value.x[0]) * np.array([gauss(x_, ml_value.x[2], ml_value.x[4]) for x_ in x])
    y = y_F + y_M
    return y_F, y_M, y
    
    
from scipy import optimize

theta_0_ = [0.25, 15.0, 32.0, 4.0, 13.0] # 初期値
bounds = [(0.0, 1.0), (5.0, 25.0), (20.0, 45.0), (0.1, 30.0), (0.1, 30.0)] # 定義域の制約

x = np.linspace(data_min, data_max, int(1e4))


method = ["Nelder-Mead", "Powell", "L-BFGS-B", "TNC", "SLSQP", "trust-constr"]
for m in method:
    ml_value = optimize.minimize(fun=ll, x0=theta_0_, method=m, bounds=bounds, args=data)
    print(f"{m}: {ml_value.x}, {ml_value.fun}")
    y_F, y_M, y = get_optimized_y(ml_value, x)
    visualize(x=x, y=[y_F, y_M, y], label=["Female", "Male", "Mixed"], method_name=m)


ml_value = optimize.differential_evolution(func=ll, bounds=bounds, maxiter=100, args=[data])
print(f"differential_evolution: {ml_value.x}, {ml_value.fun}")
y_F, y_M, y = get_optimized_y(ml_value, x)
visualize(x=x, y=[y_F, y_M, y], label=["Female", "Male", "Mixed"], method_name="differential_evolution")

ml_value = optimize.dual_annealing(func=ll, bounds=bounds, maxiter=100, x0=theta_0_, args=[data])
print(f"dual_annealing: {ml_value.x}, {ml_value.fun}")
y_F, y_M, y = get_optimized_y(ml_value, x)
visualize(x=x, y=[y_F, y_M, y], label=["Female", "Male", "Mixed"], method_name="dual_annealing")