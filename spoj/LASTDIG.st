trim:=[:st|
	|l r|
	l:=1.
	r:=st size.
	[ l<=r and: [ (st at: l) isSeparator] ]
		whileTrue: [ l := l + 1 ].	
	[ l<=r and: [ (st at: r) isSeparator] ]
		whileTrue: [ r := r - 1 ].
	st copyFrom: l to: r.
].
read:= [:i|
  st := trim value: (stdin nextLine).
  (st size)=0 ifFalse:[
	  a:=ArrayedCollection new: i.
	  p:=1.
	  l:=1.
	  1 to: i do:[:index|
	   		[(p<st size) and: [(st at: p) isSeparator not]]
				whileTrue: [p:=p+1]. 
		  	a at: index put: (st copyFrom: l to:p) asNumber. p:=p+1. l:= p.].a] ifTrue:[nil]].
[stdin atEnd] whileFalse:[	
	x:=(read value:1).
	z:=#(#(1) #(2 4 8 6) #(3 9 7 1) #(4 6) #(5) #(6) #(7 9 3 1) #(8 4 2 6) #(9 1)).
    x=nil ifFalse:[(x at: 1) timesRepeat:[
|j a b t|
j:=read value:2. 
t:=(j at: 1) asString.a:=(t at: t size) asInteger-48.b:=(j at: 2) asNumber.0=a ifTrue:[0 printNl]ifFalse:[b=0 ifTrue:[1 printNl]ifFalse:[k := (z at: a) size.0=(b \\ k) ifTrue:[((z at: a) at:1) printNl]ifFalse:[((z at: a) at: (b \\ k)) printNl]]]]]]
