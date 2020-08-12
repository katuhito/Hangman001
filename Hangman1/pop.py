pop = []   #洋楽ポップソングを保存するリスト
jpop = []    #Jpopソングを保存するリスト

def collect_songs():
    song = "曲名を入力してください:"
    ask = "pかjのどちらかを入力してください。qで終わります:"

    while True:
        genre = input(ask)
        if genre == 'q':
            break

        if genre == 'p':
            q = input(song)
            pop.append(p)

        elif genre == 'j':
            j = input(song)
            jpop.apennd(j)

        else:
            print("不正な値です。")

    print("pop songs: ", pop)
    print("jpop songs: ", jpop)

collect_songs()
