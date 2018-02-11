(define (factorial x)
	(if (= x 1) 
		x
		(* x (factorial (- x 1)))
	)
)





(define (fib n)
	(if (< n 2) 
		1
		(+ (fib (- n 1)) (fib (- n 2)))
	)
)



(define (contact a b)
	(if (null? a) b
		(cons (car a)
			(contact (cdr a) b))
	)

)

;def contact(a, b):
;	if a = Link.empty:
;		return b
;	else:
;		return Link(a.first, contact(a.rest, b))
; 
(contact '(1 2 3) '(4 5 6))



(define (replicate x n)
	(if (equal? n 0) nil
		(cons x (replicate x (- n 1)))

	)
)


; def replicate(x, n):
; 	if n == 0:
; 		return Link.empty
; 	else:
; 		return Link(x, replicate(x, n-1))