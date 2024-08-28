"""
Объявить переменные с помощью которых можно будет посчитать общую сумму покупки нескольких товаров.
Например создайте переменные chocolate_bar, coffee и тд.
(придумайте сами несколько) и посчитайте сумму вашей покупки.
"""

new_york_cheesecake = 1.15
venti_cappuccino = 2.69
grande_caramel_iced_latte = 3.40
blueberry_muffin = 1.67
take_away_fee = 0.23
tax_included = 1.02

total = new_york_cheesecake + venti_cappuccino + grande_caramel_iced_latte + blueberry_muffin + take_away_fee + tax_included

print("Thank you for visiting Starbucks!\n\nHere's your receipt:\n\nNew York Cheescake -  {}\n"
      "Venti Cappuccino -  {}\nGrande Caramel Latte - {}\nBlueberry Muffin - {}\nTake Away Fee - {}\n"
      "Tax - {}\n\nYour total is {}\nEnjoy :)".format(new_york_cheesecake, venti_cappuccino,grande_caramel_iced_latte,
                                                       blueberry_muffin, take_away_fee, tax_included, total))
