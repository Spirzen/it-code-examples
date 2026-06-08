; NASM, Linux i386, точка входа _start
section .data
    msg db 'Hello, world!', 0xA
    len equ $ - msg

section .text
    global _start

_start:
    ; write(1, msg, len) — sys_write = 4 в таблице i386
    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    mov edx, len
    int 0x80

    ; exit(0) — sys_exit = 1
    mov eax, 1
    mov ebx, 0
    int 0x80
