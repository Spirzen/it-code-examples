;; 1) guard-clause через when + return-from
(defun safe-sqrt (x)
  (when (minusp x)
    (return-from safe-sqrt nil))
  (sqrt x))

;; 2) ранний выход из loop
(loop for x in '(3 7 11 20 5)
      when (> x 10)
      return x)

;; 3) разветвление по типу данных
(typecase data
  (string (length data))
  (list (length data))
  (t 0))
