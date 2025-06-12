number=[2,5,6,9,85,22,46,90,81,55]
n=("数字を入力してください。('q'で終了)")
while True:
    i=input(n)
    try:
        if i=="q":
            break
        else:
            i=int(i)
    except ValueError:
        print("数字か'q'を入力してください")
        continue
    if i in number:
        print("正解")
    else:
        print("不正解")

    


