# 기본 금액 : balance
# 기본 금액에 돈을 넣어주세요
# while 문을 이용해서 입금, 출금, 영수증 보기, 종료라는 기능이 종료라는 버튼을 누르기 전까지 노출되도록 만들어주세요.
# 종료를 누르면 서비스를 종료한다는 메시지를 출력하고 현재 잔액을 보여주세요.

# 입금할 금액을 받는 변수 : deposit_amount
# 입금된 금액은 balance 변수에 추가되도록 코드를 작성해주세요.abs
# 영수증에 다음 순서로 값이 들어가도록 코드를 만들어주세요. -> "입금", "입금 요청액", "총액" 순으로 데이터 넣어주세요.
# 단, 영수증에 내역은 변경되지 않아야 하며 입금 또는 출금이 진행될 때마다 이력이 기록이 기록 됩니다.

deposit_amount = 0
balance = 1000

while True:
    select_num = input("사용하실 기능을 선택해주세요. (1: 입금, 2: 출급, 3: 영수증 보기, 4: 종료)")

    if select_num == "4":
        break
    elif select_num == "1":
        deposit_amount = input("입금하실 금액을 입력해주세요")
        beforeBalance = balance
        balance += int(deposit_amount)
        print(f'현재 입금액은 {beforeBalance}원\n입금 요청액은 {deposit_amount}원\n총액은 {balance}원 입니다.')


print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 입니다 ^^')
    


