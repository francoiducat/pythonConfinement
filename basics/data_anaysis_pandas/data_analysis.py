#!/usr/bin/env python

import pandas


# Create pandas data structure
df1 = pandas.DataFrame([[1.0, 2.0], [3.0, 4.0]], columns=[
                       "col1", "col2"], index=["first", "second"])

print(df1)
print(type(df1))

print(df1.mean())
print(df1.col1.max())
print(type(df1.mean()))
