(defun f (n list)
  (if (null list)
      nil
      (let ((item (car list)))
	(if (>= n item)
	    (cons item (f n (cdr list)))
	    (f n (cdr list))))))
	  
(defun read-list ()
    (let ((n (read *standard-input* nil)))
        (if (null n)
            nil
            (cons n (read-list)))))

;(format t "~{~d~%~}" (f 1 1))
;(format t "~{~d~%~}" (f (read) (read-list)))
