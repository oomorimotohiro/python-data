## pandasの使い方

import pandas as pd

dfs = []
# 最初のファイルを読み込んでDataFrameに格納
df1 = pd.read_csv('./use-pandas/input/file1.csv')

df1 = df1.set_index(['Item1','Item2'])
dfs.append(df1)

# 別のファイルを読み込んでDataFrameに格納
df2 = pd.read_csv('./use-pandas/input/file2.csv')
df2 = df2.set_index(['Item1','Item2'])
dfs.append(df2)

# 列を結合
merged_df = pd.concat(dfs, axis=1, join='inner').reset_index()

# 結合されたデータをCSVファイルとして出力
merged_df.to_csv('./use-pandas/output/output.csv', index=False)
