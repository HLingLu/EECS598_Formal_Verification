;declare variable
(declare-const A (_ BitVec 2))
(declare-const B (_ BitVec 3))

(assert (not (= ((_ extract 5 2) (concat #b110 A B)) (concat #b0 A ((_ extract 2 2) B)))))
(check-sat)
