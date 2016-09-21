# -*- coding: utf-8 -*-
# @date 2016/09/21
# @author yfeng@vwms.cn
# @desc python tips
# @record
#


"""
1.Dict的for循环中避免使用低效的iteritems() 和 keys()

a = {}
for i in xrange(0, 1000000):
    a[i] = i
print(type(a))
print(len(a))
output:

<type 'dict'>
1000000

def for_func1():
    for x in a:
        pass

def for_func2():
    for x in a.keys():
        pass

def for_func3():
    for x,v in a.iteritems():
        pass

import timeit
print(timeit.timeit(for_func1, number=100))
print(timeit.timeit(for_func2, number=100))
print(timeit.timeit(for_func3, number=100))

output:
1.46062994003
2.23361301422
2.39151501656

2.for循环中获得index神器：enumerate

students = ('James', 'Andrew', 'Mark')
for i, student in enumerate(students):
    print i, student
output：
0 James
1 Andrew
2 Alice

3.想确定for循环完整结束，用else吧

for ele in ['a', 'b', 'c']:
    if ele == 'b':
        break
else: # no break
    print('for循环完整结束')
# break后，不运行else中的语句

for ele in ['a', 'b', 'c']:
    if ele == 'd':
        break
else: # no break
    print('!!! for循环完整结束 !!!')
output:
!!! for循环完整结束 !!!

4.迭代工具之chain连接器

import itertools

#把所有元素放到一个list中
a=[[1],[2],[3,4],[5,6],[7,8,9]]
print list(itertools.chain(*a))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
#甚至还能连接不同类型数据dict和list
b=[{'a': 1, 'b': 2},[2],[3,4],[5,6],[7,8,9]]
print list(itertools.chain(*b))
['a', 'b', 2, 3, 4, 5, 6, 7, 8, 9]

5.zip拉链函数

random_numbers = [1,2,3]
names = ('James', 'Andrew', 'Mark')
print zip(random_numbers, names)
d = dict(zip(random_numbers, names))
print d
output:
[(1, 'James'), (2, 'Andrew'), (3, 'Mark')]
{1: 'James', 2: 'Andrew', 3: 'Mark'}

li=[['a','b','c'],['d','e','f']]
print zip(*li)
output:
[('a', 'd'), ('b', 'e'), ('c', 'f')]

dots = [(1, 3), (2, 4), (3, 5)]
print zip(*dots)
output:
[(1, 2, 3), (3, 4, 5)]

6.with语句的保护性

with open('/etc/passwd', 'r')as f:
    print f.read()
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
messagebus:x:102:105::/var/run/dbus:/bin/false
ntp:x:103:109::/home/ntp:/bin/false
sshd:x:104:65534::/var/run/sshd:/usr/sbin/nologin

print(f)
<closed file '/etc/passwd', mode 'r' at 0x7f2fb884adb0>
With 语句结束会自动关闭文件!

7.数据结构之counter-计数神器

import collections

print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print collections.Counter({'a':2, 'b':3, 'c':1})
print collections.Counter(a=2, b=3, c=1)
Counter({'b': 3, 'a': 2, 'c': 1})
Counter({'b': 3, 'a': 2, 'c': 1})

Counter({'b': 3, 'a': 2, 'c': 1})

c = collections.Counter()
print 'Initial :', c

c.update('abcdaab')
print 'Sequence:', c

c.update({'a':1, 'd':5})
print 'Dict    :', c
Initial : Counter()
Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})

Dict    : Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})

c = collections.Counter()
with open('/usr/share/dict/words', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())
print 'Most common:'
for letter, count in c.most_common(3):
    print '%s: %7d' % (letter, count)
Most common:
s:   90113
e:   88833

i:   66986

8.数据结构之defaultdict-任何数据转成dict的神器

from collections import defaultdict

order = (
('Mark', 'Steak'),
('Andrew', 'Veggie Burger'),
('James', 'Steak'),
('Mark', 'Beer'),
('Andrew', 'Beer'),
('James', 'Wine'),
)
#key已经确定, 返回value是list的工厂
group_order = defaultdict(list)

for name, menu_item in order:
    group_order[name].append(menu_item)

print group_order
print group_order['Mark']
defaultdict(<type 'list'>, {'James': ['Steak', 'Wine'], 'Andrew': ['Veggie Burger', 'Beer'], 'Mark': ['Steak', 'Beer']})

['Steak', 'Beer']

#key已经确定, 返回value是int的工厂
order_count = defaultdict(int)

for name, menu_item in order:
    order_count[menu_item] += 1

print order_count
defaultdict(<type 'int'>, {'Beer': 2, 'Steak': 2, 'Wine': 1, 'Veggie Burger': 1})

9.数据结构之OrderDict-记住插入数据的顺序

from collections import OrderedDict

li_order1=['a','b','c','c']
li_order2=['c','b','a','c']

d1 =  OrderedDict()
d2 = OrderedDict()

for x in li_order1:
    d1[x] = 1
print d1
OrderedDict([('a', 1), ('b', 1), ('c', 1)])

for x in li_order2:
    d2[x] = 1
print d2
print d2['b']
OrderedDict([('c', 1), ('b', 1), ('a', 1)])

1

10.数据结构之namedtuple-闪电般构造一个类

from collections import namedtuple
#namedtuple is a CLASS
Parts = namedtuple('Parts', 'id_num desc cost amount')
auto_parts = Parts(id_num='1234', desc='Ford Engine',
                   cost=1200.00, amount=10)
print auto_parts.id_num,  auto_parts.amount
output:

1234 10

auto_parts = ('1234', 'Ford Engine', 1200.00, 10)
print auto_parts[2]
output:
1200.0

id_num, desc, cost, amount = auto_parts
print id_num
Parts = {'id_num':'1234', 'desc':'Ford Engine',
                      'cost':1200.00, 'amount':10, 'profit': 10000}
parts = namedtuple('Parts', Parts.keys())(**Parts)
print parts
output:
1234

Parts(profit=10000, amount=10, cost=1200.0, id_num='1234', desc='Ford Engine')

# define new type
BuildInput = namedtuple('BuildInput', ['name', 'files'])
# test scenarios
b1 = BuildInput('test_build_1', ['file1.txt', 'file2.txt'])

b2 = BuildInput(name='test_build_2', files=['file3.txt', 'file4.txt'])

another_b1 = BuildInput(name='test_build_1', files=['file1.txt', 'file2.txt'])

print b1 != b2
print b1 == another_b1

#recall something??
a = [1,2,3]
b = a
a[1] = 0
print b
output:
True
True
[1, 0, 3]

11.一行生成器与一行list写法区分

a = (x**2 for x in [1,2,3,4,5])

print(type(a))
for i in a:
    print(i)
output:
<type 'generator'>
1
4
9
16
25

b = [x**2 for x in [1,2,3,4,5]]
print(b)
output:
[1, 4, 9, 16, 25]

12.python函数式编程入门—map&&reduce

name_lengths = map(len, ["Mary", "Isla", "Sam"])
print name_lengths
output:
[4, 4, 3]

squares = map(lambda x: x * x, [0, 1, 2, 3, 4])
print squares
output:
[0, 1, 4, 9, 16]

sum = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print sum
output:
10

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
heights = map(lambda x: x['height'],
              filter(lambda x: 'height' in x, people))
if len(heights) > 0:
    from operator import add
    average_height = reduce(add, heights) / len(heights)
print average_height
output:
120

13.python函数式编程入门-partial_function

import functools

def adder(x, y):
  return x + y

# it adds!
assert adder(1, 1) == 2
assert adder(5, 5) == 10
assert adder(6, 2) == 8

# pre fill y with the value 5
add_five = functools.partial(adder, y=5)

#now it adds 5!
# x=1, y=5
assert add_five(1) == 6
print add_five(1)
# x=5, y=5
assert add_five(5) == 10
# x=2, y=5
assert add_five(2) == 7
output:
6

"""
