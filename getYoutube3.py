#! python3
# coding:utf-8

import appex,os,clipboard
from objc_util import *
import threading
import youtube_dl
    
def add_video(path):
	PHPhotoLibrary = ObjCClass('PHPhotoLibrary')
	PHAssetChangeRequest = ObjCClass('PHAssetChangeRequest')
	lib = PHPhotoLibrary.sharedPhotoLibrary()
	url = nsurl(path)

	def change_block():
		req = PHAssetChangeRequest.creationRequestForAssetFromVideoAtFileURL_(url)

	def perform_changes():
		lib.performChangesAndWait_error_(change_block, None)

	t = threading.Thread(target=perform_changes)
	t.start()
	t.join()

def my_hook(d):
	if d['status'] == 'finished':
		print('\nダウンロードしました')
		global downloadCheck
		downloadCheck=True
		
if not appex.is_running_extension():
	url=clipboard.get()
else:
	url = appex.get_text()
if not url:
	url=clipboard.get()

folder=os.getcwd()

downloadCheck=False

ydl_opts = {
	'outtmpl': '%(title)s.%(ext)s',
    'format': 'best',
    'progress_hooks': [my_hook],
}
ydl=youtube_dl.YoutubeDL(ydl_opts)
with ydl:
	result=ydl.extract_info(url,download=True)

#print(result)

if downloadCheck==True:
	filename=result['title']+'.'+result['ext']
	#print('フォトライブラリに移動しますか？ y/n')
	#photoFlg=input()
	photoFlg='y'
	if photoFlg=='y':
		abspath = os.path.join(folder,filename)
		if os.path.isfile(abspath):
			os.remove(abspath)
		add_video(abspath)

print('終了')
