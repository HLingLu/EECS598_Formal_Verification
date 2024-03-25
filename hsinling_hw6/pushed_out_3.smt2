;declare variable
(declare-const A (_ BitVec 2))
(declare-const B (_ BitVec 3))

(assert (not (= 
        ((_ extract 8 4) (concat #b110 (concat #b11 A) B)) 
        (concat #b1011 ((_ extract 1 1) A))
)))
(check-sat)
