def solve(a,b)
	ia = 0
	ib = 0
	a.each_char{|x|ia = ia | (1<<(x.ord - 'a'.ord))}
	b.each_char{|x|ib = ib | (1<<(x.ord - 'a'.ord))}
	if (ia&ib)==0
		puts "NO"
	else
		puts "YES"
	end
end

t = gets.to_i
for i  in (1..t) do
	a = gets
	b = gets
	solve(a,b)
end
