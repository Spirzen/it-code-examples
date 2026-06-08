; NASM, Windows 32-bit, stdcall, точка входа _start
section .data
    msg db 'Hello, World!', 0
    caption db 'My First ASM Program', 0

section .text
    global _start
    extern _MessageBoxA@16
    extern _ExitProcess@4

_start:
    ; MessageBoxA(hWnd, lpText, lpCaption, uType)
    push 0               ; uType = MB_OK
    push caption
    push msg
    push 0               ; hWnd = NULL
    call _MessageBoxA@16

    push 0               ; exit code
    call _ExitProcess@4
