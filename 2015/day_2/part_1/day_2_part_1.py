from typing import Final

def calc_wrapping_feet(file_name:str)->int:
    l:Final[int] = 0
    w:Final[int] = 1
    h:Final[int] = 2
    
    l_w:Final[int] = 0
    w_h:Final[int] = 1
    h_l:Final[int] = 2

    sum:int = 0
    with open(file_name, "r") as file:
        for line in file:
            line_data:str = line.strip().split('x')
            str_data = [int(d) for d in line_data if d.isdigit()]

            lst_feet:list = []
            lst_feet.append(str_data[l]*str_data[w])
            lst_feet.append(str_data[w]*str_data[h])
            lst_feet.append(str_data[h]*str_data[l])
            sum += (2*lst_feet[l_w]) + (2*lst_feet[w_h]) + (2*lst_feet[h_l])
            sum += min(lst_feet)
    return sum


if __name__ == "__main__":
    try:
        wrapping_feet:int = calc_wrapping_feet("./input.txt")
        print(wrapping_feet)
    except Exception as e:
        print(e)