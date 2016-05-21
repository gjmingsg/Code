printLine := [ :row :col :index|
		(index=1 | ((index>1) & (row=index))) ifTrue:[
			Transcript show: (String new: col withAll: $*).
		].

		(index>1) & (index<row) ifTrue:[
			1 to:col do:[:i|
				(i=1 | ((i=col) & (i>1))) ifTrue:[
					Transcript show: '*'.
				]ifFalse:[
					Transcript show: '.'.
				].

			].
		].
		Transcript show: '';cr.
	].

solve := [ :row :col| 
		1 to:row do:[:i|
			printLine value: row value: col value: i.
			Transcript show: '';cr.
		]
	].
		
[stdin atEnd] whileFalse:[
  n := stdin nextLine asNumber.
  1 to: n do:[:i|
    st:=stdin nextLine.
    pos := st findFirst: [:d | d isDigit not].
    a:=(st copyFrom: 1 to: pos -1) asNumber.
    b:=(st copyFrom: pos+1 to: st size) asNumber.
    solve value:a value:b.
  ].
]
