section .text
global main
extern printf

main:
    push rbp
    mov rbp, rsp
    sub rsp, 16         ; выравнивание стека на 16 байт перед call в ABI

    lea rdi, [rel fmt]  ; 1-й аргумент C
    mov rsi, 42         ; 2-й
    xor rax, rax        ; для variadic: число XMM-регистров = 0
    call printf

    xor eax, eax
    leave
    ret

section .rodata
    fmt db 'value=%ld', 10, 0
