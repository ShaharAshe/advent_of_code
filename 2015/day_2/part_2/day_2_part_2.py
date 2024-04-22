from typing import Final

def calc_wrapping_feet(file_name:str)->int:
    l:Final[int] = 0
    w:Final[int] = 1
    h:Final[int] = 2

    sum:int = 0
    with open(file_name, "r") as file:
        for line in file:
            line_data:str = line.strip().split('x')
            str_data = [int(d) for d in line_data if d.isdigit()]

            lst_feet:list = []
            lst_feet.append(str_data[l])
            lst_feet.append(str_data[w])
            lst_feet.append(str_data[h])
            feet_ribon_bow = max(lst_feet)
            lst_feet.remove(max(lst_feet))
            
            feet_ribon_wrap = 0
            for f in lst_feet:
                feet_ribon_wrap += f*2
                feet_ribon_bow *= f
            sum += feet_ribon_wrap + feet_ribon_bow
    return sum


if __name__ == "__main__":
    try:
        wrapping_feet:int = calc_wrapping_feet("./input.txt")
        print(wrapping_feet)
    except Exception as e:
        print(e)