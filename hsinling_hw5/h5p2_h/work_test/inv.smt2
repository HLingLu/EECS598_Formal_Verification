; inductive invariant
(define-fun .induct_inv () Bool (! 
; size 1
(and
	property
)
 :invar-property 1))

; inductive invariant next
(define-fun .induct_inv_next () Bool 
; size 1
(and
	property$next
)
)

(echo "asserting design: transition relation and global constraints")
(assert .trans)

(push 1)
(echo "checking (initial -> proof)")
(assert (and .init (not .induct_inv)))
(check-sat)
(pop 1)

(push 1)
(echo "checking (proof -> property)")
(assert (and .induct_inv (not property)))
(check-sat)
(pop 1)

(push 1)
(echo "checking (proof is inductive)")
(assert (and .induct_inv (not .induct_inv_next)))
(check-sat)
(pop 1)


