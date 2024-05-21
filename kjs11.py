def validate_jumin_number(jumin):
    # 주민등록번호는 13자리여야 한다.
    if len(jumin) != 13 or not jumin.isdigit():
        return False

    # 각 자리에 곱할 가중치 배열
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    # 마지막 자리는 제외하고 앞의 12자리 숫자에 가중치를 곱하고 합산
    sum = 0
    for i in range(12):
        sum += int(jumin[i]) * weights[i]

    # 11로 나눈 나머지 값을 구한다
    remainder = sum % 11

    # 11에서 나머지 값을 뺀다
    check_digit = (11 - remainder) % 10  # 결과가 10인 경우를 대비하여 % 10

    # 연산의 결과 값이 주민번호의 마지막 자리의 수와 같은지 비교
    return check_digit == int(jumin[-1])


# 사용자로부터 주민등록번호 입력받기
jumin = input("주민등록번호 13자리를 입력하세요 (숫자만 입력): ")

if validate_jumin_number(jumin):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")