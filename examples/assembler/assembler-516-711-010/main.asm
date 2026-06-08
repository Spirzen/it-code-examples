section .data
    arr dq 15, -3, 42, 7, 29, -10, 100
    arr_len equ ($ - arr) / 8
    msg db 'Max: ', 0

section .bss
    num_buf resb 20

section .text
    global _start

    ; Подпрограмма itoa (как в предыдущем примере, сокращена)
    ; ... (вставьте itoa здесь или вынесите в отдельный файл) ...

find_max:
    mov rcx, arr_len
    mov rsi, arr
    mov rax, [rsi]      ; первый элемент — текущий максимум
    dec rcx
    jz .done
.next:
    add rsi, 8
    mov rdx, [rsi]
    cmp rdx, rax
    jle .skip
    mov rax, rdx
.skip:
    loop .next
.done:
    ret

print_str:
    mov rax, 1
    mov rdi, 1
    syscall
    ret

_start:
    call find_max        ; RAX = максимум

    lea rsi, [num_buf]
    mov rdi, rax
    call itoa

    ; Вывод "Max: "
    mov rdx, 5
    mov rsi, msg
    call print_str

    ; Вывод числа
    mov rdx, rax
    lea rsi, [num_buf]
    call print_str

    ; Новая строка
    mov rdx, 1
    mov rsi, newline
    call print_str

    mov rax, 60
    mov rdi, 0
    syscall
