extern printf
extern exit

section .data
    fmt db 'Hello from libc!', 10, 0

section .text
    global main

main:
    push rbp
    mov rbp, rsp

    mov rdi, fmt
    xor rax, rax      ; количество векторных регистров = 0
    call printf

    mov rdi, 0
    call exit
