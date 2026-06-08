section .data
    filename db 'input.txt', 0
    size_msg db 'File size: ', 0

section .bss
    buffer   resb 4096
    num_buf  resb 20

section .text
    global _start

    ; itoa и print_str — как выше ...

_start:
    ; Открыть файл
    mov rax, 2
    mov rdi, filename
    mov rsi, 0          ; O_RDONLY
    mov rdx, 0
    syscall
    mov r12, rax        ; fd

    cmp rax, 0
    jl .error

    xor r13, r13        ; total = 0

.read_loop:
    mov rax, 0
    mov rdi, r12
    mov rsi, buffer
    mov rdx, 4096
    syscall

    test rax, rax
    jle .done

    add r13, rax
    jmp .read_loop

.done:
    mov rax, 3
    mov rdi, r12
    syscall             ; close

    ; Вывод результата
    mov rdx, 11
    mov rsi, size_msg
    call print_str

    lea rsi, [num_buf]
    mov rdi, r13
    call itoa

    mov rdx, rax
    lea rsi, [num_buf]
    call print_str

    mov rsi, newline
    mov rdx, 1
    call print_str

    mov rax, 60
    mov rdi, 0
    syscall

.error:
    mov rax, 60
    mov rdi, 1          ; exit code 1
    syscall
