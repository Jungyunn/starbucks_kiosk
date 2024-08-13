def add_menu(item_list):
    print("========== Add Menu ==========")
    menu_list = ['아메리카노', '카페라떼', '콜드브루', '에스프레소', '아이스티', '말차라떼']
    end_key = ['동작 취소', '동작취소']
    i = 0
    
    while True:
        user_input = input(f"{i+1}.")

        if (user_input in end_key or len(item_list.beverages) == 10):
            break

        elif user_input not in menu_list:
            print("잘못된 메뉴입니다. 다시 입력해주세요")

        else: 
            print(f"{i+1}. {user_input}")
            item_list.beverages.append(user_input)
            item_list.total_price += item_list.price_info[user_input] # 총 가격 출력
            i += 1

    return item_list