def  partition( ar) 
  p = ar.first
  small = []
  big = []
  i=1
  while i<ar.size do 
    x = ar[i]
    if x<p
      small << x
    else
      big << x
    end
    i+=1
  end
    ar=(small << p ).concat(big)
    puts ar.join(" ")
    
end
cnt = gets.to_i;
ar = STDIN.gets.chomp.split(" ").map! {|i| i.to_i};
partition(ar);
