# for i in range(4):
#     name = 'v' + str(i)
#     locals()['v' + str(i)] = i
#     # v1,v2,v3 编辑器中会提示错误，但运行不会出问题
#     print(v1, v2, v3)
# 可以循环调用
# for index in range(4):
#     print(locals()['v' + str(index)])


exec("h{} = 10".format(5))
print(h5)
