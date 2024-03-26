;declare variable
(declare-const A (_ BitVec 2))
(declare-const B (_ BitVec 3))

;First
(push)
(assert (not (= ((_ extract 5 2) (concat #b110 A B)) (concat #b0 A ((_ extract 2 2) B)))))
(check-sat)
(pop)

;Second
(push)
(assert (not (= (concat #b110 (concat #b11 A) B) (concat #b11011 A B))))
(check-sat)
(pop)

;Thrid
(push)
(assert (not (= 
        ((_ extract 8 4) (concat #b110 (concat #b11 A) B)) 
        (concat #b1011 ((_ extract 1 1) A))
)))
(check-sat)
(pop)

