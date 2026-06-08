; NASM, Win64, консольная подсистема
default rel
section .data
    msg db 'Hello, Windows x64', 13, 10
    msg_len equ $ - msg
    bytes_written dq 0

section .text
    global main
    extern GetStdHandle
    extern WriteFile
    extern ExitProcess

main:
    push rbp
    mov rbp, rsp
    sub rsp, 48              ; shadow + выравнивание + локальные

    mov rcx, -11             ; STD_OUTPUT_HANDLE
    call GetStdHandle
    mov rbx, rax             ; handle в rbx (callee-saved)

    mov rcx, rbx
    lea rdx, [msg]
    mov r8, msg_len
    lea r9, [bytes_written]
    mov qword [rsp+32], 0    ; lpOverlapped = NULL (5-й аргумент в shadow+stack)
    call WriteFile

    xor ecx, ecx
    call ExitProcess
