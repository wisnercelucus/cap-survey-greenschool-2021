import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

def rename_col_values(df, col_name, values):
    """
    This method accepts a DataFrame, 
    a column name from which we will rename the values 
    (the column should be among the DataFrame column), and a dictionary of K, V pairs 
    where K represents the keys, so that value tio be renamed and v are the new names.
    Ex: df, col_name= "name", values = {'Pop':'Pope',
                                        'Ro':'Roma',
                                        }
    rename_value(df, 'name', values)
    It will return a list of the new values that we can use to replace the correct column in the DataFrame
    """
    col = df[col_name]
    col_renamed = []

    for v in col:
        col_renamed.append(values.get(v))
    return col_renamed


def rename_col_with_multiple_values(df, col_name, values):
    """
    This method accepts a DataFrame, 
    a column name from which we will rename the values 
    (the column should be among the DataFrame column), and a dictionary of K, V pairs 
    where K represents the keys, so that value tio be renamed and v are the new names.
    Ex: df, col_name= "name", values = {'Pop':'Pope',
                                        'Ro':'Roma',
                                        }
    rename_value(df, 'name', values)
    It will return a list of the new values that we can use to replace the correct column in the DataFrame
    """
    col = df[col_name]
    col_renamed = []
    

    for v in col:
        if type(v) != str:
            col_renamed.append(v)
            continue
        for k in values.keys():
            if not k in v:
                continue
            v = v.replace(k, values[k])
        col_renamed.append(v)
    return col_renamed


def count_freq_simple_answer(dframe, col_name):
    response_frequencies = {}
    col = dframe[col_name]
    for entry in col:
        if entry in response_frequencies.keys():
            response_frequencies[entry] = response_frequencies[entry] + 1
        else:
            response_frequencies[entry] = 1
    col_name_df = pd.DataFrame(list(response_frequencies.items()), columns =['response', 'frequency'])
    return col_name_df


def count_freq_multiple_answer(dframe, col_name, patterns):
    response_frequencies = {}
    col = dframe[col_name]
    for entry in col:
        for pattern in patterns:
            if pattern in str(entry):
                if pattern in response_frequencies.keys():
                    response_frequencies[pattern] = response_frequencies[pattern] + 1
                else:
                    response_frequencies[pattern] = 1       
    col_name_df = pd.DataFrame(list(response_frequencies.items()), columns =['response', 'frequency'])
    return col_name_df


def merge_match_size(df_1, df_2, key):
    if df_1.shape[0] > df_2.shape[0]:
        return df_1.merge(df_2, how='left', on=key).fillna(0)
    elif df_1.shape[0] < df_2.shape[0]:
        return df_2.merge(df_1, how='left', on=key).fillna(0)
    else:
        return df_1.merge(df_2, how='left', on=key)

def get_percent(n, d):
    return (n/d) * 100

def plot_g(sub):
    x = list(sub['response'])
    y = list(sub['frequency'])
    ind = np.arange(len(y))
    plt.bar(ind, y)
    plt.xticks(ind, x, rotation=60)
    plt.show()