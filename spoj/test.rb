while text = gets
  x = text.to_i
  if x==42
  break  
  end
  puts text
end


tmp = gets.split /\s/
x = tmp[0].to_i
y = tmp[1].to_i
puts x+y