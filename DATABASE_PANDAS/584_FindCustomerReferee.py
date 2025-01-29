import pandas as pd
import numpy as np

customer = pd.DataFrame({'id':[i for i in range(1,7)], 'name':[chr(name) for name in range(65, 71)],'referee_id':[np.NaN, np.NaN, 2, np.NaN, 1,2]})
#Given a data frame, return a dataframe with the filter aplied

# print(customer)
def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:

    # Can Query the dataframe like a dataabse
    # For some reason this works when run locally on python 3.10 but not on leetcode
    # It does not count the null values on leetcode but does here
    # query_db = customer.query("referee_id != 2 or referee_id == None")

    #This works though. 
    query_db = customer.query("referee_id != 2 or referee_id.isnull()")
    print (query_db['name'])

find_customer_referee(customer=customer)