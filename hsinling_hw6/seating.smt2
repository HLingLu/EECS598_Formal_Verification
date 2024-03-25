;declare variable
(declare-const C Int)
(declare-const J Int)
(declare-const M Int)
(declare-const P Int)

;set range from 0 to three
(assert (and (< C 4) (>= C 0))) 
(assert (and (< J 4) (>= J 0))) 
(assert (and (< M 4) (>= M 0))) 
(assert (and (< P 4) (>= P 0))) 

;J -> C, M -> P, 0 is right of 3
(assert (or (= (+ J 1) C) (and (= J 3) (= C 0))))
(assert (or (= (+ M 1) P) (and (= M 3) (= P 0))))

;don't sit in the same spot
(assert (not (= C J)))
(assert (not (= C M)))
(assert (not (= C P)))
(assert (not (= J P)))
(assert (not (= J M)))
(assert (not (= M P)))

;the output order is NESW
(check-sat)
(get-model)

(echo "JCMP")
;remove JCMP
(assert (not (and (= J 0) (= C 1) (= M 2) (= P 3))))
(check-sat)
(get-model)

(echo "CMPJ")
;remove CMPJ
(assert (not (and (= C 0) (= M 1) (= P 2) (= J 3))))
(check-sat)
(get-model)

(echo "MPJC")
;remove MPJC
(assert (not (and (= M 0) (= P 1) (= J 2) (= C 3))))
(check-sat)
(get-model)

(echo "PJCM")
;remove PJCM
(assert (not (and (= P 0) (= J 1) (= C 2) (= M 3))))
(check-sat)
