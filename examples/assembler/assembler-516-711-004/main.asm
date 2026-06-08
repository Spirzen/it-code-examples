; Открыть исходный файл
mov rax, 2
mov rdi, src_name
mov rsi, 0
syscall
mov r12, rax        ; сохраняем дескриптор

; Открыть целевой файл (создать, если нет)
mov rax, 2
mov rdi, dst_name
mov rsi, 0x441      ; O_CREAT | O_WRONLY | O_TRUNC
mov rdx, 0o644
syscall
mov r13, rax

; Чтение и запись в цикле
.read_loop:
    mov rax, 0
    mov rdi, r12
    mov rsi, buffer
    mov rdx, 1024
    syscall
    test rax, rax
    jle .done           ; <= 0 — конец или ошибка

    mov rbx, rax        ; сохраняем количество байт
    mov rax, 1
    mov rdi, r13
    mov rsi, buffer
    mov rdx, rbx
    syscall

    jmp .read_loop

.done:
    ; Закрыть оба файла
    mov rax, 3
    mov rdi, r12
    syscall
    mov rax, 3
    mov rdi, r13
    syscall
