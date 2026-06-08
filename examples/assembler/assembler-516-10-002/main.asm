%define SYS_WRITE 1
%define STDOUT    1

%macro write 2
    mov rax, SYS_WRITE
    mov rdi, STDOUT
    mov rsi, %1
    mov rdx, %2
    syscall
%endmacro

section .rodata
    hello db 'Hi', 10
    hello_len equ $ - hello

section .text
global _start
_start:
    write hello, hello_len
    mov rax, 60
    xor rdi, rdi
    syscall
