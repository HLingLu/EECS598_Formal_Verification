; printed by MathSAT5 version 5.6.9 (0214d34392af) (Nov 10 2022 09:51:42, gmp 6.2.0, gcc 7.5.0, 64-bit)

 (set-logic ALL)

; state variables
(declare-fun .State () (_ BitVec 3))
(declare-fun .State$next () (_ BitVec 3))
(define-fun ..State () (_ BitVec 3) (! .State :next .State$next))
(declare-fun .T.Q () (_ BitVec 4))
(declare-fun .T.Q$next () (_ BitVec 4))
(define-fun ..T.Q () (_ BitVec 4) (! .T.Q :next .T.Q$next))

; input variables
(declare-fun .Reset () Bool)
(declare-fun .Reset$next () Bool)
(declare-fun .E () Bool)
(declare-fun .E$next () Bool)
(declare-fun .W () Bool)
(declare-fun .W$next () Bool)
(declare-fun .NL () Bool)
(declare-fun .NL$next () Bool)
(declare-fun .EL () Bool)
(declare-fun .EL$next () Bool)

; initial state
(define-fun .init () Bool (! 
; size 2
(and
	(= .State (_ bv0 3))
	(= .T.Q (_ bv10 4))
)
 :init true))

; transition relation main
(define-fun .T () Bool 
; size 2
(and
	(let ((.def_38 (= .State (_ bv6 3)))) (let ((.def_43 (= .State (_ bv7 3)))) (let ((.def_60 (not .NL))) (let ((.def_77 (= .T.Q (_ bv0 4)))) (let ((.def_101 (not .EL))) (let ((.def_102 (and (and .def_60 (and (not .E) (not .W))) .def_101))) (let ((.def_117 (= .State (_ bv2 3)))) (let ((.def_122 (= .State (_ bv4 3)))) (let ((.def_135 (and .def_77 (or .EL .def_102)))) (let ((.def_151 (not .def_102))) (= .State$next (ite .Reset (_ bv0 3) (ite (or .def_43 (or (= .State (_ bv5 3)) .def_38)) (ite .def_43 (ite (or (or .E .W) .def_60) (_ bv0 3) (_ bv2 3)) (ite .def_38 (ite .def_38 (ite (and .def_77 (or .NL (or .W (or .E .def_102)))) (_ bv7 3) (_ bv6 3)) (_ bv0 3)) (_ bv6 3))) (ite (or .def_117 .def_122) (ite .def_122 (_ bv6 3) (ite .def_117 (ite .def_135 (_ bv5 3) (ite .def_117 (ite .def_135 (_ bv0 3) (ite (and .def_101 (and (and .W .def_77) .def_151)) (_ bv3 3) (_ bv2 3))) (_ bv0 3))) (_ bv0 3))) (ite (= .State (_ bv1 3)) (_ bv2 3) (ite (and .def_77 (or .NL .def_102)) (_ bv1 3) (ite (and .def_60 (and .def_151 (and .def_77 .EL))) (_ bv4 3) (_ bv0 3))))))))))))))))))
	(let ((.def_43 (= .State (_ bv7 3)))) (let ((.def_205 (or (= .State (_ bv6 3)) .def_43))) (let ((.def_207 (or .def_205 (or (= .State (_ bv5 3)) (= .State (_ bv4 3)))))) (let ((.def_250 (= .T.Q (_ bv3 4)))) (let ((.def_255 (= .T.Q (_ bv2 4)))) (let ((.def_263 (or (= .T.Q (_ bv0 4)) (= .T.Q (_ bv1 4))))) (let ((.def_289 (= .T.Q (_ bv6 4)))) (let ((.def_294 (= .T.Q (_ bv5 4)))) (= .T.Q$next (ite (or (and (and (= .State (_ bv1 3)) (not (or (= .State (_ bv2 3)) (= .State (_ bv3 3))))) (not .def_207)) (and .def_207 (or (not .def_205) (and .def_43 .def_205)))) (_ bv9 4) (ite (or .def_263 (or .def_255 (or (= .T.Q (_ bv4 4)) .def_250))) (ite .def_263 (_ bv0 4) (ite .def_255 (_ bv1 4) (ite .def_250 (_ bv2 4) (_ bv3 4)))) (ite (or .def_294 (or (= .T.Q (_ bv7 4)) .def_289)) (ite .def_294 (_ bv4 4) (ite .def_289 (_ bv5 4) (_ bv6 4))) (ite (= .T.Q (_ bv8 4)) (_ bv7 4) (ite (= .T.Q (_ bv9 4)) (_ bv8 4) (_ bv9 4)))))))))))))))
)
)

