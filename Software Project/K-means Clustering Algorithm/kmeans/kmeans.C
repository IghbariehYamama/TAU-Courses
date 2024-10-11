#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

double** read_data(int* num_points, int* dimension) {
    int dim;
    double* point;
    char line[1024];
    int capacity = 10;
    double** data = malloc(capacity * sizeof(double*));
    char* token;
    *num_points = 0;

    while (fgets(line, sizeof(line), stdin)) {
        if (line[0] == '\n') continue;

        dim = 0;
        point = malloc(10 * sizeof(double));

        token = strtok(line, ",");
        while (token) {
            point[dim++] = atof(token);
            token = strtok(NULL, ",");
        }

        if (*num_points == capacity) {
            capacity *= 2;
            data = realloc(data, capacity * sizeof(double*));
        }

        data[(*num_points)++] = point;
        *dimension = dim;
    }
    return data;
}

double euclidean_distance(double* p, double* q, int dimension) {
    int i;
    double sum = 0.0;
    for (i = 0; i < dimension; i++) {
        sum += pow(p[i] - q[i], 2);
    }
    return sqrt(sum);
}

int checkIfValid(const char* num_str) {
    char* end;
    double num = strtod(num_str, &end);
    if (*end != '\0') {
        return 0;
    }
    return floor(num) == num;
}

int main(int argc, char* argv[]) {
    char* k_str;
    char* iter_str;
    int k, iter;
    int num_points, dimension;
    double epsilon = 0.001;
    int iteration_number = 0;
    double** data;
    double** centroids;
    int i, j;

    if (argc < 2) {
        printf("An Error Has Occurred.");
        return 1;
    }

    k_str = argv[1];
    iter_str = (argc < 3) ? "200" : argv[2];

    if (!checkIfValid(k_str)) {
        printf("Invalid number of clusters!");
        return 1;
    }

    k = atoi(k_str);

    data = read_data(&num_points, &dimension);
    if (k <= 1 || k >= num_points) {
        for (i = 0; i < num_points; i++) {
            free(data[i]);
        }
        free(data);
        printf("Invalid number of clusters!");
        return 1;
    }

    if (!checkIfValid(iter_str) || atoi(iter_str) <= 1 || atoi(iter_str) >= 1000) {
        for (i = 0; i < num_points; i++) {
            free(data[i]);
        }
        free(data);
        printf("Invalid number of clusters!");
        printf("Invalid maximum iteration!");
        return 1;
    }

    iter = atoi(iter_str);

    centroids = malloc(k * sizeof(double*));
    for (i = 0; i < k; i++) {
        centroids[i] = malloc(dimension * sizeof(double));
        for (j = 0; j < dimension; j++) {
            centroids[i][j] = data[i][j];
        }
    }

    while (iteration_number < iter) {
        int* cluster_sizes = calloc(k, sizeof(int));
        double** new_centroids = malloc(k * sizeof(double*));
        int converged;
        int d;

        for (i = 0; i < k; i++) {
            new_centroids[i] = calloc(dimension, sizeof(double));
        }

        for (i = 0; i < num_points; i++) {
            double min_dist = euclidean_distance(data[i], centroids[0], dimension);
            int cluster_index = 0;
            for (j = 1; j < k; j++) {
                double dist = euclidean_distance(data[i], centroids[j], dimension);
                if (dist < min_dist) {
                    min_dist = dist;
                    cluster_index = j;
                }
            }
            cluster_sizes[cluster_index]++;
            for (d = 0; d < dimension; d++) {
                new_centroids[cluster_index][d] += data[i][d];
            }
        }

        for (i = 0; i < k; i++) {
            for (d = 0; d < dimension; d++) {
                new_centroids[i][d] /= cluster_sizes[i];
            }
        }

        converged = 1;
        for (i = 0; i < k; i++) {
            if (euclidean_distance(centroids[i], new_centroids[i], dimension) >= epsilon) {
                converged = 0;
                break;
            }
        }

        if (converged){
            for (i = 0; i < k; i++) {
                free(new_centroids[i]);
            }
            free(new_centroids);
            free(cluster_sizes);
            break;
        } 

        for (i = 0; i < k; i++) {
            for (d = 0; d < dimension; d++) {
                centroids[i][d] = new_centroids[i][d];
            }
            free(new_centroids[i]);
        }

        free(new_centroids);
        free(cluster_sizes);
        iteration_number++;
    }

    for (i = 0; i < k; i++) {
        for (j = 0; j < dimension; j++) {
            printf("%.4f", centroids[i][j]);
            if (j < dimension - 1) {
                printf(",");
            }
        }
        printf("\n");
    }

    for (i = 0; i < num_points; i++) {
        free(data[i]);
    }
    free(data);
    for (i = 0; i < k; i++) {
        free(centroids[i]);
    }
    free(centroids);

    return 0;
}
