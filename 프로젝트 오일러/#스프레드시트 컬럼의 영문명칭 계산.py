#스프레드시트 컬럼의 영문명칭 계산 26진법
#영어는 순서대로 아스키코드 65번이 A chr(65)
#진법 바꾸는방법은 나누기계속해서 몫으로 역순
#역순 하는 방법은 A[::-1]

    
n = 10 ** 8
res = ""

while n > 0:
    res += str(chr(65 + n % 26 - 1))
    n //= 26

print(res[::-1])


# 모범답안...ㄷㄷ