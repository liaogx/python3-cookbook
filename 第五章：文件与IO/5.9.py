#读取二进制数据到可变缓冲区中，读取可变数组使用文件对象的readinto()方法
import os.path
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename,'rb') as f:
        f.readinto(buf)
    return buf
#Write a sample file
with open('data.bin','wb') as f:
    f.write(b'Hello World')
buf = read_into_buffer('data.bin')
print(buf)
buf[0:5] = b'hELLO'
print(buf)
with open('newdata.bin','wb') as f:
    f.write(buf)













