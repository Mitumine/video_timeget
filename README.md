# 使用方法
- `main.py`と同じディレクトリに`work_fold`を新規ディレクトリとして作成する。
- `work_fold`内に動画ファイルを内包したディレクトリを配置する。
- `main.py`を実行すると動画の合計時間が出力される。


# 注意
- `hachoir`ディレクトリについて、こちらは今回の要件を満たすためのライブラリとなっていますので、削除・移動しないようお願い致します。
- 今回暫定的に`work_fold`と致しましたが、`main.py`10行目あたりにある以下の部分を書き換えることによって任意のフォルダ名に変更することができます。

```py

# 作業フォルダ名の名前
WORK_FOLD_PATH = 'work_fold'

```


# 参考

- [vstinner/hachoir: Hachoir is a Python library to view and edit a binary stream field by field](https://github.com/vstinner/hachoir)
- [メモ帳 / Pythonで動画情報を取得する](https://blog.sky-net.pw/article/26)
- [Python datetime 日付の計算、文字列変換をする方法 strftime, strptime【決定版】 \- Qiita](https://qiita.com/7110/items/4ece0ce9be0ce910ee90)


