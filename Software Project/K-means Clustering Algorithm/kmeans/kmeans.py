import sys
import math

#helping functions
def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip(): 
                data.append(list(map(float, line.strip().split(','))))
    return data

def euclidean_distance(p, q):
    return math.sqrt(sum((pi - qi) ** 2 for pi, qi in zip(p, q)))

def checkIfValid(num):
    try:
        num = float(num)
        intNum = int(num)
        return intNum == num 
    except ValueError:
        return False

def kmeansAlgorithm(k, iter, data):
    epsilon = 0.001
    iteration_number = 0
    k = int(float(k))
    iter = int(float(iter))
    centroids = data[:k]

    while(iteration_number < iter):
        clusters = [[] for i in range(k)]
        for victor in data:
            distances = [euclidean_distance(victor, centroid) for centroid in centroids]
            index = distances.index(min(distances))
            clusters[index].append(victor)

        new_centroids = []

        # update the centroids
        for cluster in clusters:
            new_centroids.append([sum(xi) / len(cluster) for xi in zip(*cluster)])
        if(all(euclidean_distance(c1, c2) < epsilon for c1, c2 in zip(centroids, new_centroids))):
            break
        centroids = new_centroids
        iteration_number += 1

    for centroid in centroids:
        print(','.join('{:.4f}'.format(coord) for coord in centroid))


if len(sys.argv) < 3:
    print("An Error Has Occurred.")
    exit(1)

# kmeans algorithm
k = sys.argv[1]
iter = 200 if len(sys.argv) < 4 else sys.argv[2] 
input_data = sys.argv[2] if len(sys.argv) < 4 else sys.argv[3]
data = read_data(input_data)

# checking validity of k
if not checkIfValid(k) or int(float(k)) <= 1 or int(float(k)) >= len(data):
    print("Invalid number of clusters!")
    exit(1)

# checking validity of iter
if not checkIfValid(iter) or int(float(iter)) <= 1 or int(float(iter)) >= 1000:
    print("Invalid maximum iteration!")
    exit(1)

# starting the kmeans algorithm
kmeansAlgorithm(k, iter, data)
