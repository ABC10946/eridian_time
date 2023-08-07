import time

number_dict = {'0': 'ℓ', '1': 'I', '2': 'V', '3': 'λ', '4': '+', '5': '∀'}


def convert_to_erid_num(num_str):
    return ''.join([number_dict[x] for x in num_str])


def dec_to_hexa(num):
    hexa_list = []
    if num == 0:
        hexa_list.append(0)

    while num != 0:
        hexa_list.append(num % 6)
        num = num // 6

    hexa_list_str = list(map(str, hexa_list))
    return ''.join(reversed(hexa_list_str))


def main():
    while True:
        num = int(time.time()//2.366)
        hexa_num = dec_to_hexa(num)
        eridian_num = convert_to_erid_num(hexa_num)
        print(eridian_num)
        time.sleep(2.366)


if __name__ == '__main__':
    main()
