(defun f (n) 
  (if (> n 0)
      (cons n (f (- n 1)))
      nil))
(let ((x (coerce (read) 'integer)))
    (format t "~S" (length (f x))))
