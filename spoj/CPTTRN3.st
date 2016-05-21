printLine :=[:row :col :index|
  	string:=String streamContents: [ :stream|
		stream nextPutAll: (String new:col*3+1 withAll:$*).
    ].
	Transcript show: string;cr.
 	string:=String streamContents: [ :stream|
		col timesRepeat:[stream nextPutAll:'*..'].
		stream nextPut:$*.
    ].
	Transcript show: string;cr.
	Transcript show: string;cr.
	row=index ifTrue:[
 		string:=String streamContents: [ :stream|
			stream nextPutAll: (String new:col*3+1 withAll:$*).
      ].
	  Transcript show: string;cr.
	].
].

solve:=[:row :col|
  1 to: row do:[:i|
     printLine value:row value:col  value:i.
	
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
