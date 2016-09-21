# -*- coding: utf-8 -*-
# @date 2016/09/20
# @author yfeng@vwms.cn
# @desc the usage of python's try...except, finally;
#       What problem have we encountered?
# @record
#


def try_multi_except_finally_order_except():
    try:
        raise ValueError("ValueError")

    except ValueError, data:
        print "Except {0}: a".format(data)
        return "Return: b"
    finally:
        print "Doing Finally: c"
        # raise Exception

if __name__ == '__main__':
    print try_multi_except_finally_order_except()
