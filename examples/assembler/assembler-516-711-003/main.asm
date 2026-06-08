my_function:
    push rbp
    mov rbp, rsp
    sub rsp, 16              ; два 8-байтовых локальных слова

    mov [rbp - 8], rdi       ; сохранили первый аргумент
    mov [rbp - 16], rsi      ; сохранили второй аргумент

    ; ... вычисления ...

    mov rax, [rbp - 8]       ; загрузили результат
    mov rsp, rbp
    pop rbp
    ret
