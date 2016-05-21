squaresum := [ :a :b|
		(a to: b) inject: 0 into: [ :sum :each| sum+(each*each)]
		 ].

 [stdin atEnd] whileFalse:[
    st:=stdin nextLine.
    pos := st findFirst: [:d | d isSeparator  ].
    pos>0 ifTrue:[
    a:=(st copyFrom: 1 to: pos -1) asNumber.
    b:=(st copyFrom: pos+1 to: st size) asNumber.
    c:=    (squaresum value:a value:b).
	c printNl.
    ].

]
