# 입력 검증 및 에러 처리 추가
# 잘못된 입력 값(숫자가 아닌 값, 음수 값 등..)을 처리하도록 기능을 추가해주세요.
# 유효하지 않은 메뉴 선택 시 경고 메시지 또는 사용방법 재안내를 해주세요.
# gitmoji는 bug 로 선택!!

receipts = []
balance = 3000

while True:
    try:
        select_num = int(input("사용하실 기능을 선택해주세요. (1: 입금, 2: 출금, 3: 영수증 보기, 4: 종료)"))

        if select_num == 4:
            break
        elif select_num == 1:  # 입금
            try:
                deposit_amount = int(input("입금하실 금액을 입력해주세요 : "))
                if deposit_amount > 0:
                    balance += deposit_amount
                    receipts.append(("입금", deposit_amount, balance))
                    print(f'현재 입금액은 {deposit_amount}원\n현재 잔액은 {balance}원 입니다.')
                else:
                    print("0 이상의 금액만 입력해주시기 바랍니다.")
            except ValueError:
                print("유효한 숫자를 입력해주세요.")
        elif select_num == 2:  # 출금
            try:
                withdraw_amount = int(input("출금하실 금액을 입력해주세요 : "))
                if withdraw_amount > 0:
                    withdraw_amount = min(balance, withdraw_amount)
                    balance -= withdraw_amount
                    receipts.append(("출금", withdraw_amount, balance))
                    print(f'현재 출금액은 {withdraw_amount}원\n현재 잔액은 {balance}원 입니다.')
                else:
                    print("0 이상의 금액만 입력해주시기 바랍니다.")
            except ValueError:
                print("유효한 숫자를 입력해주세요.")
        elif select_num == 3:  # 영수증 보기
            print("<=영수증=>")
            if receipts:
                for record in receipts:
                    print(f"{record[0]}: {record[1]}원 | 잔액: {record[2]}원")
            else:
                print("기록된 영수증이 없습니다.")
        else:
            print("유효한 메뉴 번호를 선택해주세요. (1, 2, 3, 4)")
    except ValueError:
        print("유효한 숫자를 입력해주세요. (1, 2, 3, 4)")

print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 입니다 ^^')


