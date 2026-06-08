section .data
    result_msg db 'Factorial: ', 0
    newline    db 10

section .bss
    buffer     resb 20

section .text
    global _start

; Функция: преобразует число в строку (десятичное)
; вход: RDI = число, RSI = буфер (заполняется задом наперёд)
; выход: RAX = длина строки
itoa:
    mov rax, rdi
    mov rdi, rsi
    add rdi, 19        ; указываем на конец буфера
    mov byte [rdi], 0  ; нулевой терминатор
    dec rdi
    mov rbx, 10
    cmp rax, 0
    jnz .loop
    mov byte [rdi], '0'
    dec rdi
    jmp .done
.loop:
    xor rdx, rdx
    div rbx
    add dl, '0'
    mov [rdi], dl
    dec rdi
    test rax, rax
    jnz .loop
.done:
    inc rdi
    mov rax, rsi
    sub rax, rdi
    neg rax
    ret

; Функция: факториал
; вход: RDI = n
; выход: RAX = n!
factorial:
    cmp rdi, 1
    jle .base
    push rdi
    dec rdi
    call factorial
    pop rbx
    imul rax, rbx
    ret
.base:
    mov rax, 1
    ret

_start:
    mov rdi, 6                 ; вычисляем 6!
    call factorial

    lea rsi, [buffer]
    mov rdi, rax
    call itoa                  ; RAX = длина

    ; Вывод "Factorial: "
    mov rax, 1
    mov rdi, 1
    mov rsi, result_msg
    mov rdx, 11
    syscall

    ; Вывод числа
    mov rax, 1
    mov rdi, 1
    lea rsi, [buffer]
    ; длина уже в RAX
    syscall

    ; Новая строка
    mov rax, 1
    mov rdi, 1
    mov rsi, newline
    mov rdx, 1
    syscall

    ; Завершение
    mov rax, 60
    mov rdi, 0
    syscall
