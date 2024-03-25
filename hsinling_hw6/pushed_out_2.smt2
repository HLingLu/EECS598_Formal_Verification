;declare variable
(declare-const A (_ BitVec 2))
(declare-const B (_ BitVec 3))

(assert (not (= (concat #b110 (concat #b11 A) B) (concat #b11011 A B))))
(check-sat)
