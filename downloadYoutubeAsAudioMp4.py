from pytube import YouTube

#Asking for all the video links
# Examnple  python downloadYoutbut.py
# 100
# $song name 1
# $youtube url
# $song name 2
# $youtube url
# and so on, once done.. kill the function, will download song at home location

n = int(input("Enter the number of youtube videos to download:   "))
links=[]
print("\nEnter all the links one per line:")
link = input()
count = 0
for i in range(0, n):
    print(count)
    if link:
        if not count % 2:
            filename = link
        else:
            links.append(link)
            # 140 tag downloads mp4 audio @128bps
            download_tag = 140
            yt = YouTube(link)
            ys = yt.streams.get_by_itag(download_tag)
            ys.download(filename=filename+".mp4")
    else:
        break
    count += 1
    print('Enter new filename')
    link = input()
 
print(links)
#n = 1    
#links = ['https://youtu.be/70QpN7DvaK4'] 
##Showing all details for videos and downloading them one by one
#for i in range(0,n):
#    link = links[i]
#    yt = YouTube(link)
#    print("\nDetails for Video",i+1,"\n")
#    print("Title of video:   ",yt.title)
#    print("Number of views:  ",yt.views)
#    print("Length of video:  ",yt.length,"seconds")
#    #stream = str(yt.streams.filter(progressive=True))
#    stream = str(yt.streams.filter(only_audio=True))
#    stream = stream[1:]
#    stream = stream[:-1]
#    streamlist = stream.split(", ")
#    print("\nAll available options for downloads:\n")
#    for i in range(0,len(streamlist)):
#        st = streamlist[i].split(" ")
#        print(i+1,") ",st[1]," and ",st[3],sep='')
#    tag = int(input("\nEnter the itag of your preferred stream to download:   "))
#    ys = yt.streams.get_by_itag(tag)
#    print("\nDownloading...")
#    ys.download()
#    print("\nDownload completed!!")
#    print()
