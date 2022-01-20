import textwrap


rules_dict = {'0000' : '0', '0001' : '0', '0010' : '0', '0011' : '0', '0100' : '0', '0101' : '0', '0110' : '1', '0111' : '1', 
              '1000' : '0', '1001' : '0', '1010' : '1', '1011' : '1', '1100' : '1', '1101' : '1', '1110' : '1', '1111' : '1'}  


def convert_to_triangle(a):
    if len(a) == 64:
        z = [a[:3], a[15], a[16:19], a[3], a[4:7], a[19], a[20:23], a[7], a[8:11], a[23], a[24:27], a[11], a[12:15], a[27], a[28:31],
            a[39], a[40:43], a[31], a[32:35], a[43], a[44:47], a[35], a[36:39], a[47], a[48:51], a[55], a[56:59], a[51], a[52:55], a[59], a[60:]]
    if len(a) == 16:
        z = [a[:3], a[7], a[8:11], a[3], a[4:7], a[11], a[12:]]
    z = ''.join(z)
    return z


def cell_list(input_data: str):
    cell = textwrap.wrap(input_data, 4)
    return cell


def logic(a):
    new_list = []
    for i in a:
        for k, v in rules_dict.items():
            if i == k:
                new_list.append(v)
    result = ''.join(new_list)
    print(result)
    if len(result) != 1:
        my_dump(result, first_run=False)


def my_dump(input_data, first_run: bool = True):

    if len(input_data) <= 64 and first_run:
        a = cell_list(convert_to_triangle(input_data))
        logic(a)
    
    if len(input_data) <= 16 and not first_run:
        a = cell_list(input_data)
        logic(a)


if __name__ == '__main__':
    my_dump(input_data=input('Введите число: '))


