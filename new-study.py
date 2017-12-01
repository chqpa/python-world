def noinput():
    print("HI")

noinput()


def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

def say_mtself(name: object, old: object, man: object = True) -> object:
    print("나의 이름은 %s 입니다." % name)
    print("나의 나이는 %d 입니다." % old)
    if man:
        print("남자입니다.\n")
    else:
        print("여자입니다\n")
    return

print(sum_many(10,11,12),"\n")

print('\n', say_mtself("김민후", 35, 0))