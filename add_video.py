from objc_util import *
import threading


def add_video(path):
    PHPhotoLibrary = ObjCClass('PHPhotoLibrary')
    PHAssetChangeRequest = ObjCClass('PHAssetChangeRequest')
    lib = PHPhotoLibrary.sharedPhotoLibrary()
    url = nsurl(path)
    # path to local video file

    def change_block():
        req = PHAssetChangeRequest.creationRequestForAssetFromVideoAtFileURL_(url)

    def perform_changes():
        lib.performChangesAndWait_error_(change_block, None)

    t = threading.Thread(target=perform_changes)
    t.start()
    t.join()

if __name__ == '__main__':
    add_video() 
