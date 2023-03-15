# v5 -> 화면에 선택해서 작업하는 메뉴화면 작성, 파일 IO도 추가
#       1) 메뉴추가  2) 메뉴확인  3) 메뉴선택  4) 메뉴삭제  0) 종료 ==> 1
# 요구사항
# - 동일한 메뉴는 추가되지 않도록 한다.
# - 정렬해서 확인
# - 선택 : 추가된 메뉴가 하나도 없을 때에는 선택하지 못하도록
# - 삭제 : 삭제할 메뉴를 입력받는다. 있으면 삭제, 없으면 없다라는 메시지 출력
# - 종료 : 현재까지 입력된 모든 메뉴를 파일(lunch.txt.)로 저장 후 종료
#        : 프로그램이 구동 되자마자 바로 파일을 읽어서 처리
import random

# 파일로부터 데이터를 읽음
def read_file() :
    lunch = []
    try :
        with open('./lunch.txt', 'rt', encoding="UTF-8") as f:
            while True :
                mymenu = f.readline()
                if mymenu == None or len(mymenu) == 0: break
                lunch.append(mymenu[:-1])
            return lunch
    except FileNotFoundError :
        lunch = []
        return lunch

# 메뉴 입력 (메인에서 1번이 선택되었을 때)    
def input_lunch(lunch) :
    while True:
        try :
            mymenu = input('> 점심메뉴를 입력:')
            if mymenu == '#' : 
                return lunch
            if mymenu.isnumeric() : raise ValueError
            if mymenu not in lunch :
                lunch.append(mymenu)
        except :
            print(" ** 메뉴를 다시 입력해 주세요")

#2) 메뉴확인
def output_lunch(lunch) : 
    if lunch == None or len(lunch) == 0 :
        print("** 저장된 메뉴가 없습니다.")
        return
    print("** 현재 점심 메뉴 : ", end="")
    for item in lunch :
        print(item, sep=", ", end=" ")
    print()
    
# 3) 메뉴 선택
def choice_lunch(lunch) :
    if lunch == None or len(lunch) == 0 :
        print("** 저장된 메뉴가 없습니다.")
        return        
    mychoice = random.choice(lunch)        
    return mychoice

# 4)
def delete_lunch(lunch) :
    if lunch == None or len(lunch) == 0 :
        print("** 저장된 메뉴가 없습니다.")
        return          
    try :
        print("** 메뉴목록 : ", end="")
        for item in lunch :
            print(item, sep=", ", end=" ")
        print()
        mymenu = input('> 삭제시킬 메뉴를 입력:')
        if mymenu == '#' : 
            return lunch
        if mymenu in lunch :
            lunch.remove(mymenu)
            return lunch
    except :
        pass
    
#5) 메뉴 0 선택시 ==> 파일에 저장 
def write_lunch(lunch) :
    if lunch == None or len(lunch) == 0 :
        return    

    with open('./lunch.txt', 'wt', encoding="UTF-8") as f:
        for item in lunch :
            f.write(item + "\n")
        print("** 파일 저장완료!")

# main부분
lunch = read_file()
while True :
    try : 
        select = input("1) 메뉴추가  2) 메뉴확인  3) 메뉴선택  4) 메뉴삭제  0) 종료 =>")
        if(select < '0' or select > '4'): raise ValueError
        if select == '1' :
            input_lunch(lunch)
        elif select == '2' :
            output_lunch(lunch)
        elif select == '3' :
            mymenu = choice_lunch(lunch)
            if mymenu != None : print("** 오늘 점심메뉴는: ", mymenu)
        elif select == '4' :
            lunch = delete_lunch(lunch)
        elif select == '0' :
            write_lunch(lunch)
            print('** 프로그램을 종료합니다.')
            break
            
    except ValueError :
        print("> 메뉴를 다시 선택해 주세요")