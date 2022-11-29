from pytube import YouTube


def main():
    link = input("Enter the link: ")  # User Input
    yt = YouTube(link)

    stream = yt.streams.get_by_itag(22)
    stream.download()
    # .streams.filter(progressive=True), file_extension='mp4').order_by('resolution').desc().first().download()

    # Title of Video
    print("Title: ", yt.title)

    # Num of Views of video
    print("Number of views: ", yt.views)

    # Length of vid
    print("Length of video: ", yt.length, "seconds")

    # Descr of vid
    print("Description: ", yt.description)

    # Rating
    print("Ratings: ", yt.rating)

    '''
    
    # For Audio
    # yt.streams.filter(only_audio=True)
    [<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">,
    <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">,
    <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">,
    <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]
    
    '''


'''
    YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
    yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
    yt.streams
        .filter(progressive=True), file_extension='mp4')
        .order_by('resolution')
        .desc()
        .first()
        .download()
'''

main()
