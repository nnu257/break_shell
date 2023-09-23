# 機能
- 本プログラムは，ファイル構造を平坦化します．なお，平坦化の深度は1のみです．

# 使い方
- move.pyのparent_directory_nameに作業フォルダを入れて実行してください．
- 空フォルダは削除されます．
- フォルダ内のファイル名は，フォルダ名_ファイル名に変更されます．

# 使用例
平坦化前：  
hoge  
|-fuga1(空フォルダ)  
|-fuga2  
&emsp;|- piyo1  
&emsp;|- piyo2  

parent_directory_name = hogeとし，平坦化後：  
hoge  
|-fuga2_piyo1  
|-fuga2_piyo1  
