(defun f (n list) 
  ;; Complete this function
  (if (null list)
      nil
      (append (list-n n (car list)) (f n (cdr list)))))

(defun list-n (n item)
  (if (> n 0)
      (cons item (list-n (- n 1) item))))

(defun read-list ()
    (let ((n (read *standard-input* nil)))
        (if (null n)
            nil
            (cons n (read-list)))))

;(format t "~{~d~%~}" (f 1 1))
(format t "~{~d~%~}" (f (read) (read-list)))
