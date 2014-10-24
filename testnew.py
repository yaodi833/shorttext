from sklearn import datasets
import numpy
import scipy
iris = datasets.load_iris()
di = datasets.load_digits()
print di.data
print di.target
print di.images[0]