public class Fibonacci {
    /**
     * @param n: an integer
     * @return an integer f(n)
     */
    public int fibonacci(int n) {
        int f1 = 0;
	int f2 = 1;
	int f3 = f2;
	if(n ==1)
	    return f1;
	if(n==2)
	    return f2;
	for(int i=3;i<=n;i++){
	    f3=f2+f1;
	    f1=f2;
	    f2=f3;
	}
	return f2;
    }

    public static void main(String args[]){
	Fibonacci f = new Fibonacci();
	System.out.println(f.fibonacci(10));
	
    }
}
