import numpy as np


def squared_euclidean_distance(p, q):
    """
    Compute the squared Euclidean distance between two points p and q.
    
    Parameters:
    p: First point.
    q: Second point.
    
    Returns:
    The squared Euclidean distance between p and q.
    """

    return np.sum((np.array(p) - np.array(q)) ** 2)


def sym(X):
    """
    Form the similarity matrix A from the given data points using the Gaussian kernel.
    
    Parameters:
    X: Array of data points where each row represents a point.
    
    Returns:
    The similarity matrix A (n x n), where n is the number of data points.
    """

    n = X.shape[0]
    
    # Initialize similarity matrix A with zeros
    A = np.zeros((n, n))
    
    # Fill the similarity matrix A
    for i in range(n):
        for j in range(i + 1, n):
            A[i, j] = np.exp(-squared_euclidean_distance(X[i], X[j]) / 2)
            A[j, i] = A[i, j]
    return A


def ddg(X):
    """
    Form the diagonal degree matrix D from the similarity matrix A.
    
    Parameters:
    X: Array of data points where each row represents a point.
    
    Returns:
    The diagonal degree matrix D (n x n), where D[i, i] is the sum of row i in A.
    """
    
    # Compute the similarity matrix A
    A = sym(X)

    # Compute the diagonal elements as the sum of rows of A
    degrees = np.sum(A, axis=1)
    
    # Create a diagonal matrix from the degrees
    D = np.diag(degrees)
    
    return D


def norm(X):
    """
    Compute the normalized similarity matrix W from the similarity matrix A and the diagonal degree matrix D.

    Parameters:
    A : The similarity matrix of size (n x n), where n is the number of data points.
    D : The diagonal degree matrix (n x n) containing the degrees (sum of rows of A) along the diagonal.
    
    Returns:
    The normalized similarity matrix of size (n x n).
    """
    
    # Compute the similarity matrix A
    A = sym(X)

    # Compute the similarity matrix A
    D = ddg(X)

    # Compute D^(-1/2) as 1 / sqrt(D)
    D_inv_sqrt = np.power(D, -0.5)

    # Compute the normalized similarity matrix W
    W = A * D_inv_sqrt[:, np.newaxis] * D_inv_sqrt[np.newaxis, :]

    return W


def initialize_H(W, k):
    """
    Initialize the matrix H for SymNMF.

    Parameters:
    W: The normalized similarity matrix (n x n), where n is the number of data points.
    k: The number of clusters.
    
    Returns:
    The initialized matrix H of size (n x k), where n is the number of data points.
    """
    # Set the random seed
    np.random.seed(1234)
    
    # Calculate the average of all entries of W
    m = np.mean(W)
    
    # Initialize H with random values
    n = W.shape[0]
    H = np.random.uniform(0, 2 * np.sqrt(m / k), (n, k))
    
    return H

