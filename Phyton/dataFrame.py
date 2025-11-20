import pandas as pd

# Create DataFrame
df = pd.DataFrame({ 'x' : [0,1,3,5,8],
                    'y' : [2,4,6,5,9]})
print(df)

print(df.sum())