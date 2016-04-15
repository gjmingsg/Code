=begin
a = '68932147586'
b = '468711654886'
puts a.to_i + b.to_i
=end
class P1005
	def cal(a,b)
		a.to_i() + b.to_i()
	end
end

cal = P1005.new
puts cal.cal(gets,gets)