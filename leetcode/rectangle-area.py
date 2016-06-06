class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        v1 = abs((C-A) * (D-B))
        v2 = abs((G-E) * (H-F))
       
        print v1,' ',v2,' ',v3
        if (A>=E and A<=G and B>=F and B<=H and C>=E and C<=G and D>=F and D<=H):
            return v2
        elif (A<E and E<G and B<F and F<D and A<G and G<C and B<H and H<D):
            return v1
        elif (C>E and C<G and B>F and B<H):
            return v1+v2 - abs((C-E) * (H-B))
        elif (A>E and A<G and B>F and B<H):
            return v1+v2 - abs((C-E) * (H-B))
        elif (C>E and C<G and D>F and D<H):
            return v1+v2 - abs((C-E) * (D-F))
        elif (A>E and A<G and D>F and D<H):
            return v1+v2 - abs((C-E) * (H-B))
        else:
            return v1 + v2


c = Solution()

print c.computeArea(-3,0,3,4,0,-1,9,2)

print c.computeArea(0,0,0,0,-1,-1,1,1)
print c.computeArea(-2,-2,2,2,-2,-2,2,2)

print c.computeArea(-2,-2,2,2,1,-3,3,-1)

print c.computeArea(-2,-2,2,2,1,1,3,3)
