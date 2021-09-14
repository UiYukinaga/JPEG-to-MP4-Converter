#=====================================================================
# jpgファイルを繋ぎ合わせて動画(mp4)に変換する
#---------------------------------------------------------------------
# Arguments:
#   1 ディレクトリパス or 'help'コマンド
#   2 解像度の指定コマンド or ユーザー指定の幅
#   3 フレームレート[fps] or ユーザー指定の高さ
#   4 NONE or フレームレート[fps]
# Return: None
# Output: Converted MP4 file
#=====================================================================
import cv2
import glob
import os
import shutil
import time
import datetime
import sys
import pathlib

def is_int(dat):
    print(dat)
    try:
        int(dat)
        return True
    except ValueError:
        return False


def convert_to_mp4(images, w, h, fps, path):
    # 処理開始時間を取得する
    start = time.time()
    
    current_dt = datetime.datetime.now()
    dt_str = current_dt.strftime('%Y%m%d_%H%M%S')
    file_name = dt_str + '_movie.mp4'
    save_path = os.path.join(os.getcwd(), file_name)

    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    video = cv2.VideoWriter(save_path, fourcc, fps, (w, h))
    
    print(">> 動画形式に変換しているよ。ちょっと待ってね。")
    
    images.sort()
    
    count = 0
    n_images = len(images)
    progress = 0
    for i in range(len(images)):
        img = cv2.imread(images[i])
        img = cv2.resize(img,(w, h))
        video.write(img) 
        # 処理の進捗表示
        count += 1
        progress = 100 * count / n_images
        if progress == 100:
            print('\r>> 変換完了！')
        else:
            print('\r>> {0}%'.format(progress),end="")
    
    video.release()

    # 動画変換にかかった時間を計算する
    elapsed_time = time.time() - start
    # 経過時間を表示
#    print("\r\n")
    print(">> 変換にかかった時間: {0}[sec]".format(elapsed_time))
    print(">> 変換した動画の場所: " + save_path)
    print(">> 動画のサイズ: {0} x {1}".format(w, h))
    print(">> フレームレート: {0}fps".format(fps))
    
if __name__ == '__main__':
    
    args = sys.argv
    
    # 第1引数: ディレクトリパス or HELPコマンド判定
    arg_1 = str(args[1])
    dir_path = ""
    if arg_1.upper() == 'HELP':
        print('Argument 1st is Image Directory path')
        print('Argument 2nd is Select a Size of Frame')
        print('<COMMAND>')
        print('QVGA: 320 x 240')
        print('VGA: 640 x 480')
        print('WVGA: 800 x 480')
        print('SVGA: 800 x 600')
        print('XGA: 1,024, 768')
        print('WXGA or HD: 1,280 x 768')
        print('FULLHD: 1920 x 1080')
        sys.exit()
    else:
        dir_path = arg_1
        p = pathlib.Path(dir_path)
        p = p.resolve()
        dir_path = str(p)
        print(dir_path)
    
    # 第2引数: 解像度の指定コマンドの解析
    arg_2 = str(args[2])
    arg_3 = 0
    arg_4 = 0
    
    # 幅・高さマニュアル指定モードであるなら
    if is_int(arg_2):
        width = int(arg_2)
        arg_3 = int(args[3])
        height = arg_3
        arg_4 = int(args[4])
        frame_rate = arg_4
    
    else:    
        resolution = str(arg_2)
        if resolution.upper() == 'QVGA':
            width = 320
            height = 240
        elif resolution.upper() == 'VGA':
            width = 640
            height = 480
        elif resolution.upper() == 'WVGA':
            width = 800
            height = 480
        elif resolution.upper() == 'SVGA':
            width = 800
            height = 600
        elif resolution.upper() == 'XGA':
            width = 1024
            height = 768
        elif resolution.upper() == 'WXGA':
            width = 1280
            height = 768
        elif resolution.upper() == 'HD':
            width = 1280
            height = 768
        elif resolution.upper() == 'FULLHD':
            width = 1920
            height = 1080
        else:
            print('ERROR: "' + resolution.upper() + '" is the out of support.')
            sys.exit()
        # 第3引数: フレームレートの取得
        frame_rate = int(args[3])
        
    # 基になる静止画リストの取得
    images = sorted(glob.glob(os.path.join(dir_path, '*.jpg')))
    # 取得した静止画の数を表示
    print(">> 画像の総枚数: {0}".format(len(images)))
    # 動画変換実行
    convert_to_mp4(images, width, height, frame_rate, dir_path)
    
