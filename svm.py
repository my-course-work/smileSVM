from cvxopt import solvers, matrix
import numpy as np
import sklearn.svm

class SVM ():
    def __init__ (self):
        pass

    # Expects each *row* to be an m-dimensional row vector. X should
    # contain n rows, where n is the number of examples.
    # y should correspondingly be an n-vector of labels (-1 or +1).
    def fit (self, X, y):
        # TODO change these -- they should be matrices or vectors
        n = X.shape[0]
        G = make_G(X, y)
        P = [
            [1.0, 0.0],
            [0.0, 0.0]
        ]

        q = 0
        h = -1 * np.ones((n,))

        # print(G.shape)
        # print(P.shape)
        # print(h.shape)

        # Solve -- if the variables above are defined correctly, you can call this as-is:
        sol = solvers.qp(matrix(P, tc='d'), matrix(q, tc='d'), matrix(G, tc='d'), matrix(h, tc='d'))

        # Fetch the learned hyperplane and bias parameters out of sol['x']
        self.w = 0  # TODO change this
        self.b = 0  # TODO change this

    # Given a 2-D matrix of examples X, output a vector of predicted class labels
    def predict (self, x):
        return 0  # TODO fix

def make_row(h, size):
    return 

def make_G(X, y):
    Y = np.array([y, y]).T
    return np.hstack((-Y * X, np.reshape(-y, (y.shape[0], 1))))

def test1 ():
    # Set up toy problem
    X = np.array([ [1,1], [2,1], [1,2], [2,3], [1,4], [2,4] ])
    y = np.array([-1,-1,-1,1,1,1])

    # Train your model
    svm = SVM()
    svm.fit(X, y)
    print(svm.w, svm.b)

    # Compare with sklearn
    svm = sklearn.svm.SVC(kernel='linear', C=1e15)  # 1e15 -- approximate hard-margin
    svm.fit(X, y)
    print(svm.coef_, svm.intercept_)

    acc = np.mean(svm.predict(X) == svm.predict(X))
    print("Acc={}".format(acc))

def test2 ():
    # Generate random data
    X = np.random.rand(20,3)
    # Generate random labels based on a random "ground-truth" hyperplane
    while True:
        w = np.random.rand(3)
        y = 2*(X.dot(w) > 0.5) - 1
        # Keep generating ground-truth hyperplanes until we find one
        # that results in 2 classes
        if len(np.unique(y)) > 1:
            break

    svm = SVM()
    svm.fit(X, y)

    # Compare with sklearn
    svm = sklearn.svm.SVC(kernel='linear', C=1e15)  # 1e15 -- approximate hard margin
    svm.fit(X, y)
    diff = np.linalg.norm(svm.coef_ - svm.w) + np.abs(svm.intercept_ - svm.b)
    print(diff)

    acc = np.mean(svm.predict(X) == svm.predict(X))
    print("Acc={}".format(acc))

    if acc == 1 and diff < 1e-1:
        print("Passed")

if __name__ == "__main__": 
    test1()
    # test2()
