import pandas as pd 
from datetime import datetime
def count_month_yr(x):
    '''Count occurrences of month-yr in dataframe'''
    assert isinstance(x, pd.DataFrame)
    assert not x.empty
    assert not x['month-yr'].empty
    timestamp = x['month-yr']
    assert all([isinstance(s, str) for s in timestamp])
    df = pd.DataFrame(columns=['Timestamp'])
    for i in range(0, len(x)):
        t = timestamp[i]
        if (df.index == t).any():
            df.loc[t] += 1
        else:
            df.loc[t] = 1
    return df

def add_month_yr(x):
    '''Output new month-yr column from input survey dataframe'''
    assert isinstance(x, pd.DataFrame)
    assert not x.empty
    assert not x['Timestamp'].empty
    assert isinstance(x['Timestamp'], pd.Series)
    timestamp = x['Timestamp']
    assert all([isinstance(s, str) for s in timestamp])
    assert not x['ID'].empty
    assert isinstance(x['ID'], pd.Series)
    id_var = x['ID']
    assert all([isinstance(s, int) for s in id_var])
    df = x[['Timestamp', 'ID']]
    df_new = pd.DataFrame(columns=['month-yr'])
    for i in range(0, len(df)):
        time = datetime.strptime(df.loc[i]["Timestamp"], '%m/%d/%Y %H:%M')
        s1 = pd.DataFrame([datetime.strftime(time, '%b-%Y')], index=[df.loc[i]["ID"]], columns=['month-yr'])
        df_new = pd.concat([df_new, s1])
    df_new = df_new.reset_index()
    x = pd.concat([x, df_new], axis=1)
    return x