(defun f (list)
  (fp 0 list))

(defun fp(n list)
    (if (null list)
      nil
      (let ((item (car list)))
	(if (oddp n)
	    (cons item (fp (- n 1) (cdr list)))
	    (fp (- n 1) (cdr list))))))

(defun read-list ()
    (let ((n (read *standard-input* nil)))
        (if (null n)
            nil
            (cons n (read-list)))))

(f '(1 2 3 4 5 6))
;(format t "~{~d~%~}" (f (read) (read-list)))
