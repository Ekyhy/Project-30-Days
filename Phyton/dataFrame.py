import pandas as pd
import numpy as nw
import matplotlib.pyplot as plot

# Create DataFrame
df = pd.DataFrame({ 'x' : [0,1,3,5,8],
                    'y' : [2,4,6,5,9]})
print(df)
print(df.sum())

# Basic Scatter Plot using numpy and matplotlib.pyplot
x = nw.array([2,3,3,3,4,4,5,5,5,6])
y = nw.array([28.7,24.8,26.0,30.5,23.8,24.6,23.8,20.4,21.6,22.1])


plot.scatter(x,y)
plot.title("Basic Scatter Plot")
plot.xlabel("X Values")
plot.ylabel("Y Values")
plot.show()

