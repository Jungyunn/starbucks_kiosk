def check_menu(item_list):
    print(f"주문 품묵 총액 {item_list.total_price}입니다.")
    for i in item_list.beverages:
        print(f"{i}", end = ', ')
