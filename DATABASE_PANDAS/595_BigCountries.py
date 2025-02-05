import pandas as pd
World = pd.DataFrame({'name':['Afghanistan', 'Ethiopia', 'Jamaica'],'area':[120000, 120000000, 400000000],'population':[20000000, 120000000,300000]})
def BigCountries(World: pd.DataFrame, **kwargs )->pd.DataFrame:
    print(kwargs)
    print (pd.DataFrame(World.query("area >= @kwargs['min_area'] or population >= @kwargs['min_pop']")[['name','population']]))

BigCountries(World=World, min_area=3000000, min_pop = 25000000)