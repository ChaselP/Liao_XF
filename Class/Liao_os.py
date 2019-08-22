import os,logging
#logging.basicConfig(level=logging.INFO)
path=r'/Users/chaselchou/PycharmProjects/test/'

#输出path路径下所有文件与文件夹
print('All:',[x for x in os.listdir(path)])

# 输出path路径下所有文件夹
print('dir:',[x for x in os.listdir(path) if os.path.isdir(x)])

#使用walk方式输出path路径下所有文件夹
for root,dirs,files in os.walk(path):
    print('walk_dir:',dirs)

#传入绝对路径
for x in os.listdir(path):
    print(os.path.isdir(os.path.join(os.path.abspath(x),x)))

#查询指定path下包含字符串s的文件相对路径
def findFileWithStr(path,s):
    for root,dirs,files in os.walk(path):
        for file in files:
            if s in file:
                # lstrip方法未能返回正确结果
                # print(os.path.join(root,file).lstrip(path))
                relativePath=os.path.join(root,file).replace(path,'')
                print('./'+relativePath if relativePath[0]!='/' else '.'+relativePath)


findFileWithStr(path,'t')
