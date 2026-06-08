; rdi = адрес A, rsi = адрес B, rdx = адрес результата, rcx = число слов (N)
add_words:
    xor rax, rax              ; CF := 0
.loop:
    mov r8, [rdi]
    adc r8, [rsi]             ; r8 = A[i] + B[i] + CF
    mov [rdx], r8
    add rdi, 8
    add rsi, 8
    add rdx, 8
    loop .loop                  ; dec rcx; jnz — классический счётчик
    setc al                     ; al = 1, если был перенос за старший разряд
    movzx rax, al
    ret
