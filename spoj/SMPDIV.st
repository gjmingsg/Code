|solve|
solve:=[:n :x :y|
	|t|
	t := (1 to: n-1) select: [ :each| (each \\ x = 0) & (each \\ y > 0)  ].
	t do: [ :each|
	    Transcript show: each asString.
	    Transcript show: ' '.
	].
	Transcript show:'';cr.
].
trim:=[:st|
	|left right|
	left := 1.
	right := st size.
	
	[ left <= right and: [ (st at: left) isSeparator] ]
		whileTrue: [ left := left + 1 ].
		
	[ left <= right and: [ (st at: right) isSeparator] ]
		whileTrue: [ right := right - 1 ].
	
	st copyFrom: left to: right.
].

[stdin atEnd] whileFalse:[
n := (trim value: stdin nextLine) asNumber.

  1 to: n do:[:i|
    st := stdin nextLine.

    st := trim value: st.

    pos := st findFirst: [:d | d isDigit not].

    

    a:=(st copyFrom: 1 to: pos - 1) asNumber.
    
    pos1 := st findLast: [:d | d isDigit not].
    b:=(st copyFrom: pos+1 to: pos1) asNumber.
    
    c:=(st copyFrom: pos1+1 to: st size) asNumber.
    

    solve value:a value:b value:c.
  ].
]
