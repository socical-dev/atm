# 기본 금액 : balance
# 기본 금액에 돈을 넣어주세요
# while 문을 이용해서 입금, 출금, 영수증 보기, 종료라는 기능이 종료라는 버튼을 누르기 전까지 노출되도록 만들어주세요.
# 종료를 누르면 서비스를 종료한다는 메시지를 출력하고 현재 잔액을 보여주세요.

balance = 1000

while True:
    select_num += input("사용하실 기능을 선택해주세요. (1: 입금, 2: 출급, 3: 영수증 보기, 4: 종료)")

    if select_num == "4":
        print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 입니다 ^^')
        break

