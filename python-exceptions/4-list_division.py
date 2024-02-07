#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    div_res = 0
    for i in range(0, list_length):
        try:
            div_res = (my_list_1[i] / my_list_2[i])
        except TypeError:
            div_res = 0
            print("wrong type")
        except IndexError:
            div_res = 0
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
            div_res = 0
        finally:
            new.append(div_res)
    return new
