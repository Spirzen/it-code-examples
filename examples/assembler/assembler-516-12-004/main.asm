section .text
global block_transform

; void block_transform(const unsigned char *in, unsigned char *out)
; rdi = in, rsi = out
block_transform:
    mov rcx, 16
.copy:
    mov al, [rdi]
    xor al, 0x5A              ; простая подстановка байта
    mov [rsi], al
    inc rdi
    inc rsi
    loop .copy
    ret
