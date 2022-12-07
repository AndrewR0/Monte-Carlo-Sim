import numpy as np

S0 = 10
K = 10
r = 0.02
sigma = 0.25
T = 0.25
delta_t = 0.025

M = T / delta_t # M = 10

def monte(S0, K, r, sigma, delta_t, n):
    discount_factor = np.exp(-r * T)

    CT_sum = 0
    
    for _ in range(n): # loop over n paths
        S = S0
        for _ in range(int(M)): # loop over time steps  
            delta_S = r*S*delta_t + sigma*S*np.sqrt(delta_t)*np.random.normal()
            S += delta_S
        CT_sum += max(S - K, 0)

    return discount_factor*CT_sum/n

if __name__ == "__main__":
    N = [10,100,1000,10000]

    for j in range(10):
        for i in N:
            m = monte(S0, K, r, sigma, delta_t, i)
            print(m)
            print("Abs_E", abs(0.5224453276436325 - m))
        print("\n")