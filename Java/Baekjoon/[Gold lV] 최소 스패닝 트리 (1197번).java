import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge>{
    int u, v, w;

    public Edge(int u, int v, int w){
        this.u = u;
        this.v = v;
        this.w = w;
    }

    @Override
    public int compareTo(Edge other){
        if (this.w != other.w){
            return Integer.compare(this.w, other.w);
        }
        else if (this.u != other.u){
            return Integer.compare(this.u, other.u);
        }
        else{
            return Integer.compare(this.v, other.v);
        }
    }
}

class Main{
    static int[] parent;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        
        parent = new int[v+1];
        for (int i = 0; i<v+1; i++){
            parent[i] = i;
        }

        ArrayList<Edge> edgeList = new ArrayList<>();
        for (int i = 0; i<e; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            edgeList.add(new Edge(a, b, c));
        }
        PriorityQueue<Edge> edges = new PriorityQueue<>(edgeList);
        int cost = 0;

        for (int i = 0; i<e; i++){
            Edge ed = edges.poll();

            if (find(ed.u) != find(ed.v)){
                union(ed.u, ed.v);
                cost += ed.w;
            }
            
        }
        System.out.println(cost); 
    }    
    static int find(int x){
        if (parent[x] == x){
            return x;
        }
        parent[x] = find(parent[x]);
        return parent[x];
    }
    
    static void union(int a, int b){
        a = find(a);
        b = find(b);

        if (a == b){
            return;
        }
        parent[a] = b;
    }
}