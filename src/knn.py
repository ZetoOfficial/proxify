import random

import numpy as np
import pandas as pd


class KNN:
    data: pd.DataFrame

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def predict(self, array_predict: [], weight=None, k=5, stand=False, poll=False):
        if weight is None:
            weight = [1, 1, 1, 1]

        nearest_neighbors = []

        if stand and k > 1:
            self.data['Sepal.L'] = (self.data['Sepal.L'] - self.data['Sepal.L'].mean()) / self.data['Sepal.L'].std()
            self.data['Sepal.W'] = (self.data['Sepal.W'] - self.data['Sepal.W'].mean()) / self.data['Sepal.W'].std()
            self.data['Petal.L'] = (self.data['Petal.L'] - self.data['Petal.L'].mean()) / self.data['Petal.L'].std()
            self.data['Petal.W'] = (self.data['Petal.W'] - self.data['Petal.W'].mean()) / self.data['Petal.W'].std()

            array_predict[0] = (array_predict[0] - self.data['Sepal.L'].mean()) / self.data['Sepal.L'].std()
            array_predict[1] = (array_predict[1] - self.data['Sepal.W'].mean()) / self.data['Sepal.W'].std()
            array_predict[2] = (array_predict[2] - self.data['Petal.L'].mean()) / self.data['Petal.L'].std()
            array_predict[3] = (array_predict[3] - self.data['Petal.W'].mean()) / self.data['Petal.W'].std()

        self.data['Sepal.L'] = self.data['Sepal.L'] * weight[0]
        self.data['Sepal.W'] = self.data['Sepal.W'] * weight[1]
        self.data['Petal.L'] = self.data['Petal.L'] * weight[2]
        self.data['Petal.W'] = self.data['Petal.W'] * weight[3]

        values = self.data.values.tolist()
        random.shuffle(values)
        for j in values:
            dist = np.sqrt(
                (array_predict[0] - j[0]) ** 2 + (array_predict[1] - j[1]) ** 2 + (array_predict[2] - j[2]) ** 2 + (
                            array_predict[3] - j[3]) ** 2)

            if len(nearest_neighbors) < k:
                nearest_neighbors.append([dist, j[4]])
            else:
                for ne in range(len(nearest_neighbors)):
                    if nearest_neighbors[ne][0] > dist:
                        nearest_neighbors[ne] = [dist, j[4]]
                        break
            sorted(nearest_neighbors, key=lambda x: x[1])

        k_setosa = 0
        k_versicolor = 0
        k_virginica = 0

        if not poll:
            for i in nearest_neighbors:
                if i[1] == 'Iris-setosa':
                    k_setosa += 1
                if i[1] == 'Iris-versicolor':
                    k_versicolor += 1
                if i[1] == 'Iris-virginica':
                    k_virginica += 1
        else:
            for i in nearest_neighbors:
                if i[1] == 'Iris-setosa':
                    k_setosa += 1 / (0.5 + i[0] ** 2)
                if i[1] == 'Iris-versicolor':
                    k_versicolor += 1 / (0.5 + i[0] ** 2)
                if i[1] == 'Iris-virginica':
                    k_virginica += 1 / (0.5 + i[0] ** 2)
        num = max(k_setosa, k_versicolor, k_virginica)

        if num == k_versicolor:
            return 'Iris-versicolor'
        if num == k_virginica:
            return 'Iris-virginica'
        if num == k_setosa:
            return 'Iris-setosa'
