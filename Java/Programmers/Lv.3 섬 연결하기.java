import java.util.*;

class Solution {
    int[] parent;
    
    public int find(int x){
        if (parent[x] == x){
            return x;
        }else{
            parent[x] = find(parent[x]);
            return parent[x];
        }
    }
    
    public void union(int a,int b){
        a = find(a);
        b = find(b);
        parent[a] = b;
    }
    
    public int solution(int n, int[][] costs) {
        parent = new int[n];
        for(int i = 0; i<n; i++){
            parent[i] = i;
        }
        Arrays.sort(costs, (int[] c1, int[] c2) -> c1[2]-c2[2]);
        
        int answer = 0;
        for (int i = 0; i<costs.length; i++){
            if (find(costs[i][0]) != find(costs[i][1])){
                union(costs[i][0],costs[i][1]);
                answer += costs[i][2];
            }
        }
        return answer;
    }
}