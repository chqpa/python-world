#make_file.py
#구구단을 파일로 출력하기

def gugudan(a):
    f = open("C:/Users/PARK/PycharmProjects/study/gugudan.txt", 'w')
    show = print("OK 내가 구구단 {0}단 출력해줄께!! \n".format(int(a)))
    for b in range(1,10):
        result = int(a) * b
        print("{0}*{1}={2}\n".format(a,b,result))
        f.write("{0}*{1}={2}\n".format(a,b,result))
        b = b + 1
    f.close()
#print("몇단 출력하셈?")

gugudan(input("몇 단 출력하셈?"))

#오대단한데?
#a뭐지?


