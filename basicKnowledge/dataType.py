'''***************************************
for data type test
***************************************'''
def testString():
    str = 'This is a string!'
    print(str)

    str = "This is a string too!"
    print(str)

    str = '''This 
        is
        a
        'long'
        "string"!
        *'''
    print(str)
    print(str.encode())
    print(str[-1])

    print(type(str))

def bytesTest():
    #help(bytes)
    a = bytes()
    print(a)

    b=bytes(3)
    print(b)

    c = bytes(range(15))
    print(c)

    d = b'\x61\x62\x63'
    print(d)
    print(type(d))

    d = bytes('study', 'utf-8')
    print(d)

    e=b'speek'
    print(e)
    f=e.replace(b'e', b'x')
    print(f)
    print(f.hex())

    g=bytes.fromhex('00 01 02 03 04 05 0e ff')
    print(g)

    h='This is a test function!'.encode().hex()
    print(h)

    i = 'This is a test function!'.encode()
    print(i)
    print(i[0])


def bytesarryTest():
    #help(bytearray)
    a = bytearray([0x42, 0x76])
    print(a.hex())
    print(a[0])
    print(a[-1])

def listTest():
    list = ['abcd', 786, 2.23, 'runoob', 70.2]
    tinylist = [123, 'runoob']

    print(list)  # 输出完整列表
    print(list[0])  # 输出列表第一个元素
    print(list[1:3])  # 从第二个开始输出到第三个元素
    print(list[2:])  # 输出从第三个元素开始的所有元素
    print(tinylist * 2)  # 输出两次列表
    print(list + tinylist)  # 连接列表

def setTest():
    student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

    print(student)  # 输出集合，重复的元素被自动去掉

    # 成员测试
    if 'Rose' in student:
        print('Rose 在集合中')
    else:
        print('Rose 不在集合中')

    # set可以进行集合运算
    a = set('abracadabra')
    b = set('alacazam')

    print(a)

    print(a - b)  # a 和 b 的差集

    print(a | b)  # a 和 b 的并集

    print(a & b)  # a 和 b 的交集

    print(a ^ b)  # a 和 b 中不同时存在的元素

def dictTest():
    dict = {}
    dict['one'] = 'This is one'
    dict[2] = 'This is two'
    tinydict = {'name': 'john', 'code': 5762, 'dept': 'sales'}

    print(dict['one'])  # 输出键为'one'的值
    print(dict[2])  # 输出键为2的值
    print(tinydict)  # 输出完整的字典
    print(tinydict.keys())  # 输出所有键
    print(tinydict.values())  # 输出所有值

def testDataType():
    print("Data type test:")
    testString()
    bytesTest()
    bytesarryTest()
    listTest()
    setTest()
    dictTest()



