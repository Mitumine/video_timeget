from glob import glob
import datetime

# ローカルからimport
# https://github.com/vstinner/hachoir
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser


# 作業フォルダ名の名前
WORK_FOLD_PATH = 'work_fold'


def getduration(video_path: str):
    '''
    渡されたpathの再生時間を取得する。
    渡されるpathの形式はmp4でなければならない。
    '''

    parser = createParser(video_path)
    meta = extractMetadata(parser)
    duration = meta.get("duration")
    return duration


def main():
    # 作業用フォルダの中身を取得
    glob_path_1 = f'{WORK_FOLD_PATH}/*'
    for fold_name in glob(glob_path_1):
        # 時間計算用の零点
        total = datetime.timedelta()

        # フォルダ名をダイアログに出力
        print('-'*5)
        print(fold_name)

        # mp4ファイル検索
        glob_path_2 = f'{fold_name}/*.mp4'
        for video_path in glob(glob_path_2):
            duration = getduration(video_path)
            print('単品 =>', duration)
            total += duration

        # フォルダ内のmp4の合計時間を出力
        print('合計 =>', total)


if __name__ == '__main__':
    main()
