import pandas as pd

def read_file(spreadsheet, head):
    return pd.read_excel(spreadsheet, header=head)

def write_sheets(df, file_name):
    df.to_excel(file_name, index = False)
    return