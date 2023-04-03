import pandas as pd

def separate_items(df_shopventory, split_location):

    df_items_without_variants = df_shopventory.iloc[:split_location]
    df_items_with_variants = df_shopventory.iloc[split_location:]

    return df_items_with_variants, df_items_without_variants

def combine_product_names(df_shopventory):
    # combine product name and variant name, if present
    df_shopventory['Combined Name'] = df_shopventory['Product Name'] + " - " + df_shopventory['Variant Name']
    return df_shopventory

def join_dfs(df_shopventory, df_lightspeed, variants=False):
    # joing dataframes on df_shopventory, preserving the item order
    print("Lightspeed columns:")
    print(df_lightspeed)
    df_lightspeed = df_lightspeed.rename(columns={'Item': 'Product Name'})
    if variants is False:
        # df_shopventory.join(df_lightspeed, how='inner', left_on='Product Name', right_on='Item')
        df_shopventory_combined = df_shopventory.join(df_lightspeed.set_index('Product Name'), on='Product Name')
    else:
        # df_shopventory.join(df_lightspeed, how='inner', left_on='Combined Name', right_on='Item')
        df_shopventory_combined = df_shopventory.join(df_lightspeed.set_index('Product Name'), on='Combined Name')
    return df_shopventory_combined

# def find_stragglers(df_shopventory_without_variants, df_shopventory_with_variants, df_lightspeed):
#     df_stragglers_no_variant = df_shopventory_without_variants.join(df_lightspeed.set_index('Product Name'), on='Product Name', how='cross')
#     df_stragglers_variant = df_shopventory_with_variants.join(df_lightspeed.set_index('Product Name'), on='Combined Name', how='cross')
#     df_stragglers = df_stragglers_no_variant.join(df_stragglers_variant.set_index('Combined Name'), on='Product Name', how='inner')
#     print(df_stragglers)

def drop_columns(df, column_list):
    df.drop(column_list, axis=1, inplace=True)
    return df