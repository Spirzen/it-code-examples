       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-CURRENT-DATE.
           05  WS-YEAR      PIC 9(4).
           05  WS-MONTH     PIC 9(2).
           05  WS-DAY       PIC 9(2).

       01  WS-EMPLOYEE-RECORD.
           05  EMP-ID       PIC X(10).
           05  EMP-NAME     PIC X(30).
           05  EMP-SALARY   PIC 9(7)V99.
           05  EMP-STATUS   PIC X.
               88  ACTIVE   VALUE 'A'.
               88  INACTIVE VALUE 'I'.
               88  TERMINATED VALUE 'T'.
