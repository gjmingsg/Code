def solve(n,a,b)
	hs ={}
	t = n * a 
	hs[t]=0
	for i in (1..n)
		t = t-a+b
		hs[t]=0
	end
	ls = hs.keys.sort!
	s=""
	ls.each{|x| s = s + x.to_s + " "}
	puts s.strip
end

t = gets.to_i
for i in (1..t) do
	n = gets.to_i
	a = gets.to_i
	b = gets.to_i
	solve(n-1,a,b)
end

