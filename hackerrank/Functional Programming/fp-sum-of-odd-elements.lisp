(defun f(lst)
  (let ((acc 0))
    (dolist (item lst)
      (if (oddp item)
	 (setf acc (+ acc item))))
      acc))
	  
(defun read-list ()
    (let ((n (read *standard-input* nil)))
        (if (null n)
            nil
            (cons n (read-list)))))

;(format t "~{~d~%~}" (f 1 1))
(format t "~A~%" (f (read-list)))
