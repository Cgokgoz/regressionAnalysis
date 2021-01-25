# regressionAnalysis
Regression analysis is one of the most important fields in statistics and machine learning.
Regression searches for relationships among variables.[1] We can observe several house of some
city and try to understand how their priceses depend on the features, such as lot area, living area,
number of floors, number of bedrooms, number of bathrooms, and so on.
This is a regression problem where data related to each house represent one observation. The
presumption is that the lot area, living area, number of floors, number of bedrooms, number of
bathrooms, waterfront, year the house and year the house was renovated are the independent
features, while the priceses depends on them.

In this project, data were prepared first. Two arrays of dependent y, independent x were created and
x(inputs) and y(output) values were determined. 80% of the dataset used as the training data. The
next step is to create a linear regression model and fit it using the existing data. With .fit(), we
calculate the optimal values of the weights b0 and b1 , using the existing input and output ( x and y)
as the arguments.

Root-mean-square error (RMSE) is a frequently used measure of the differences between values
(sample or population values) predicted by a model or an estimator and the values observed. The
RMSD represents the square root of the second sample moment of the differences between
predicted values and observed values or the quadratic mean of these differences.[2]

References:
[1]: https://realpython.com/linear-regression-in-python/
[2]: https://en.wikipedia.org/wiki/Root-mean-square_deviation
