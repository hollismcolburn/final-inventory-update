Sort Lightspeed inventory export to match Shopventory inventory import
To be used 4/2 to do final inventory update before switch to Square/Shopventory

Steps to use:
1. Download Shopventory Google Sheet to "Edit Variants" as .xlsx
2. Rename as "shopventory_import.xlsx" and move to main folder
3. Export all inventory items from Lightspeed, showing all locations
4. Save as "lightspeed_export.xlsx" and move to main folder
5. In "shopventory_import.xlsx", find dividing index between items with and without variants
6. Update "split_location" variable with dividing index (main.py, line 10)
7. run main.py