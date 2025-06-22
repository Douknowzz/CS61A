;;; non-empty subsets of integer list s that have an even sum
(define (even-subsets s)
    (if (null? s) nil
        (append (even-subsets (cdr s))
                (subsets-helper even? s))))

;;; non-empty subsets of integer list s that have an odd sum
(define (odd-subsets s)
    (if (null? s) nil
        (append (odd-subsets (cdr s))
                (subsets-helper odd? s))))

(define (subsets-helper f s)
    (append
        (map (lambda (t) (cons (car s) t))
            (if (f (car s))
                (even-subsets (cdr s))
                (odd-subsets (cdr s))))
        (if (f (car s)) 
            (list (list (car s))) 
            nil
        )
    )
)

;;; non-empty subsets of s
(define (nonempty-subsets s)
  (if (null? s) nil
    (let ((rest (nonempty-subsets (cdr s))))
      (append rest
        (map (lambda (t) (cons (car s) t)) rest)
        (list (list (car s)))))))

;;; non-empty subsets of integer list s that have an even sum
(define (even-subsets s)
  (filter (lambda (s) (even? (apply + s))) (nonempty-subsets s)))