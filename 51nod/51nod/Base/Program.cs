using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Base
{
    class Program
    {

        static void Main(string[] args)
        {
            string a = Console.ReadLine();
            int T = Convert.ToInt32(a);
            while(T-->0){
                var c = Cricle.Create();
                var t = Triangle.Create();
                Console.WriteLine(IsCross(c, t));
            }
            
        }
        static bool IsTouch(Cricle c, int x1,int y1,int x2,int y2)
        {
            var LL = SquareDis(x1, y1, x2, y2);
            var rr = c.R * c.R;
            var K = SquareDis(c.xc, c.yc, x2, y2) + SquareDis(x1, y1,c.xc, c.yc) - 2 * rr;
            if (2 * K - LL < 0 || K > LL)
            {
                return false;
            }
            else {
                return true;
            }
        }
        static string IsCross(Cricle c,Triangle t) {
            var d1 = SquareDis(c.xc, c.yc, t.GetPointX(0), t.GetPointY(0));
            var d2 = SquareDis(c.xc, c.yc, t.GetPointX(1), t.GetPointY(1));
            var d3 = SquareDis(c.xc, c.yc, t.GetPointX(2), t.GetPointY(2));
            var RSquare = c.R * c.R;
            if ((d1 < RSquare && d2 < RSquare && d3 < RSquare) )
            {
                return "NO";
            }
            else if ((d1 > RSquare && d2 > RSquare && d3 > RSquare))
            {
                if (IsTouch(c, t.GetPointX(0), t.GetPointY(0), t.GetPointX(1), t.GetPointY(1))||
                    IsTouch(c, t.GetPointX(0), t.GetPointY(0), t.GetPointX(2), t.GetPointY(2))||
                    IsTouch(c, t.GetPointX(2), t.GetPointY(2), t.GetPointX(1), t.GetPointY(1)))
                    return "YES";
                return "NO";
            }
            else {
                return "YES";
            }
        }
        static long SquareDis(int x1,int y1,int x2, int y2) {
            return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);
        }
    }
    class Cricle {
        public int xc { get; set; }
        public int yc { get; set; }
        public int R { get; set; }
        public static Cricle Create()
        {
            string s = Console.ReadLine();
            return new Cricle() { xc = Convert.ToInt32(s.Split(' ')[0]), yc = Convert.ToInt32(s.Split(' ')[1]), R = Convert.ToInt32(s.Split(' ')[2]) };
        }
    }

    class Triangle
    {
        public Triangle() {
            Point = new List<Dictionary<string, int>>();
        }
        public List<Dictionary<string,int>> Point { get; set; }
        public int GetPointX(int i) {
            return Point[i]["x"];
        }
        public int GetPointY(int i)
        {
            return Point[i]["y"];
        }
        public void SetPoint(int x, int y) {
            Point.Add(new Dictionary<string, int>() { { "x", x }, { "y", y } });
        }
        public static Triangle Create()
        {
            var t = new Triangle();
            for (int i = 0; i < 3; i++) {
                string s = Console.ReadLine();
                t.SetPoint(Convert.ToInt32(s.Split(' ')[0]), Convert.ToInt32(s.Split(' ')[1]));
            }
            return t;
        }
    }
    
}
