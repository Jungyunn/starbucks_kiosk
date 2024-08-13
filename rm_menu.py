def remove_menu(item_list):
    print("========== Remove Menu ==========")
    print("현재 주문 음료: ", item_list.beverages)
    user_del_input = input("삭제할 메뉴들을 작성해주세요: ")
    print(user_del_input)
    user_del_list = user_del_input.split()
    print(user_del_list)

    for del_menu in user_del_list:
        item_list.beverages.remove(del_menu)
        item_list.total_price -= item_list.price_info[del_menu]
        print(del_menu,"가 삭제되었습니다")
        print("남은메뉴", item_list.beverages)

    return item_list