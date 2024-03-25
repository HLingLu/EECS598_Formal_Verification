;declare variable
(declare-const w1_ori (_ BitVec 16))
(declare-const w2_ori (_ BitVec 16))
(declare-const w3_ori (_ BitVec 16))
(declare-const w1_opt (_ BitVec 16))
(declare-const w2_opt (_ BitVec 16))
(declare-const w3_opt (_ BitVec 16))

(declare-const w4 (_ BitVec 8))
(declare-const w5 (_ BitVec 8))
(declare-const w6 (_ BitVec 8))
(declare-const w7 (_ BitVec 8))
(declare-const w8 (_ BitVec 8))
(declare-const w9 (_ BitVec 8))

(declare-const condition (_ BitVec 1))

(declare-const t1 (_ BitVec 16))
(declare-const t2 (_ BitVec 32))
(declare-const t3 (_ BitVec 8))
(declare-const t4 (_ BitVec 8))

;set t1, t2, t3, t4
(assert (= t1 (ite (= condition #b1) (concat w6 w7) (concat w8 w9))))
(assert (= t2 (concat w4 t1 w5)))
(assert (= t3 (ite (= condition #b1) w6 w8)))
(assert (= t4 (ite (= condition #b1) w7 w9)))

;set original output and optimized output
(assert (= w1_ori ((_ extract 31 16) t2)))
(assert (= w2_ori ((_ extract 23 8) t2)))
(assert (= w3_ori ((_ extract 15 0) t2)))

(assert (= w1_opt (concat w4 t3)))
(assert (= w2_opt (concat t3 t4)))
(assert (= w3_opt (concat t4 w5)))

;check equivalent
(assert (not (= w1_ori w1_opt)))
(assert (not (= w2_ori w2_opt)))
(assert (not (= w3_ori w3_opt)))
(check-sat)
