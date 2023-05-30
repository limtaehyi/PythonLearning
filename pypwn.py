from pwn import *

r = remote('127.0.0.1',1234)
r.send("hello, world!\n")
r.close()

elf = ELF('example_binary')
print(hex(elf.symbols['main'])) # print main's symbol address

p = process('example_binary')
p.sendline('input string')
output = p.recv()

#r.sendlineafter()
#r.recvuntil
