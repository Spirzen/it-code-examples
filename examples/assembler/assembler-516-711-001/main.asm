extern malloc
extern free

section .text
    mov rdi, 1024      ; запрашиваем 1024 байта
    call malloc        ; возвращает указатель в RAX
    test rax, rax
    jz  alloc_failed

    ; используем память по адресу RAX
    mov [rax], byte 42

    ; освобождение
    mov rdi, rax
    call free
