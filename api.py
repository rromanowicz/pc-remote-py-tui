from typing import Tuple
import requests


host = "192.168.0.150"
port = "8080"


endpoints = {
    'media': "/mediaKey?key={}",
    'volume': "/vol?key={}&val={}",
    'shutdown': "/shut?key={}&type={}&val={}"
}


mediaKeys = {
    "nextTrack": "",
    "prevTrack": "",
    "playPause": "",
    "keyEscape": "",
    "keySpacebar": "__",
    "keyReturn": "",
    "arrowUp": "",
    "arrowDown": "",
    "arrowLeft": "",
    "arrowRight": ""
}

volumeKeys = {
    "increase": "",
    "decrease": "",
    "set": "",
    "mute": ""
}

shutdownType = {
    "shut": "",
    "hibernate": "",
    "sleep": ""
}

shutdownKeys = {
    "confirm": "",
    "cancel": "",
    "check": ""
}


def getEndpoint(endpoint: str):
    return f'http://{host}:{port}{endpoints.get(endpoint)}'


def call_media(key: str) -> Tuple[int, str]:
    keyValue = list(mediaKeys.keys())[list(mediaKeys.values()).index(key)]
    url = getEndpoint('media').format(keyValue)
    return __make_get_request(url)


def call_volume(key: str, val: int) -> Tuple[int, str]:
    keyValue = list(volumeKeys.keys())[list(volumeKeys.values()).index(key)]
    url = getEndpoint('volume').format(keyValue, val)
    return __make_get_request(url)


def call_shutdown(key: str, type: str, val: int) -> Tuple[int, str]:
    keyValue = list(shutdownKeys.keys())[
        list(shutdownKeys.values()).index(key)]
    typeValue = list(shutdownType.keys())[
        list(shutdownType.values()).index(type)]
    url = getEndpoint('shutdown').format(keyValue, typeValue, val)
    return __make_get_request(url)


def __make_get_request(urlStr: str) -> Tuple[int, str]:
    print(urlStr)

    try:
        r = requests.get(urlStr)
        r.raise_for_status()
        return (r.status_code, r.content.decode("utf-8"))
    except requests.exceptions.ConnectionError:
        return (503, "Connection refused.")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


if __name__ == '__main__':
    print(call_media(""))
    print(call_volume("", 10))
    print(call_shutdown("", "", 90))
