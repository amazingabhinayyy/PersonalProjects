import java.util.*;

public class KittenOnATree {

    public static void main(String[] args) {
        // TODO Auto-generated method stub

        Scanner s = new Scanner (System.in);
        int stuck = s.nextInt();
        s.nextLine();
        String current = s.nextLine();
        Map<Integer, Set<Integer>> adj = new HashMap<>();
        ArrayList<Integer> potRoots = new ArrayList<>();
        boolean cont = true;
        int exit = 0;
        
        while(current.charAt(0)!='-') {
        	String[] branch = current.split(" ");
        	Set<Integer> ad = new HashSet<>();
        	int key = Integer.parseInt(branch[0]);
        	
        	for(int i = 1; i<branch.length;i++) {
        		ad.add(Integer.parseInt(branch[i]));
        		adj.put(key, ad);
        		potRoots.add(key);
        	}
        	current = s.nextLine();
        }
        
       for(int i = 0; i<potRoots.size()&&cont; i++) {
    	   int curRoot = potRoots.remove(0);
    	   if(!adj.containsValue(curRoot)) {
    		   exit = curRoot;
    		   cont = false;
    	   }
    			   
       }
       
       List<Integer> path = depthFirstSearch(adj,stuck,exit);
       for(int i = 0; i<path.size();i++) {
    	   System.out.print(path.get(i));
    	   if(i<path.size()-1) {
    		   System.out.print(" ");
    	   }
       }
     
    }
    
    public static List<Integer> depthFirstSearch(Map<Integer,Set<Integer>> adjlist, int start, int end) {
    	
    	
    	
    	List<Integer> path = new ArrayList<>();
    	List<Integer> key = new ArrayList<>();
    	path.add(start);
    	boolean contains = true;
    	
    	
    	Set<Integer> n = adjlist.keySet();
    	int node = start;
    	
    	
    	Set<Integer> keys = adjlist.keySet();
    	while (node!=end) {
    		for(Integer s: keys) {
    			key.add(s);
    		}
    		for(int i =0; i<key.size();i++) {
    			Integer s = key.get(i);
    			Set<Integer> values = adjlist.remove(s);
    			if(values.contains(node)) {
    				path.add(s);
    				node = s;
    			}
    			adjlist.put(s, values);
    		}
    	}
    	
    	return path;
    
    }
}