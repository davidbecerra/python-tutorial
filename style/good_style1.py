def mse(self, x, y, standardize=True):
    """
    Compute the Mean Squared Error (MSE) between the true target y and 
    the prediction f(x)

        MSE = 1/N * sum_1^N (y - f(x))^2
    
    param {numpy array N x D} Matrix of data. Rows are a data point. 
        Columns are features. N data points, D features
    param {numpy array N x 1} Target vector. 1 target value for 
        each of the N data points
    return {float} Mean squared error
    """
    if standardize:
        X = self.standardize(x)
    y_pred = self.predict(X)
    N = float(len(X))
    error = y - y_pred
    return np.dot(error, error) / N