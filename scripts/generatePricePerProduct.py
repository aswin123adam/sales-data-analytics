import pandas as pd

def generatePrice(SalesData):
      df_SalesData = pd.DataFrame(SalesData)
      df_nan_removed = df_SalesData[(df_SalesData['Quantity'] * 10) % 10 == 0]
      df_nansale_removed = df_nan_removed[(df_nan_removed['Sales'] >=0 )]
      df_price_per_product_code = df_nansale_removed.drop_duplicates(subset=['Product ID'],keep='first')
      df_price_per_product_code['Price Per Product'] = ((df_price_per_product_code['Sales'] / df_price_per_product_code['Quantity']) * 100) / (100 - (df_price_per_product_code['Discount'] * 100))





      df_price_per_product_code.drop(['Row ID','Order ID','Order Date',
                      'Ship Date','Ship Mode','Customer ID','Segment','Region',
                      'Category','Sub-Category','Product Name','Sales','Quantity',
                      'Discount','Profit','Country'],axis=1,inplace=True)
      return(df_price_per_product_code)

    #   df_price_per_product_code.drop(['Row ID','Order ID','Order Date',
    #                   'Ship Date','Ship Mode','Customer ID','Segment','Region',
    #                   'Category','Sub-Category','Product Name','Profit','Country'],axis=1,inplace=True)
    #   return(df_price_per_product_code)


def get_output_schema():
 	return pd.DataFrame({
            'Product ID' : prep_string(),
            'Price Per Product' : prep_decimal()
 		});