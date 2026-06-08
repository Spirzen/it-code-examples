extern printf
extern exit

section .data
    fmt db 'Result: %ld', 10, 0

section .text
    global main

main:
    push rbp
    mov rbp, rsp

    mov rdi, fmt
    mov rsi, 42
    call printf

    mov rdi, 0
    call exit
