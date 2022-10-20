import pandas as pd
import sankey as sk


def min_val(df, val, **kwargs):
    '''
    :param df: original dataframe that contains selected data
    :param col: the targets and sources of the sankey diagram
    :param val: the name of grouped count column
    :param kwargs: any other possible factor, eg. minimal count as a filter
    :return: a new dataframe that contain selected factors and their grouped counts
    '''

    df.sort_values(val, ascending=False, inplace=True)
    # set a minimal value as a filter so the graph is clearer
    min_val = kwargs.get('min_val', 7)
    groups = df[df[val] >= min_val]
    return groups
def execute_sankey(df, col, val):
    '''
    :param df: original dataframe that contains selected data
    :param col: the targets and sources of the sankey diagram
    :param val: the name of grouped count column
    :return: a sankey diagram showing the connections
    '''
    # render the dataset to selected group dataframe
    groups = min_val(df, val)

    # if multi-factors(n > 2), refer directly to the renamed source and target
    if len(col) > 2:
        sk.show_sankey(groups, 'Source', 'Target', vals=val)
    # if two factors, refer to the column names
    else:
        sk.show_sankey(groups, col[0], col[1], vals=val)