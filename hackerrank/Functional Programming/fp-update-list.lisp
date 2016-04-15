(defun f(lst)
  (if (null lst)
      nil
      (let ((item (car lst)))
	(if (< item 0)
	    (cons (- 0 item) (f (cdr lst)))
	    (cons item (f (cdr lst)))))))
	  
(defun read-list ()
    (let ((n (read *standard-input* nil)))
        (if (null n)
            nil
            (cons n (read-list)))))

;(format t "~{~d~%~}" (f 1 1))
(format t "~{~d~%~}" (f (read-list)))
