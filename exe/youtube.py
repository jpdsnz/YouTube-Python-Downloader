from pytube import YouTube


link = input("Enter the link: ")  # User Input
yt = YouTube(link)

stream = yt.streams.get_by_itag(22)
stream.download()

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


