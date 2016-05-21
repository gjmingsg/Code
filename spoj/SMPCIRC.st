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
	|t|
	t := (read value:1).
   
    t = nil ifFalse:[
		(t at: 1) timesRepeat:[
			|x1 y1 r1 x2 y2 r2 temp sub x|
			temp:= (read value:6).
			temp=nil ifFalse:[
				x1:= temp at:1.
				y1:= temp at:2.
				r1:= temp at:3.
				x2:= temp at:4.
				y2:= temp at:5.
				r2:= temp at:6.
	
				sub:= (((x1-x2)*(x1-x2)) + ((y1-y2)*(y1-y2))) sqrt asInteger.

				r1 < r2 ifTrue:[
					x := r2.
					r2 := r1.
					r1 := x.
				].
				((r2 + sub) = r1)  ifTrue:[
					Transcript show:'E';cr.
				].
				(r2 + sub) < r1 ifTrue:[
					Transcript show:'I';cr.
				].
				(r2 + sub) > r1 ifTrue:[
					Transcript show:'O';cr.
				].		
			].
		]. 		
	].
]
