# login.py
# 로그인 여부 확인

# 입력값
id_pw = ['rabbit04', '98761']

db = [['jaja11', '98761'], ['krong0313', '29440'], ['rabbit00', '111333']]

# 로그인 결과 함수 정의
def login_result(id_pw, db):
    login_yn = 0

    if id_pw in db:
        login_yn = 1
    else:
        if id_pw[0] in [x[0] for x in db]:
            login_yn = 2
        else:
            login_yn = 3

    if login_yn == 1:
        print("login")
    elif login_yn == 2:
        print("wrong_pw")
    else:
        print("fail")


login_result(id_pw, db)
    
