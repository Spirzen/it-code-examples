; main.asm
%define SYS_WRITE 1
%define SYS_EXIT  60
%define STDOUT    1

extern add_u64
extern msg
extern msg_len

section .text
global _start
_start:
    mov rdi, 40
    mov rsi, 2
    call add_u64          ; rax = 42

    mov rax, SYS_WRITE
    mov rdi, STDOUT
    mov rsi, msg
    mov rdx, [rel msg_len]
    syscall

    mov rax, SYS_EXIT
    xor rdi, rdi
    syscall
