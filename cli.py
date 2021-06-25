years = 10
capital_10k = 10000
capital_1l = 100000
one_lakh = 100000
ten_thousand = 10000
crore = 10000000

while True:
    roi_str = input("year roi : ")
    roi = int(roi_str)
    base = round(1 + roi/100, 2)
    times = round(pow(base , years),2)
    final_capital_in_c10k_in_lakh = round(capital_10k * times /one_lakh, 2)
    final_capital_in_clakh_in_cr = round(capital_1l * times/crore,2)

    print(f"final capital c lakh in cr {final_capital_in_clakh_in_cr} final c10k in l {final_capital_in_c10k_in_lakh} times {times}")