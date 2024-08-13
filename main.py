# Main function
from Check_Menu import check_menu
from menu_add import add_menu
from order import order
from rm_menu import remove_menu

from enum import Enum

class ItemList():
    def __init__(self):
        self.beverages = []
        self.total_price = 0
        self.price_info = {'아메리카노': 4500, '카페라떼':5000, '콜드브루': 4900, '에스프레소':4000, '아이스티':5900, '말차라떼':6100}


class Menu(Enum):
    ADD = 1
    REMOVE = 2
    CHECK = 3
    ORDER = 4
    END = 5


def select():
    print("========== What Do You Want ==========")
    print("1. 음료 추가 ")
    print("2. 음료 삭제")
    print("3. 선택 음료 확인")
    print("4. 선택 음료 주문")
    print("5. 프로그램 종료")


def main():
    item_list = ItemList()
    while True:
        select()
        choice = int(input("선택: "))
        print("\n\n")

        if choice == Menu.ADD.value:
            add_menu(item_list)
            print("\n\n")
        elif choice == Menu.REMOVE.value:
            remove_menu(item_list)
            print("\n\n")
        elif choice == Menu.CHECK.value:
            check_menu(item_list)
            print("\n\n")
        elif choice == Menu.ORDER.value:
            if order(item_list):
                print("주문 완료. 프로그램을 종료합니다.")
                break
            else:
                
                print("주문 보류!")
                print("\n\n")
        elif choice == Menu.END.value:
            print("프로그램을 종료합니다")
            break
        else:
            print("잘못된 입력입니다. 동작을 취소합니다.")
            break

if __name__ == "__main__":
    main()