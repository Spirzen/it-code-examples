; NASM, MS-DOS (DOSBox), int 21h
section .data
    msg db 'Hello, World!$'

section .text
    global _start

_start:
    mov ah, 09h
    mov dx, msg
    int 21h

    mov ah, 4Ch
    mov al, 0
    int 21h
