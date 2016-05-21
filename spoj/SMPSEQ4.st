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
  st := stdin nextLine.
  st=nil ifFalse:[
	  st := trim value: st.
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
	]ifTrue:[
		nil.
	]	
].


[stdin atEnd] whileFalse:[	
	|n m s q ans x y|
	x := (read value:1).
   
    x = nil ifFalse:[
		n := (x at: 1).
		s := read value: n.
		
	].

	y := (read value:1).
	y = nil ifFalse:[
		m := (y at: 1).
		q := read value: m.
		
	].
	(s = nil) not ifTrue:[
		ans := (s select:[:item| (q count:[:inner| inner=item])>0]).
		ans do: [:t| 
			Transcript show:t asString.
			Transcript show:' '.
		].
		Transcript show:'';cr.
	]
]
