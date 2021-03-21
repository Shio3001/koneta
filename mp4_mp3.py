import os

path_list = list(os.listdir())

for i in path_list:

    if i[-3:] != "mp4":
        continue

    j = i[:-4]

    print(j)

    test = "ffmpeg -i {0}.mp4 {0}.mp3".format(j)

    print(test)

    os.system(test)
