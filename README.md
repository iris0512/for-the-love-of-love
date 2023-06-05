# for-the-love-of-love
a project to analyze the data related to romantic movies using Python and Tableau. Entry for IronViz2022

### Building dataset
The first step includes extracting the movie dataset from [IMdB](https://datasets.imdbws.com/). We are using the following datasets to build our initial list of movies:
1. title.akas.tsv.gz
2. title.basics.tsv.gz
3. title.ratings.tsv.gz

We then join it with the 2 datasets available in the input folder to build the dataset that will finally be used in the Tableau dashboard. 

The next step includes extracting the movie scripts and processing it using the nltk package to build a word cloud.

### Tableau Dashboard
https://public.tableau.com/app/profile/siri.mrudula/viz/FortheLoveofLove/FortheLoveofLove


