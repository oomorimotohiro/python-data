## pandasの使い方

import pandas as pd

dfs = []
# 最初のファイルを読み込んでDataFrameに格納
df1 = pd.read_csv('./use-pandas/input/file1.csv')

# 別のファイルを読み込んでDataFrameに格納
df2 = pd.read_csv('./use-pandas/input/file2.csv')

# 列を結合
merge_data = df1.join(df2, lsuffix="Item1")

merge_data.to_csv('./use-pandas/output/output3.csv', index=False)