; transition relation
(define-fun .trans () Bool (! 
(and 
	.T
)
 :trans true))

; property expression
(define-fun .prop () Bool 
; size 1
(and
	(let ((.def_33 (= .State (_ bv5 3)))) (let ((.def_43 (= .State (_ bv7 3)))) (let ((.def_205 (or (= .State (_ bv6 3)) .def_43))) (let ((.def_207 (or .def_205 (or .def_33 (= .State (_ bv4 3)))))) (let ((.def_224 (= .State (_ bv3 3)))) (let ((.def_225 (or (= .State (_ bv2 3)) .def_224))) (let ((.def_346 (= (ite .def_207 (ite .def_205 (ite .def_43 (_ bv17 7) (_ bv16 7)) (_ bv47 7)) (_ bv47 7)) (_ bv16 7)))) (let ((.def_364 (= (ite .def_207 (ite .def_205 (_ bv47 7) (ite .def_33 (_ bv47 7) (_ bv17 7))) (ite .def_225 (_ bv47 7) (ite (= .State (_ bv1 3)) (_ bv17 7) (_ bv16 7)))) (_ bv16 7)))) (let ((.def_388 (= (ite .def_207 (ite .def_205 (ite .def_43 (_ bv47 7) (_ bv16 7)) (ite .def_33 (_ bv17 7) (_ bv47 7))) (ite .def_225 (ite .def_224 (_ bv17 7) (_ bv16 7)) (_ bv47 7))) (_ bv16 7)))) (not (or (or (and .def_346 .def_364) (and .def_346 .def_388)) (and .def_364 .def_388))))))))))))
)
)

; property next expression
(define-fun .prop_next () Bool 
; size 1
(and
	(let ((.def_415 (= .State$next (_ bv5 3)))) (let ((.def_423 (= .State$next (_ bv7 3)))) (let ((.def_424 (or (= .State$next (_ bv6 3)) .def_423))) (let ((.def_426 (or .def_424 (or (= .State$next (_ bv4 3)) .def_415)))) (let ((.def_434 (= (ite .def_426 (ite .def_424 (ite .def_423 (_ bv17 7) (_ bv16 7)) (_ bv47 7)) (_ bv47 7)) (_ bv16 7)))) (let ((.def_454 (= .State$next (_ bv3 3)))) (let ((.def_455 (or (= .State$next (_ bv2 3)) .def_454))) (let ((.def_464 (= (ite .def_426 (ite .def_424 (_ bv47 7) (ite .def_415 (_ bv47 7) (_ bv17 7))) (ite .def_455 (_ bv47 7) (ite (= .State$next (_ bv1 3)) (_ bv17 7) (_ bv16 7)))) (_ bv16 7)))) (let ((.def_488 (= (ite .def_426 (ite .def_424 (ite .def_423 (_ bv47 7) (_ bv16 7)) (ite .def_415 (_ bv17 7) (_ bv47 7))) (ite .def_455 (ite .def_454 (_ bv17 7) (_ bv16 7)) (_ bv47 7))) (_ bv16 7)))) (not (or (or (and .def_434 .def_464) (and .def_434 .def_488)) (and .def_464 .def_488))))))))))))
)
)

; property
(define-fun property () Bool (! 
	.prop
 :invar-property 0))

; property next
(define-fun property$next () Bool
	.prop_next
)
