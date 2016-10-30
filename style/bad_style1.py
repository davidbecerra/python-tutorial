def mse(self, x, y, standardize=True):
    if standardize:
        X = self.standardize(x)
    y_pred = self.predict(X)
    N = float(len(X))
    error = y - y_pred
    return np.dot(error, error) / N