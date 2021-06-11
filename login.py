id1 = "toto"
pwd = "1234"

for i in range(1,6):
    yid = input("아이디 입력 : ")
    ypwd = input("비밀번호 입력 : ")

    if id1 == yid:
        if pwd == ypwd:
            print(":: 로그인 성공 ::")
        else:
            print(":: 비밀번호 틀렸습니다. ::")
    else:
        print(":: 아이디가 틀렸습니다 ::")


