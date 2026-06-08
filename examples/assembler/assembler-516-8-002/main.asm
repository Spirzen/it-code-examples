; rdi = база массива слов, rcx = N (>= 1)
; по завершении r10 = бит, "выпавший" из старшего слова (переполнение)
shl_words_left_1:
    xor r10, r10              ; перенос в младшее слово = 0
    xor r11, r11              ; индекс слова
.loop:
    mov rax, [rdi + r11*8]
    mov rbx, rax
    shl rax, 1
    or rax, r10               ; втянуть перенос с предыдущего слова
    mov [rdi + r11*8], rax
    shr rbx, 63               ; исходный старший бит -> перенос для следующего
    mov r10, rbx
    inc r11
    loop .loop
    ret
