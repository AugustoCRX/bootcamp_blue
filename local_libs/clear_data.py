import pandas as pd

def clear_data_train(df):
    # droping null categories names and brands names(around 3000 values)
    dropnull = df[df.category_name.isnull() & df.brand_name.isnull()].index
    df = df.drop(dropnull, axis=0).reset_index(drop=True)

    # replace null values to "Other" df['category_name'] = df['category_name'].fillna("Other")
    df['category_name'] = df['category_name'].fillna("Other")

    #have just 4 lines of null item description, i will remove them
    df = df.dropna(subset = ['item_description']).reset_index(drop=True)
    df = df.drop(columns = ['train_id'])

    #I will raplace all 629225 null values in "train['brand_name']" for other again, after we can looking again
    df['brand_name'] = df['brand_name'].fillna("Other")

    #replacing data 29-02-2018 for 28-02-2018
    df['date'] =  df['date'].replace('29-2-2018','28-2-2018')

    #Creating new dates columns
    df['date2'] = pd.to_datetime(df['date'], errors='coerce')    #corrige os erros com os valores das datas de nascimento, adequa para DateTime
    df['day'] = df['date2'].dt.day
    df['month'] = df['date2'].dt.month
    df['year'] = df['date2'].dt.year

    #It drops rows with 0 price.
    x = df.query(f"{'price'} == 0").index
    df.drop(x, inplace= True)

    return df

def clear_data_test(df):
    # droping null categories names and brands names(around 3000 values)
    dropnull = df[df.category_name.isnull() & df.brand_name.isnull()].index
    df = df.drop(dropnull, axis=0).reset_index(drop=True)

    # replace null values to "Other" df['category_name'] = df['category_name'].fillna("Other")
    df['category_name'] = df['category_name'].fillna("Other")

    #have just 4 lines of null item description, i will remove them
    df = df.dropna(subset = ['item_description']).reset_index(drop=True)
    df = df.drop(columns = ['test_id'])

    #I will raplace all 629225 null values in "train['brand_name']" for other again, after we can looking again
    df['brand_name'] = df['brand_name'].fillna("Other")

    #replacing data 29-02-2018 for 28-02-2018
    df['date'] =  df['date'].replace('29-2-2018','28-2-2018')

    #Creating new dates columns
    df['date2'] = pd.to_datetime(df['date'], errors='coerce')    #corrige os erros com os valores das datas de nascimento, adequa para DateTime
    df['day'] = df['date2'].dt.day
    df['month'] = df['date2'].dt.month
    df['year'] = df['date2'].dt.year

    return df
