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
			|r c s temp sub|
			temp:= (read value:3).
				temp=nil ifFalse:[
					r := temp at: 1.
					c := temp at: 2.
					s := temp at: 3.
					
				].
		]. 		
	].
]
