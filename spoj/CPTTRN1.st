printLine :=[:row :col|
  string:=String streamContents: [ :stream|
        1 to:col do: [:i|
          row odd ifTrue: [
            i odd ifTrue: [
              stream nextPut: $*.
            ]ifFalse:[
              stream nextPut: $..
            ]
          ] ifFalse:[
            i odd  ifTrue: [
              stream nextPut: $..
            ]ifFalse:[
              stream nextPut: $*.
            ]
          ]
        ]
      ].
].

solve:=[:row :col|
  1 to: row do:[:i|
    Transcript show: (printLine value:i value:col );cr.
    ]
].
                                                                                                                                                                           "
                                                                                                                                                                                solve value:3 value:1.
                                                                                                                                                                                Transcript show:''; cr.
                                                                                                                                                                                solve value:4 value:4.
                                                                                                                                                                                Transcript show:''; cr.
                                                                                                                                                                                solve value:2 value:5.
                                                                                                                                                                                Transcript show:''; cr.
                                                                                                                                                                                "
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
