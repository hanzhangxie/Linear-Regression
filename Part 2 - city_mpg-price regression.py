import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# split the dataset into training/testing sets
x = np.array([31, 19, 24, 24, 27, 23, 37, 23, 31, 25, 31, 23, 18, 49, 28, 19, 31, 37, 31, 31, 30, 19, 26, 23, 21, 26, 24, 23, 20, 16, 31, 31, 27, 31, 24, 19, 19, 27, 25, 37, 38, 26, 27, 22, 21, 27, 19, 26, 31, 25, 28, 26, 19, 29, 34, 24, 29, 31, 22, 28, 31, 17, 31, 37, 31, 24, 17, 26, 21, 17, 38, 21, 27, 19, 27, 24, 37, 21, 28, 24, 24, 19, 31, 25, 30, 31, 38, 22, 31, 19, 21, 17, 27, 31, 27, 20, 24, 38, 31, 15, 26, 26, 18, 23, 31, 27, 32, 26, 30, 24, 38, 30, 24, 27, 31, 30, 31, 31, 26, 19, 35, 28, 24, 27, 19, 19, 30, 17, 23, 37, 23, 24, 17, 24, 28, 30, 27, 47, 45])
y = np.array([0.6669, 1.862, 1.1549, 1.5985, 1.0295, 0.9959, 0.5572, 1.1694, 0.6189, 0.8189000000000001, 0.6229, 0.8013, 2.1485000000000003, 0.6479, 1.32, 2.2018, 0.6918000000000001, 0.5572, 0.5499, 0.7349, 0.5195000000000001, 1.8150000000000002, 0.9298000000000001, 0.9279000000000001, 1.5510000000000002, 1.1245, 0.8921, 1.6925000000000001, 1.5690000000000002, 3.5056000000000003, 0.6649, 0.6229, 1.1248, 0.5118, 1.6515000000000002, 1.2964, 1.5998, 0.8949, 0.8499, 0.7775000000000001, 0.7788, 0.8495, 0.8845000000000001, 2.5552, 1.504, 0.8778, 2.2625, 0.996, 0.6377, 1.0198, 1.7950000000000002, 0.9995, 1.558, 0.8948, 0.7898000000000001, 0.7957000000000001, 0.8238000000000001, 0.8249000000000001, 2.8248, 0.7463000000000001, 0.6695, 1.895, 0.6855, 0.9495, 0.6338, 0.8921, 1.4399000000000002, 0.7053, 2.1105, 1.9699, 0.5399, 1.185, 0.8495, 1.7710000000000001, 0.9549000000000001, 0.7957000000000001, 0.7995, 2.097, 0.7775000000000001, 1.395, 0.998, 1.19, 0.7799, 0.6989000000000001, 0.7198, 0.7609, 0.7738, 2.8176, 0.6849000000000001, 1.7199, 1.217, 1.842, 1.0898, 0.6692, 0.9988, 1.6558000000000002, 0.9989, 0.6575000000000001, 0.6095, 3.225, 2.247, 0.8845000000000001, 1.8150000000000002, 1.294, 0.7395, 0.9095000000000001, 0.7126, 0.9538000000000001, 0.7129000000000001, 0.8449000000000001, 0.6295000000000001, 0.6529, 1.1259000000000001, 0.8195, 0.6488, 0.7295, 0.7299, 0.6692, 1.0245, 1.9045, 0.5348, 1.6900000000000002, 0.7689, 0.7895000000000001, 1.8399, 1.828, 0.7295, 2.3875, 0.9279000000000001, 0.5389, 1.3415000000000001, 1.7669000000000001, 1.3499, 1.2945, 0.9258000000000001, 0.6938000000000001, 0.7975, 0.5151, 0.7099000000000001])

x_test=np.array([25, 31, 27, 23, 19, 29, 31, 24, 24, 26, 24, 31, 19, 18, 30, 31, 28, 26, 23, 22])
y_test=np.array([1.0345, 0.7499, 0.7898000000000001, 1.6845, 1.663, 0.8058000000000001, 0.6795, 0.9233, 1.1199000000000001, 0.7603000000000001, 0.9639000000000001, 0.7609, 1.3499, 1.745, 1.0698, 0.7999, 0.8358, 1.0595, 1.643, 3.16])

n = len(x)

# fit LinearRegression models
lr = LinearRegression()
# train the model using the training set
lr.fit(x[:, np.newaxis], y)  
# make predictions using the testing set
y1 = lr.predict(x_test[:, np.newaxis])

# the coefficients
print('Coefficients: \n', lr.coef_)
# the mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, y1))
# explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, y1))

# plot outputs
segments = [[[i, y[i]]] for i in range(n)]
lc = LineCollection(segments, zorder=0)
lc.set_array(np.ones(len(y)))
lc.set_linewidths(np.full(n, 0.5))
fig = plt.figure()
plt.plot(x_test, y_test, 'r.', markersize=12)
plt.plot(x_test, y1, 'b-')
plt.gca().add_collection(lc)
plt.legend(('Data','Linear Fit'), loc='lower right')
plt.title('city_mpg-price regression')
plt.xlabel('city_mpg')
plt.ylabel('price')
plt.show()