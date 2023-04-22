import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main{
    static int[] parent;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        parent = new int[n+1];
        for (int i = 0; i<n+1; i++){
            parent[i] = i;
        }
        for (int i = 0; i<m; i++){
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int o = Integer.parseInt(st2.nextToken());
            int a = Integer.parseInt(st2.nextToken());
            int b = Integer.parseInt(st2.nextToken());
            if (o == 0){
                union(a, b);
            }
            else{
                if(find(a) == find(b)){
                    System.out.println("YES");
                }else{
                    System.out.println("NO");
                }
            }
        }
        br.close();
    }
    public static int find(int x){
        if (parent[x] == x){
            return x;
        }
        parent[x] = find(parent[x]);
        return parent[x];
    }
    public static void union(int a, int b){
        a = find(a);
        b = find(b);
        if (a == b){
            return;
        }
        parent[a] = b;
    }
}