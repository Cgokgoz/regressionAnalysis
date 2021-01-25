from pyexpat import model

from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


def build_data(path):
    dependent_y = []
    independent_x = []

    with open(path) as f:
        next(f)
        for line in f.read().splitlines():
            price, lot_area, living_area, num_floors, num_bedrooms, num_bathrooms, waterfront, \
            year_built, year_renovated = line.split(',')

            dependent_y.append(int(price))
            independent_x.append(
                [int(lot_area), int(living_area), float(num_floors), int(num_bedrooms), float(num_bathrooms),
                 int(waterfront),
                 int(year_built), int(year_renovated)])
    calculation(dependent_y, independent_x)


def calculation(dependent_y, independent_x):
    x_train, x_test, y_train, y_test = train_test_split(independent_x, dependent_y, test_size=0.20, random_state=42)
    reg = linear_model.LinearRegression()
    reg.fit(x_train, y_train)
    y_predict = reg.predict(x_test)
    # for each in y_predict:
    #   print("prediction our test data " + str(each))
    # for each in y_test:
    #   print("actual prices on test data " + str(each))
    print("root mean squared error : ")
    print(mean_squared_error(y_test, y_predict, squared=False))
    test_accuracy = reg.score(x_test, y_test)
    print("test accuracy : ")
    print(test_accuracy)


if __name__ == '__main__':
    build_data("data/prices.csv")
