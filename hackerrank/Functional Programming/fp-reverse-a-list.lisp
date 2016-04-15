(defun f(lst)
  (if (null lst)
      nil
      (append (f (cdr lst)) (cons (car lst) nil))))
	  
(defun read-list ()
    (let ((n (read *standard-input* nil)))
        (if (null n)
            nil
            (cons n (read-list)))))

;(format t "~{~d~%~}" (f 1 1))
;(format t "~{~d~%~}" (f (read-list)))
