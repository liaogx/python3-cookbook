#内存映射的二进制文件，你想内存映射一个二进制文件到一个可变字节数组中，
# 目的可能是为了随机访问它的内容或者是原地做些修改。
#使用mmap模块来内存映射文件。下面是一个工具函数，向你演示了如何打开一个文件并以一种便捷方式内存映射这个文件。
import os
import mmap
def memory_map(filename,access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename,os.O_RANDOM)
    return mmap.mmap(fd,size,access=access)
#为了使用这个函数，你需要有一个已创建并且内容不为空的文件。 下面是一个例子，教你怎样初始创建一个文件并将其内容扩充到指定大小：
size = 10000
with open('data.bin','wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

#下面是一个利用 memory_map() 函数类内存映射文件内容的例子：
# m = memory_map('data.bin')
# print(len(m))   此处为什么会报错？？？？？？
# mmap() 返回的 mmap 对象同样也可以作为一个上下文管理器来使用， 这时候底层的文件会被自动关闭。比如：

# with memory_map('data.bin') as m:
#     print(len(m))  妈的的为什么这两行又报错？？？受不鸟了


