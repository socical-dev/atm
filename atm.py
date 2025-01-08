# 출금 요청한 금액을 받는 변수 : withdraw_amount
# 출금을 요청한 금액을 balance 변수에서 뺀 결과가 들어가도록 코드를 작성해주세요.
# 영수증에 다음 순으로 값이 들어가도록 코드를 만들어주세요 -> ("출금", withdraw_amount, balance) 순으로 데이터 넣어주세요.
# 가지고 있는 금액보다 출금을 원하는 금액이 클 때 가지고 있는 금액만 출금되도록 코드를 작성해주세요.
# 단, 영수증에 내역은 변경되지 않아야 하며 입금 또는 출금이 진행될때마다 이력이 기록됩니다.
# 영수증 변수는 : receipts

receipts = []
balance = 3000

while True:
    select_num = input("사용하실 기능을 선택해주세요. (1: 입금, 2: 출금, 3: 영수증 보기, 4: 종료)")

    if select_num == "4":
        break
    elif select_num == "1":
        deposit_amount = int(input("입금하실 금액을 입력해주세요 : "))
        balance += deposit_amount
        receipts.append(("입금", deposit_amount, balance))
        print(f'현재 입금액은 {deposit_amount}원\n현재 잔액은 {balance}원 입니다.')
    elif select_num == "2":
        withdraw_amount = int(input("출금하실 금액을 입력해주세요 : "))
        # if balance > withdraw_amount:
        #     balance -= balance - withdraw_amount
        # else:
        #     balance = 0
        # 또는
        withdraw_amount = min (balance, withdraw_amount)
        balance -= withdraw_amount
        receipts.append(("출금", withdraw_amount, balance))
        print(f'현재 출금액은 {withdraw_amount}원\n현재 잔액은 {balance}원 입니다.')
    else:
        print(f'영수증\n{receipts}\n입니다.')
        
print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 입니다 ^^')


