       PERFORM UNTIL EOF-FLAG = "Y"
           READ INVOICE-FILE
               AT END
                   MOVE "Y" TO EOF-FLAG
               NOT AT END
                   EVALUATE INVOICE-STATUS
                       WHEN "N"
                           PERFORM PROCESS-NEW-INVOICE
                       WHEN "R"
                           PERFORM PROCESS-RETRY-INVOICE
                       WHEN OTHER
                           PERFORM LOG-UNKNOWN-STATUS
                   END-EVALUATE
           END-READ
       END-PERFORM
