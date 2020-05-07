from pytube import YouTube
import add_video
import byte2si
import url_get
import os
import glob
import time


def absfpath(path):
    # ”Download”ディレクトリ下のファイルを取得する
    flist = glob.glob(path + '/*')
    if flist:
        # “Download”ディレクトリ下の1つしかない動画ファイルを取得する
        fpath = os.path.abspath(flist[0])
         # “Download”ディレクトリ下にある動画ファイルの絶対パスを返す
        return fpath
    else:
        raise OSError('The file does not exist.')


def main():
    #プログレスバー
    print('Now executing...')

    # YouTubeアプリからurlを取得
    url = url_get.yturl()
    if not url:
        raise ('Not YouTube')

    # pytube.YouTubeを使い、urlから動画リストを取得し、そのリストの最初の動画をダウンロードする
    yt = YouTube(url)
    stream = yt.streams.first()
    # main.pyと同一ディレクトリ下にある"Download"のパスを取得
    drpath = os.getcwd() + 'Download'
    # ダウンロードする
    stream.download(drpath)
    # その動画の絶対パスを取得
    abspath = absfpath(drpath)
    # その動画のサイズを取得
    size = os.path.getsize(abspath)
    sibyte = byte2si.byte2si(size)
    #ファイルサイズを表示
    print('Size:', sibyte)

    # 動画のパスを渡し、フォトライブラリーに追加する
    add_video.add_video(abspath)
    # “Download”ディレクトリにはファイルを残さない、残すと”absfpath()”でバグる
    os.remove(abspath)


if __name__ == '__main__':
    # 開始時間を取得
    start = time.time()
    main()
    #終了時間を少数第3位まで取得
    finish = round(time.time() - start, 3)
    #実行所要時間を表示
    print('Execute Time:', finish)
    #終了
    print('Done')
