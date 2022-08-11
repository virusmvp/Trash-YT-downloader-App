# importing the module
from pytube import YouTube
import PySimpleGUI as sg
import urllib.request

yt = 'nothing'


def downloadVideo():
    link = (values['-IN-'])
    print(link)

    try:
        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(link)
    except:
        print("Connection Error")  # to handle exception

    print("Downloading the video...")

    wantedRes = 22

    filteredRes = yt.streams.get_by_itag(wantedRes)

    filteredRes.download()
    print("Succesfully downloaded: " + yt.title + " ✅")
    exit()


def displayImage():
    # link of the video to be downloaded
    link = (values['-IN-'])
    print(link)
    try:
        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(link)
    except:
        print("Connection Error")  # to handle exception

    # Get title
    print(yt.title)
    # Get thumbnail
    print("Thumbnail: " + yt.thumbnail_url)
    url = yt.thumbnail_url

    urllib.request.urlretrieve(url, yt.title + "-thumbnail.jpg")
    print("Downloaded Thumbnail ✅")


sg.theme('BluePurple')

layout = [[sg.Text('Enter the link to download below:'),
           sg.Text(size=(15, 1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Download Video'), sg.Button('Download Thumbnail')]]

window = sg.Window("Viraj's crappy YT Video downloader", layout)

while True:
    event, values = window.read()
    print(event, values)

    if event == 'Download Thumbnail':
        displayImage()

    if event == 'Download Video':
        downloadVideo()
        break
    

window.close()