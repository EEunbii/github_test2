# kg to (파운드)lb 변환 함수 만들어 주세요.
# 1kg=> 2.20462 파운드 (lb)
# while, try, except, break 사용

def kg_to_lb(kg):
   lb = kg * 2.20462
   return lb

while True:
    user_input = input("kg 값을 입력하세요:")
    try: 
        kg = float(user_input)
        lb = kg_to_lb(kg)
        print(f"{kg}kg은 {lb}lb입니다. ")
        break
    except ValueError:
        print("숫자를 입력해주세요:")
         
