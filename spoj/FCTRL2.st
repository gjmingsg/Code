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

read:= [:i|
  st := trim value: (stdin nextLine).
  (st size)=0 ifFalse:[
	  a  := ArrayedCollection new: i.
	  pos := 1.
	  last :=1.
	  
	  1 to: i do:[:index|
	   		[(pos < st size) and: [(st at: pos) isSeparator not]]
				whileTrue: [ pos := pos + 1 ]. 
		  	a at: index put: (st copyFrom: last to: pos) asNumber.	 
			
			pos := pos + 1.
			last := pos.
	  ].
	  a.
  ] ifTrue:[
	nil.
	].	
].

[stdin atEnd] whileFalse:[	
	x := (read value:1).
   
    x = nil ifFalse:[
		(x at: 1) timesRepeat:[
			|temp|
			temp := read value: 1.
			((temp at: 1) asNumber factorial) printNl.
		]
	].
]
