section .data
    arr dd 1.0, 2.0, 3.0, 4.0
    n   dq 4

section .text
global sum_array
sum_array:
    xorps xmm0, xmm0          ; sum = 0
    xor rcx, rcx
    mov rcx, [rel n]
    lea rbx, [rel arr]
.loop:
    movss xmm1, [rbx]
    addss xmm0, xmm1
    add rbx, 4
    dec rcx
    jnz .loop
    ret                       ; результат в xmm0
