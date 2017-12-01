#input.py
#bmi 지수를 구하는 프로그램


print("BMI 측정시스템")

def BMI_cal():
    f = open("C:/Users/PARK/PycharmProjects/study/새새파일.txt", 'w')
    name = input("당신의 이름을 입력하세요 : ")
    height = int(input("키를 입력해주세요 (CM) : "))   #키 입력

    meter_height = float(height/100) #소수점이 생기기 때문에 실수형 변수로 형변환

    weight = int(input("\n몸무게를 입력해주세요 (kg) :"))  #몸무게 입력
    print("\n")

    print("키는",height,",  몸무게는",weight)

    question = input("맞나요? [y,n]")

    if question == 'y':
        bmi_result = weight / (meter_height * meter_height)
        print(name+"의 BMI 지수는",round(bmi_result,2),"입니다")
        f.write(name+"의 BMI 지수는{0}입니다".format(str(round(bmi_result, 2))))
        f.close()
    else:
        print("틀렸습니다")
    return 0


BMI_cal()









