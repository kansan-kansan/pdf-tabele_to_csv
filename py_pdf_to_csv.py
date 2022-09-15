import pandas as pd
import tabula


# lattice=Trueでテーブルの軸線でセルを判定
dfs = []
for i in range(1,4):
    dfs = tabula.read_pdf("./薬学部.pdf", lattice=True,pages=i)
    for df in dfs:
        print(df)
        df.to_csv(f"./ファイル/薬学部{i}.csv", index=None,encoding='utf-8_sig')
print(type(df))