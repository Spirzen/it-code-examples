CLASS-ID. BankAccount.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 balance      PIC 9(9)V99.

METHOD DIVISION.
*> Конструктор
METHOD-ID. NEW.
PROCEDURE DIVISION USING BY VALUE initialAmount AS BINARY-LONG.
    MOVE initialAmount TO balance.
END METHOD NEW.

*> Метод пополнения
METHOD-ID. Deposit.
PROCEDURE DIVISION USING BY VALUE amount AS BINARY-LONG.
    ADD amount TO balance.
END METHOD Deposit.

*> Геттер баланса
METHOD-ID. GetBalance.
PROCEDURE DIVISION RETURNING ret AS BINARY-LONG.
    MOVE balance TO ret.
END METHOD GetBalance.

END CLASS BankAccount.
