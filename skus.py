import pandas as pd

def drop_digits(df_skus):
    df_skus['UPC'] = df_skus['UPC'].astype(str)
    df_skus['UPC'] = df_skus['UPC'].str[4:]