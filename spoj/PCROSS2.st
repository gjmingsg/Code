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
	  		|temp n m ci cj j1 j2| 			"must set local var,or m will set to 1"
			temp := read value: 4.
			 
			m:= (temp at: 1).
			n:= (temp at: 2).
			ci:= (temp at: 3).
			cj:= (temp at: 4).
			"must set local var,or m will set to 1"
			t := ArrayedCollection new:m withAll: (String new:n withAll: $.).
			j1:=cj. 
			j2:=cj.

			ci to: 1 by: -1 do: [:i|
				|x|
				x := String new:n withAll: $..
	            j1>0 ifTrue: [
					x at: j1 put: $*.
				].

				j2<=n ifTrue:[
					x at: j2 put: $*.
				].
				t at: i put: x.
                j1 := j1 - 1.
				j2 := j2 + 1.
			].		
	
			j1:=cj. 
			j2:=cj.
			ci to: m do: [:i|
				|x|
				x := String new:n withAll: $..
	            j1<=n ifTrue:[
					x at: j1 put: $*.
				].
				j2>0 ifTrue:[
					x at: j2 put: $*.
				].
				t at: i put: x.
                j1 := j1 + 1.
				j2 := j2 - 1.
			].			
			

			t do:[:item| Transcript show:item asString;cr.].
			Transcript show:'' ;cr.
		].
    ]
].



	
