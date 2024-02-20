""" Yamato File Move Manager
これはファイル整理ソフトです。
app.pyと同じ場所にある
「YYYYMM_●●」というファイルを整理します。
「YYYYMM」というフォルダを作成し、
それぞれのファイルをそこに移動します。
※ YYYYMMは年月

Example:
    $ python app.py
"""
import os
import re
import shutil

def main():
    """ Main関数
    移動するファイルの一覧を取得し、
    フォルダを作成し、移動する関数
    """
    # 移動するファイルの一覧を取得する
    all_files = os.listdir("./")
    # 取得したファイル一覧をそれぞれ、以下繰り返す
    for i in all_files:
        # そのファイルが、最初の6文字が数字だったとき、かつファイル移動する
        if re.match(r"\d{6}", i) and os.path.isfile(i):
            # 移動するとき、年月フォルダがあれば移動するし、なければフォルダを作成して移動
            target_date = i[0:6]
            if os.path.isdir(target_date):
                # 移動だけ
                shutil.move(i, target_date)
            else:
                # フォルダ作成して移動
                os.mkdir(target_date)
                shutil.move(i, target_date)

if __name__ == "__main__":
    main()