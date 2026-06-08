; rdi = A, rsi = B, N=2 слова; результат: rax=1 если A>B (беззнаково), иначе 0
cmp_u128_gt:
    mov rax, [rdi + 8]      ; старшее слово A
    cmp rax, [rsi + 8]
    ja  .a_greater
    jb  .not_greater
    mov rax, [rdi]          ; равны старшие — сравнить младшие
    cmp rax, [rsi]
    ja  .a_greater
.not_greater:
    xor rax, rax
    ret
.a_greater:
    mov rax, 1
    ret
