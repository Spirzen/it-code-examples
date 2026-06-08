; Метод 1: loop (медленнее на современных CPU)
sum_loop:
    mov rcx, len
    mov rsi, arr
    xor rax, rax
.add:
    add rax, [rsi]
    add rsi, 8
    loop .add
    ret

; Метод 2: dec + jnz (быстрее)
sum_fast:
    mov rcx, len
    mov rsi, arr
    xor rax, rax
.add:
    add rax, [rsi]
    add rsi, 8
    dec rcx
    jnz .add
    ret
