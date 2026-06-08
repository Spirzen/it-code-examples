section .text
global scale_array

; void scale_array(long *arr, long n, long factor)
; rdi = arr, rsi = n, rdx = factor
scale_array:
    push rbx
    mov  rbx, rdi          ; rbx = текущий указатель (callee-saved)
    test rsi, rsi
    jz   .done
.loop:
    imul qword [rbx], rdx  ; *arr[i] *= factor
    add  rbx, 8
    dec  rsi
    jnz  .loop
.done:
    pop  rbx
    ret
