(defclass shape () ())

(defclass circle (shape)
  ((radius :initarg :radius :accessor radius)))

(defclass rectangle (shape)
  ((width :initarg :width :accessor width)
   (height :initarg :height :accessor height)))

(defgeneric area (shape))

(defmethod area ((c circle))
  (* pi (expt (radius c) 2)))

(defmethod area ((r rectangle))
  (* (width r) (height r)))

;; Использование
(let ((shapes (list (make-instance 'circle :radius 2)
                    (make-instance 'rectangle :width 3 :height 4))))
  (mapcar #'area shapes))  ; → (12.566... 12)
