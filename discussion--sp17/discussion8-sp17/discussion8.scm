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