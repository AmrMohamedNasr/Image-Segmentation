import math
import numpy as np
from sklearn.metrics.cluster import contingency_matrix
def print_measures(gt_img, kimg):
    f_measure = 0;
    cond_entropy = 0;
    for i in range(len(cont_mat[0])):
        n_i = np.sum(cont_mat[:,i]);
        n = len(gt_img);
        # f_measure_i
        temp_index = np.argmax(cont_mat[:,i]);
        prec = cont_mat[temp_index][i] / np.sum(cont_mat[:,i]);
        rec = cont_mat[temp_index][i] / np.sum(cont_mat[temp_index,:]);
        f_measure_i = (2 * prec * rec) / (prec + rec);
        f_measure += f_measure_i;
        # conditional entropy
        entropy = 0;
        for j in range(len(cont_mat)):
            percent_j = cont_mat[j][i] / np.sum(cont_mat[:,i]);
            entropy -= percent_j * math.log10(percent_j);
        entropy *= n_i / n;
        cond_entropy += entropy;
    f_measure /= len(cont_mat[0]);
    return f_measure, cond_entropy;