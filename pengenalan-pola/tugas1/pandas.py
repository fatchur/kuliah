import pandas as pd 

MAIN_PATH = "assets/"
df = pd.read_csv(MAIN_PATH + "web_traffict.tsv", sep='\t')
#remove null / NAN value 
df = df.dropna()

#give name for unnamed column
df.columns = ["col_1", "col_2"]

#rename column
df.rename( columns={'col_1':'input'}, inplace=True )
df.rename( columns={'col_2':'output'}, inplace=True )

# save result 
filepath = MAIN_PATH + "result.csv"
df.to_csv(filepath)
