## pandasの使い方

import pandas as pd

# 最初のファイルを読み込んでDataFrameに格納
df1 = pd.read_csv('./use-pandas/input/file1.csv')

# 別のファイルを読み込んでDataFrameに格納
df2 = pd.read_csv('./use-pandas/input/file2.csv')

# 列を結合
merged_df = pd.concat([df1, df2], axis=1)

# 結合されたデータをCSVファイルとして出力
merged_df.to_csv('./use-pandas/output/output.csv', index=False)

# カラムを追加
columns = ["Item1","Item2","Item3","Item4","Item5","Item6","Item7","Item8","Item9","Item10"]

df = merged_df.reindex(columns=columns)


df.to_csv('./use-pandas/output/output2.csv', index=False)

