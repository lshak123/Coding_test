class Solution {
    static int[] parent = new int[200];
	
    public int find(int x){
        if(x==parent[x]){
            return x;
        }
        else{
            parent[x] = find(parent[x]);
            return parent[x];
        }
    }
    
    public void union(int a,int b){
        a = find(a);
        b = find(b);
        parent[a] = b;
    }
    
    public int solution(int n, int[][] computers) {
        for (int i = 0; i<n; i++){
            parent[i] = i;
        }
        for (int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                if (computers[i][j] == 1){
                    if (find(i) != find(j)){
                        union(i,j);
                    }
                }
            }
        }
        int answer = 0;
        for (int i = 0; i<n; i++){
            if (parent[i] == i) answer++;
        }
        return answer;
        
    }
}