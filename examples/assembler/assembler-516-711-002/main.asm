section .text
global _start

_start:
    mov rdi, 5
    call factorial
    ; результат в RAX
    mov rdi, rax
    mov rax, 60      ; sys_exit
    syscall

factorial:
    cmp rdi, 1
    jle .base_case
    push rdi         ; сохраняем текущий n
    dec rdi
    call factorial   ; рекурсивный вызов
    pop rbx          ; восстанавливаем n
    imul rax, rbx    ; RAX = RAX * n
    ret
.base_case:
    mov rax, 1
    ret
