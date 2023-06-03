import pandas as pd
import numpy as np

path = 'YOUR PATH HERE'

#reading all the tables
titles_akas = pd.read_table(path+'title.akas.tsv\\data.tsv')
titles_basic = pd.read_table(path+'title.basics.tsv\\data.tsv')
titles_rating = pd.read_table(path+'title.ratings.tsv\\data.tsv')


#viewing the data
titles_akas.head()
titles_basic.head()
titles_rating.head()

#titles_akas cleaning
titles_akas.tail()
titles_akas_1 = titles_akas[titles_akas['isOriginalTitle']==1]
titles_akas_1.head()
titles_akas_2 = titles_akas_1[['titleId','title']]

titles_basic.head()
titles_basic.tconst.nunique(), titles_basic.tconst.count()
titles_basic['movie_flag'] = np.where(((titles_basic['titleType'] =='movie') | (titles_basic['titleType'] =='tvMovie')) ,1,0)
titles_basic_1 = titles_basic[titles_basic['movie_flag']==1]
titles_basic_1['isRomance'] = np.where(titles_basic_1['genres'].str.contains('Romance'),1,0)
titles_basic_2 = titles_basic_1[titles_basic_1['isRomance']==1]
titles_basic_3 = titles_basic_2[['tconst','primaryTitle','originalTitle','startYear','genres']]

titles_df = titles_akas_2.merge(titles_basic_3,left_on='titleId',right_on='tconst',how='right')
titles_df = titles_df.merge(titles_rating,left_on='tconst',right_on='tconst',how='left')

more_info = pd.read_csv(path+'IMDb movies.csv')
rating_bd = pd.read_csv(path+'IMDb ratings.csv')

more_data = more_info.merge(rating_bd,how='left',on='imdb_title_id')
more_data['isRomance'] = np.where(more_data['genre'].str.contains('Romance'),1,0)
more_data = more_data[more_data['isRomance']==1]

more_data.columns
titles_df = titles_df[['titleId', 'title', 'primaryTitle', 'originalTitle',
       'startYear', 'genres', 'averageRating', 'numVotes']]

final_df = titles_df.merge(more_data,how='left',left_on='titleId',right_on='imdb_title_id')
final_df.shape
final_df.head()
final_df.to_csv(path+'rom_coms.csv',index=False)