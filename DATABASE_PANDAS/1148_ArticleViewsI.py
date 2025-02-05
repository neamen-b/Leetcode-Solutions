import pandas as pd

views = pd.DataFrame(columns=['article_id','author_id','viewer_id','view_date'],
                     data={'article_id':[1,1,2,2,4,3,3],'author_id':[3,3,7,7,7,4,4],'viewer_id':[5,6,7,6,1,4,4]})
print(views)
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    query_db = views.query("author_id == viewer_id").drop_duplicates(subset=['author_id','viewer_id']).rename(columns={'author_id':'id'}).drop(columns=['article_id','viewer_id','view_date']).sort_values(by='id')
    print(query_db)

article_views(views=views)