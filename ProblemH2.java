package CPC;

import java.util.*;
public class ProjectH
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        int cases = in.nextInt();
        int min = in.nextInt();
        int max = in.nextInt();
        int [] platforms = new int[cases];
        int length = 0;
        double maxlength = 0;
        boolean start = true;
        for(int x = 0; x<cases; x++)
        {
            platforms[x] = in.nextInt();
        }
        double [] sep = new double[cases];
        for(int x = 0; x<sep.length; x++)
        {
            sep[x] = minSep(platforms, max, min, x);
            if(sep[x]<0)
            {
                length = -1;
                maxlength = -1;
            }
        }
       
       
        if(length!=-1)
        {
            for(int x = 0; x<cases; x++)
            {
                double [] spaces = new double [cases];
                for(int y = 0; y<spaces.length; y++)
                {
                    spaces[y] = 0;
                }
               
                double len = length(x, platforms, sep, min, max, spaces);
                if(start)
                {
                    start = false;
                    maxlength = len;
                }
                else if(maxlength<len)
                {
                    maxlength = len;
                }
               
            }
        }
       
        System.out.print((int)maxlength);
           
       
       
    }
    public static double length(int pos, int [] platforms, double [] sep, int min, int max, double [] spaces )
    {
        double len = 0;
        double posSep = sep[pos];
        if(posSep >= (double)max/2)
        {
            len+=max;
            spaces[pos] = max/2;
        }
        else
        {
            len+=posSep*2;
            spaces[pos] = posSep;
        }
       
        for(int x = pos+1; x<sep.length;x++)
        {
            len+=nextSep(platforms, x, max, min, spaces);
        }
        for(int x = pos-1; x>=0; x--)
        {
            len+=prevSep(platforms, x, max, min, spaces);
        }
        return len;
       
    }
       
    public static double nextSep(int [] array, int pos, int max, int min, double [] spaces)
    {
        double ans = 0;
        if(pos<array.length-1)
        {
        	ans = (double)(array[pos+1])-(double)min/2-array[pos];
        }
        double other = 0;
        if(pos>0)
        {
        	other = (double)(array[pos])-(double)array[pos-1]-(double)spaces[pos-1];
        }
        
        
        if(other<ans&&pos!=0)
        {
            ans = other;
        }
        
        if(pos==array.length-1)
        {
        	ans = other;
        }
        
        if(ans>= (double)max/2)
        {
            ans = max;
            spaces[pos] = max/2;
        }
        else
        {
            spaces[pos] = ans;
            ans = ans*2;
        }
       
        return ans;
       
    }
   
    public static double prevSep(int [] array, int pos, int max, int min, double [] spaces)
    {
        double ans = 0;
        if(pos<array.length-1)
        {
        	ans = (double)(array[pos+1])-spaces[pos+1]-array[pos];
        }
        double other = 0;
        if(pos>0)
        {
        other = (double)(array[pos])-(double)array[pos-1]-(double)min/2;
        }
        if(other<ans&&pos!=0)
        {
            ans = other;
        }
        
        if(pos==array.length-1)
        {
        	ans = other;
        }
       
        if(ans>= (double)max/2)
        {
            ans = max;
            spaces[pos] = max/2;
        }
        else
        {
            spaces[pos] = ans;
            ans = ans*2;
        }
       
       
        return ans;
       
    }

   
   
   
   
   
   
    public static double minSep(int [] array, int max, int min, int pos)
    {
        double ans = 0;
        double other = 0;
        if(pos==0)
        {
            ans = (double)array[1]-(double)min/2 -array[0];
        }
        else if(pos ==array.length-1)
        {
            ans = (double)(array[array.length-1]) - (double)min/2-array[array.length-2];
        }
        else
        {
            ans = (double)(array[pos+1])-(double)min/2-array[pos];
            other = (double)(array[pos])-(double)min/2-array[pos-1];
            if(other<ans)
            {
                ans = other;
            }
        }
        return ans;
       
    }
       
       
       
       
   
}
