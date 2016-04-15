t =gets.to_i
t.times{
    (a,b) = gets.split(" ").map{|x| x.to_i}
    count = 0
    at = Math.sqrt(a).ceil
    bt = Math.sqrt(b).floor
    count = bt - at + 1

#    for i in (at..bt) do
#        if (a..b).include? i*i
#            count += 1
#        end
#    end

    puts count
}
