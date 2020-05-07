import appex
import re


def trns():
    if not appex.is_running_extension():
        raise RuntimeError(
            'This script is intended to be run from the sharing extension.')

    url = appex.get_text()
    if not url:
        raise ValueError('No input text found.')
    elif re.search(r'youtube', url):
        return url
    raise ValueError('Not YouTube')


def yturl():
    geturl = trns()
    # 取得したurlの余分なテキストを置換し、なくす
    url = geturl.replace('&feature=share', '')
    return url


if __name__ == '__main__':
    print(yturl())
