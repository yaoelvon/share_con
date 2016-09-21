# -*- coding: utf-8 -*-
# @date 2016/09/20
# @author yfeng@vwms.cn
# @desc the usage of python's try...except, finally;
#       question 2: When 'finally' executed?
# @record
#


def normal_test():
    print "return statement: a"
    return "after return: b"


def try_multi_except_finally_order():
    try:
        print "try block: c"
        return normal_test()
    finally:
        print "finally block: d"


if __name__ == '__main__':
    print try_multi_except_finally_order()
