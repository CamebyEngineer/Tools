import pandas as pd
import numpy as np

df = pd.read_csv('Raw.csv')


import seaborn as sns


# exp = df[0:10][:1000]
# sns.pairplot(exp)
g = sns.pairplot(df, hue="Seam Group", 
                    vars = ["DEPTH_FROM" 
                            ,"DEPTH_TO"
                            ,"THICK" 
                            ,"RAW_RD"
                            ,"MOISTURE"
                            ,"ASH"
                            ,"HGI"] )
                            # ,"TOTAL_SULPHUR"] )
                            # 
                            # ,"TOTAL_SULPHUR" 
                            #,"PHOSPHORUS"
                            # ,	"CSN"
                            # ,	"HGI"
                            # ,	"MHC"] 
                            # issues 
                            # ,"ARD","VOLATILES","FIXED_CARBON","SPECIFIC_ENERGY" ]

g.savefig('test.png')