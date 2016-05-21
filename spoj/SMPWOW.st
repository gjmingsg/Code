	|printLine n|
printLine :=[:x|
	Transcript show:'W'.
	x timesRepeat: [ Transcript show:'o' ].
	Transcript show:'w';cr.
	].
	"
	printLine value:7.
	printLine value:1.
	"
	[stdin atEnd] whileFalse:[
  	n := stdin nextLine asNumber.
	printLine value:n.
]
