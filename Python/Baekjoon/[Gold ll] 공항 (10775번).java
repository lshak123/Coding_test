import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main{
    static int[] parent;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int p = Integer.parseInt(br.readLine());
        int count = 0;
        parent = new int[n+1];
        for (int i = 0; i<n+1; i++){
            parent[i] = i;
        }
        for(int i = 0; i<p; i++){
            int plane = Integer.parseInt(br.readLine());
            if(parent[find(plane)] == 0){
                break;
            }
            parent[find(plane)] = find(plane)-1;
            count++;
        }
        System.out.println(count);
    }
    public static int find(int x){
        if (parent[x] == x){
            return x;
        }
        parent[x] = find(parent[x]);
        return parent[x];
    }
}