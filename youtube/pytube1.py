from pytube import YouTube
#stream.download('https://www.youtube.com/watch?v=rrGuDH1S4zM')
y=YouTube('https://www.youtube.com/watch?v=rrGuDH1S4zM')
print(y.get_lowest_resolution())