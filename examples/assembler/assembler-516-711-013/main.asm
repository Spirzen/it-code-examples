section .data
    align 16
    vec_arr dd 1,2,3,4,5,6,7,8

section .text
sum_sse:
    pxor xmm0, xmm0           ; обнулить аккумулятор
    mov rsi, vec_arr
    mov rcx, 2                ; 8 элементов / 4 = 2 итерации

.loop:
    movdqa xmm1, [rsi]        ; загрузить 4 int32
    paddd xmm0, xmm1          ; сложить
    add rsi, 16
    loop .loop

    ; Горизонтальное сложение
    movhlps xmm1, xmm0
    paddd xmm0, xmm1
    pshufd xmm1, xmm0, 1
    paddd xmm0, xmm1
    movd eax, xmm0            ; результат в EAX
    ret
