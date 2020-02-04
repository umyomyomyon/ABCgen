# ABCgen
AtCoderの問題を解く際に、以下のような手順を踏んでいました　

1. コンテストページを開く
2. 入力例をテキストファイルに保存
3. コードを書いていくファイルに、テキストファイルを読み込むコードを記述

これを毎回繰り返すのは非常に面倒なので、以下の方法で自動化しました


1. 引数としてcontest_type, contest_num, taskを渡す

contest_type -> ABC(AtCoder Beginner Contest)

contest_num -> コンテストの開催回数

task -> 問題

ex.)AtCoder Beginner Contest 154のB問題の場合
```
    $ python3 ABCgen.py ABC 154 b
```

2. 渡された引数からコンテストの問題ページのURLを生成

3. 問題ページから入力例を取得

4. ディレクトリを生成
  ex.) ./ABC/154/B
  
5. 生成したディレクトリ内に解答用ファイル(.py)と入力例が記載されたテキストファイルを生成
