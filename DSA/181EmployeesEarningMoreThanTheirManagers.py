'''
Initial thoughts
    For each employee, check their salary against their maangers. Has to return the result table

    use the filter funciton?

    for emp in employee:
        if emp.salary > emp.manager_id.id:
            include in results table

Incomplete
'''

import pandas as pd

df = pd.DataFrame({"A":[1,2,3], "B": [4,5,6]})
def find_employees(employee : pd.DataFrame) -> pd.DataFrame:
    print(employee.query('A>1'))
    # employee.filter()

find_employees(df)