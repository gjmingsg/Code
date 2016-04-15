(defun f (n lst) 
  (if (> n 0)
      (let ((x (car lst)))
	(cons (eval-ex x 9) (f (- n 1) (cdr lst))))
      nil))

(defun eval-ex(x n)
  (if (> n 0)
      (+ (f-item x n) (eval-ex x (- n 1)))
      1))

(defun f-item(x n)
  (if (> n 0)
      (* (/ x n) (f-item x (- n 1)))
      1))

(defun read-list ()
    (let ((n (read *standard-input* nil)))
        (if (null n)
            nil
            (cons n (read-list)))))


;(format t "~{~,8f~%~}" (f (read) (read-list)))
(format t "~{~,4f~%~}"  (f 4 '(20.0000 5.0000 0.5000 -0.5000)))
