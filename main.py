import pandas as pd
import files, items

def main():

    df_lightspeed = files.read_file("lightspeed_export.xlsx", 0)
    df_shopventory = files.read_file("shopventory_import.xlsx", 1)

    shopventory_columns_del = ['ID', 'Product Categories',
       'New Variant Name', 'SKU', 'New SKU', 'Barcode', 'New Barcode', 'Price',
       'New Price', 'Default Cost', 'New Default Cost', 'PAR Level',
       'New PAR Level', 'Reorder Qty', 'New Reorder Qty', 'Vendor 1',
       'New Vendor 1', 'Vendor 1 ID', 'New Vendor 1 ID', 'Vendor 2',
       'New Vendor 2', 'Vendor 2 ID', 'New Vendor 2 ID', 'Vendor 3',
       'New Vendor 3', 'Vendor 3 ID', 'New Vendor 3 ID',
       'alberta Use Defaults', 'New alberta Use Defaults', 'alberta Price',
       'New alberta Price', 'alberta Default Cost', 'New alberta Default Cost',
       'alberta PAR Level', 'New alberta PAR Level', 'alberta Reorder Qty',
       'New alberta Reorder Qty', 'alberta Quantity In Stock',
       'New alberta Quantity In Stock', 'Bybee Use Defaults',
       'New Bybee Use Defaults', 'Bybee Price', 'New Bybee Price',
       'Bybee Default Cost', 'New Bybee Default Cost', 'Bybee PAR Level',
       'New Bybee PAR Level', 'Bybee Reorder Qty', 'New Bybee Reorder Qty',
       'Bybee Quantity In Stock', 'New Bybee Quantity In Stock',
       'center of the collage creative universe Use Defaults',
       'New center of the collage creative universe Use Defaults',
       'center of the collage creative universe Price',
       'New center of the collage creative universe Price',
       'center of the collage creative universe Default Cost',
       'New center of the collage creative universe Default Cost',
       'center of the collage creative universe PAR Level',
       'New center of the collage creative universe PAR Level',
       'center of the collage creative universe Reorder Qty',
       'New center of the collage creative universe Reorder Qty',
       'center of the collage creative universe Quantity In Stock',
       'New center of the collage creative universe Quantity In Stock',
       'Division St Use Defaults', 'New Division St Use Defaults',
       'Division St Price', 'New Division St Price',
       'Division St Default Cost', 'New Division St Default Cost',
       'Division St PAR Level', 'New Division St PAR Level',
       'Division St Reorder Qty', 'New Division St Reorder Qty',
       'Division St Quantity In Stock', 'New Division St Quantity In Stock']
    
    lightspeed_columns_del = ['System ID', 'UPC', 'EAN', 'Custom SKU', 'Manufact. SKU',
       'Qty.', ' Collage - Annex ', ' Collage Outlet ', 'Price', 'Tax', 'Brand',
       'Publish to eCom', 'Season', 'Department', 'MSRP', 'Tax Class',
       'Default Cost', 'Vendor', 'Category', 'Subcategory 1', 'Subcategory 2',
       'Subcategory 3', 'Subcategory 4', 'Subcategory 5', 'Subcategory 6',
       'Subcategory 7', 'Subcategory 8', 'Subcategory 9']

    items.drop_columns(df_shopventory, shopventory_columns_del)
    items.drop_columns(df_lightspeed, lightspeed_columns_del)

    print("Lightspeed columns:")
    print(df_lightspeed.columns)
    print("Shopventory columns")
    print(df_shopventory.columns)

    # update this number with location of split
    split_location = 6471

    df_shopventory_with_variants, df_shopventory_without_variants = items.separate_items(df_shopventory, split_location)

    df_shopventory_with_variants_renamed = items.combine_product_names(df_shopventory_with_variants)

    df_combined_with_variants = items.join_dfs(df_shopventory_with_variants_renamed, df_lightspeed, True)
    df_combined_without_variants = items.join_dfs(df_shopventory_without_variants, df_lightspeed, False)

    print("with variants head")
    print(df_combined_with_variants.head)
    print("without variants tail")
    print(df_combined_without_variants.tail)

    # df_stragglers = items.find_stragglers(df_shopventory_without_variants, df_shopventory_with_variants, df_lightspeed)

    files.write_sheets(df_combined_with_variants, "items_with_variants_inv.xlsx")
    files.write_sheets(df_combined_without_variants, "items_without_variants_inv.xlsx")
    # files.write_sheets(df_stragglers, 'straggers.xlsx')

if __name__ == "__main__":
    main()
