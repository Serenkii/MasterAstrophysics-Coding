
import numpy as np

np.set_printoptions(precision=2)

top = np.array([
    15.6, 14.8, 14.9, 15.4,
    15.1, 14.8, 14.6, 14.4,
    15.2, 15.6, 14.4, 15.0,
    14.5, 14.3, 14.5, 15.3,
    14.6, 15.4, 15.4, 15.4,
    14.3, 15.5, 14.5, 14.8,
    14.5, 15.8, 15.3, 15.5,
])

bottom = np.array([
    16.7, 16.0, 16.2, 16.6,
    16.3, 16.0, 15.8, 15.7,
    16.2, 16.7, 15.7, 16.3,
    15.5, 15.6, 15.8, 16.4,
    15.8, 16.4, 16.5, 16.4,
    15.6, 16.6, 15.7, 16.1,
    15.9, 16.9, 16.4, 16.5,
])

p = np.array([
    1.72829, 3.39729, 3.09592, 2.11207,
    2.73145, 3.28489, 4.01588, 4.65494,
    2.69976, 1.83677, 4.80080, 2.73127,
    4.60602, 4.99589, 4.29163, 2.36133,
    4.15474, 2.28500, 2.16193, 2.20349,
    5.26198, 1.88935, 4.23637, 3.31084,
    3.94111, 1.47709, 2.31922, 1.98650,
])

app_magn = np.mean(np.vstack((top, bottom)), axis=0)

abs_magn = -2.7 * np.log10(p) - 1.6

mu = app_magn - abs_magn
d_L = 10 * 10 ** (mu / 5)

print(f"Distance in parsec for every lightcurve:\n{d_L.reshape((7,4))}")
print()


mean_d_L = np.mean(d_L)
sigma_of_values_dL = np.std(d_L, ddof=1)
sigma_of_mean_dL = sigma_of_values_dL / np.sqrt(p.shape[0])



print(f"Average distance of the lightcurve {mean_d_L} pc with uncertainty of {sigma_of_mean_dL} pc.")
print()


avg_mu = 5 * np.log10(mean_d_L / 10)
avg_mu_unc = 5 * np.log10(np.e) / mean_d_L * sigma_of_mean_dL

print(f"Distance modulus µ = m - M taken based on average distance: {avg_mu} with uncertainty of {avg_mu_unc}.")
print()

print(f"We are probably observing the Large Magellanic Cloud, as they are approx. 50 kpc away. "
      f"https://en.wikipedia.org/wiki/Large_Magellanic_Cloud\n"
      f"The results seem to be in line with: https://arxiv.org/html/1112.3171v1")

