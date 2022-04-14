# a=b'python'
# # print(a,type(a))                                     # b'python' <class 'bytes'>
# print(list(a))                                         # [112, 121, 116, 104, 111, 110]
# print(tuple(a))                                        #(112, 121, 116, 104, 111, 110)
# print(set(a))                                          # {104, 110, 111, 112, 116, 121}

# a=b'python'
# for i in a:
#     print(i,end=",")                           #112,121,116,104,111,110,

# c=b'[7,8,6]'
# print(list(c))                                 #[91, 55, 44, 56, 44, 54, 93]


# print(chr(91))                                  #[
# print(chr(55))                                  #7
# print(chr(44))                                  #,
# print(chr(56))                                  #8
# print(chr(44))                                   #,
# print(chr(54))                                  #6
# print(chr(93))                                   #]

# d=bytearray(b'python')
# print(d,type(d))                           # bytearray(b'python') <class 'bytearray'>
# d[0]=ord('P')
# print(d,type(d))                           #bytearray(b'Python') <class 'bytearray'
