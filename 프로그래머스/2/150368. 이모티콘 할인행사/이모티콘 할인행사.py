from itertools import product

def solution(users, emoticons):
    discount_percent = {10: 0.9, 20: 0.8, 30: 0.7, 40: 0.6}
    answer = []
    product_of_percent = product(discount_percent.keys(), repeat=len(emoticons))
    for each_product in product_of_percent:
        user_num, total_price = 0, 0
        for target_percent, price in users:
            each_price = 0
            for idx, each_percent in enumerate(each_product):
                if target_percent <= each_percent:
                    each_price += (discount_percent[each_percent] * emoticons[idx])
            if each_price >= price:
                user_num += 1
            else:
                total_price += each_price
        answer.append([user_num, total_price])

    ans = sorted(answer, key=lambda x: (-x[0], -x[1]))[0]

    return ans

