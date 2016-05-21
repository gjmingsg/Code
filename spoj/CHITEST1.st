"your code goes here"
solve := [:a :b|
		a +b.
	].
	
 [stdin atEnd] whileFalse:[
  n := stdin nextLine asNumber.
  1 to: n do:[:i|
    st:=stdin nextLine.
    pos := st findFirst: [:d | d isSeparator  ].
    a:=(st copyFrom: 1 to: pos -1) asNumber.
    b:=(st copyFrom: pos+1 to: st size) asNumber.
    (solve value:a value:b) printNl.
  ].
]
