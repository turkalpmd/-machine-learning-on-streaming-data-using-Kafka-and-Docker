import pandas as pd
import numpy as np
import scipy.stats
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris['data'], columns = iris['feature_names'])
df['target'] = pd.Series(iris['target'], name = 'target_values')
df['target_name'] = df['target'].replace([0,1,2],
['iris-' + species for species in iris['target_names'].tolist()])



def my_distribution(min_val, max_val, mean, std):
    scale = max_val - min_val
    location = min_val
    # Mean and standard deviation of the unscaled beta distribution
    unscaled_mean = (mean - min_val) / scale
    unscaled_var = (std / scale) ** 2
    # Computation of alpha and beta can be derived from mean and variance formulas
    t = unscaled_mean / (1 - unscaled_mean)
    beta = ((t / unscaled_var) - (t * t) - (2 * t) - 1) / ((t * t * t) + (3 * t * t) + (3 * t) + 1)
    alpha = beta * t
    # Not all parameters may produce a valid distribution
    if alpha <= 0 or beta <= 0:
        raise ValueError('Cannot create distribution for the given parameters.')
    # Make scaled beta distribution with computed parameters
    return scipy.stats.beta(alpha, beta, scale=scale, loc=location)

np.random.seed(100)


def iris_data_creator(iteration=1):
    sl_list = []
    sw_list = []
    pl_list = []
    pw_list = []

    for i in range(iteration):  

        min_val_sl = df["sepal length (cm)"].min()
        max_val_sl = df["sepal length (cm)"].max()
        mean_sl = df["sepal length (cm)"].mean(skipna=True)
        std_sl = df["sepal length (cm)"].std(skipna=True)
        my_dist_sl = my_distribution(min_val_sl, max_val_sl, mean_sl, std_sl)
        sample_sl = my_dist_sl.rvs(size=1).round(1)[0]
        sl_list.append(sample_sl)
    
    for i in range(iteration): 

        min_val_sw = df['sepal width (cm)'].min()
        max_val_sw = df['sepal width (cm)'].max()
        mean_sw = df['sepal width (cm)'].mean(skipna=True)
        std_sw = df['sepal width (cm)'].std(skipna=True)
        my_dist_sw = my_distribution(min_val_sw, max_val_sw, mean_sw, std_sw)
        sample_sw = my_dist_sw.rvs(size=1).round(1)[0]
        sw_list.append(sample_sw)

    for i in range(iteration): 

        min_val_pl = df["petal length (cm)"].min()
        max_val_pl = df["petal length (cm)"].max()
        mean_pl = df["petal length (cm)"].mean(skipna=True)
        std_pl = df["petal length (cm)"].std(skipna=True)
        my_dist_pl = my_distribution(min_val_pl, max_val_pl, mean_pl, std_pl)
        sample_pl = my_dist_pl.rvs(size=1).round(1)[0]
        pl_list.append(sample_pl)

    for i in range(iteration): 

        min_val_pw = df["petal width (cm)"].min()
        max_val_pw = df["petal width (cm)"].max()
        mean_pw = df["petal width (cm)"].mean(skipna=True)
        std_pw = df["petal width (cm)"].std(skipna=True)
        my_dist_pw = my_distribution(min_val_pw, max_val_pw, mean_pw, std_pw)
        sample_pw = my_dist_pw.rvs(size=1).round(1)[0]
        pw_list.append(sample_pw)

    random_df = pd.DataFrame()
    random_df['sepal_length'] = sl_list
    random_df['sepal_width'] = sw_list
    random_df['petal_length'] = pl_list
    random_df['petal_width'] = pw_list
    
    
    return random_df.to_json()

# for i in range(1):
#     if __name__ == '__main__':
#          print(iris_data_creator(iteration=1))

