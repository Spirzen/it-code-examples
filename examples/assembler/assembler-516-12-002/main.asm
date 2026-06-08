section .text
global dot_product

; float dot_product(const float *a, const float *b, long n)
; rdi=a, rsi=b, rdx=n  →  результат в xmm0
dot_product:
    xorps xmm0, xmm0
    test rdx, rdx
    jz   .done
.loop:
    movss xmm1, [rdi]
    mulss xmm1, [rsi]
    addss xmm0, xmm1
    add rdi, 4
    add rsi, 4
    dec rdx
    jnz  .loop
.done:
    ret
