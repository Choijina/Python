#20200569 최진아 프로젝트


#숫자 야구
import random


a = random.randint(1, 9)

b = random.randint(1, 9)

c = random.randint(1, 9)

cnt=0

print("숫자 야구 게임에 오신 것을 환영합니다!\n※총 3자리의 숫자를 맞히셔야 하며, 숫자의 범위는 1~9 입니다. \nBall은 틀린 개수, Strike는 맞힌 개수를 나타냅니다.※\n")

while True:

    ball = 0

    strike = 0

    n1 = int(input("첫번째 숫자를 입력하세요: ")) #q

    n2 = int(input("두번째 숫자를 입력하세요: ")) #w

    n3 = int(input("세번째 숫자를 입력하세요: ")) #e
    
    cnt+=1
    
    if a == n1 and b == n2 and c == n3:
        print(cnt, "번 만에 숫자를 맞히셨습니다. 정답은", a,b,c,"였습니다. \n")
        break
    
    if a != n1:
        ball += 1

    if b != n2:
        ball += 1

    if c != n3:
        ball += 1

    if a == n1 :
        strike += 1

    if b == n2:
        strike += 1

    if c == n3:
        strike += 1

    print("Ball:", ball, "Strike:", strike, "\n") 





#사각형 테두리 색 선택
import turtle as t
s=t.Screen()
t.setup(800,800)
t.colormode(255)

while True:
    colore=int(input("원하시는 사각형 테두리 색의 번호를 입력하세요.\n1번:검정색, 2번:빨강색, 3번:초록색, 4번:파랑색\n"))
    
    if colore==1:
        t.color(0,0,0)
        print("선택하신 색상은 검정색입니다.\n")
        break

    elif colore==2:
        t.color(255,0,0)
        print("선택하신 색상은 빨강색입니다.\n")
        break

    elif colore==3:
        t.color(29,219,22)
        print("선택하신 색상은 초록색입니다.\n")
        break
    
    elif colore==4:
        t.color(0,0,255)
        print("선택하신 색상은 파랑색입니다.\n")
        break

    else:
        print("번호를 잘못 입력하셨습니다.\n")






#사각형 채우기 색 선택
while True:
    colorf=int(input("원하시는 사각형 채우기 색의 번호를 입력하세요.\n1번:회색, 2번:분홍색, 3번:연두색, 4번:하늘색\n"))
    
    if colorf==1:
        t.fillcolor(189,189,189)
        break

    elif colorf==2:
        t.fillcolor(255,178,217)
        print("선택하신 색상은 분홍색입니다.\n")
        break

    elif colorf==3:
        t.fillcolor(206,251,201)
        print("선택하신 색상은 연두색입니다.\n")
        break
    
    elif colorf==4:
        t.fillcolor(178,235,255)
        print("선택하신 색상은 하늘색입니다.\n")
        break

    else:
        print("번호를 잘못 입력하셨습니다.\n")

print("사각형", cnt,"개를 랜덤으로 그리기 시작합니다.")






#사각형 그리기
j=1

for i in range(cnt):
    x=random.randint(-350,350)
    y=random.randint(-350,350)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()
    t.write(j)
    j+=1


