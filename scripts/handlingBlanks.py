import pandas as pd

def handleBlanks(MergedSalesData):
	#Handling Blanks in Sales
	df_merged_salesData = pd.DataFrame(MergedSalesData)
	df_merged_salesData.loc[df_merged_salesData['Sales'].isna(),'Sales'] = ((df_merged_salesData['Price Per Product'] * df_merged_salesData['Quantity']) * (100 - (df_merged_salesData['Discount'] * 100))) / 100
	df_blankSales_handled = df_merged_salesData
	
    #Handling Decimal Values in Quantity
	df_blankSales_handled.loc[(df_blankSales_handled['Quantity'] * 10) % 10 != 0 , 'Quantity'] = 0
	
    #Handling Blanks and Decimal Values in Quantity
	df_blankSales_handled.loc[df_blankSales_handled['Quantity'].isna() | df_blankSales_handled['Quantity'] == 0 , 'Quantity'] = (df_blankSales_handled['Sales'] * 100) / (df_blankSales_handled['Price Per Product'] * (100 - (df_blankSales_handled['Discount'] * 100)))
	df_blank_sales_and_qty_handled = df_blankSales_handled
	
    #Eliminating Data with No Sales value and no reference value to calculate Price per product
	df_final = df_blank_sales_and_qty_handled.dropna(subset='Price Per Product')

	return(df_final)


def get_output_schema():
 	return pd.DataFrame({
            'Row ID' : prep_int(),
 			'Order ID' : prep_string(),
 			'Order Date' : prep_date(),
 			'Ship Date' : prep_date(),
 			'Ship Mode' : prep_string(),
 			'Customer ID' : prep_string(),
 			'Segment' : prep_string(),
 			'Region' : prep_string(),
            'Product ID' : prep_string(),
            'Category' : prep_string(),
            'Sub-Category' : prep_string(),
            'Product Name' : prep_string(),
            'Sales' : prep_decimal(),
            'Quantity' : prep_decimal(),
            'Discount' : prep_decimal(),
            'Profit' : prep_decimal(),
            'Price Per Product' : prep_decimal(),
			'Country' : prep_string()
 		});