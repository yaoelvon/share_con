# -*- coding: utf-8 -*-
# @date 2016/09/20
# @author yfeng@vwms.cn
# @desc the usage of python's try...except, finally
#       question 1: Why to use 'finally'?
# @record
#


def try_except_normal():
    # 初始化资源
    count = 0
    try:
        count += 1
        if count == 1:
            raise Exception("Exception")
    except Exception, data:
        print "except {0}".format(data)

    # 释放资源
    count = 0


def try_multi_except_no_finally(num):
    # 初始化资源
    count = 0
    try:
        count += num
        if count == 1:
            raise AttributeError("AttributeError")
        elif count == 2:
            raise ValueError("ValueError")
    except AttributeError, data:
        print "except {0}".format(data)
        count = 0
        return
    except ValueError, data:
        print "except {0}".format(data)
        count = 0
        return

    # 释放资源
    count = 0


def try_multi_except_finally(num):
    # 初始化资源
    count = 0
    try:
        count += num
        if count == 1:
            raise AttributeError("AttributeError")
        elif count == 2:
            raise ValueError("ValueError")
    except AttributeError, data:
        print "except {0}".format(data)
        return
    except ValueError, data:
        print "except {0}".format(data)
        return
    finally:
        # 释放资源
        count = 0


if __name__ == '__main__':
    print "1111111"
    try_except_normal()
    print ""

    print "2222222"
    try_multi_except_no_finally(1)

    try_multi_except_no_finally(2)
    print ""

    print "333333"
    try_multi_except_no_finally(1)

    try_multi_except_no_finally(2)


