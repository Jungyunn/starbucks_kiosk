def order(item_list):
    print(f"주문 품묵 총액 {item_list.total_price}입니다. 품목은 다음과 같습니다.")
    for i in item_list.beverages:
        print(f"{i}", end = ', ')
    aggre_ = int(input())
    if aggre_ == 1:
        print('주문이 완료되었습니다.\n 이용해주셔서 감사합니다.')
        return

    else:
        return