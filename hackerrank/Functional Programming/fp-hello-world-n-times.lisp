(defun fn(n)
  (if (> n 0)
      (progn (format t "Hello World~%")
             (fn (- n 1)))))

(fn 10)