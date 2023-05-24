import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge>{
    int u; 
    int v;
    double w;

    public Edge(int u, int v, double w){
        this.u = u;
        this.v = v;
        this.w = w;
    }

    @Override
    public int compareTo(Edge other){
        if (this.w < other.w){
            return -1;
        }else if(this.w > other.w){
            return 1;
        }
        return 0;
    }
}
class xy{
    double x, y;
    public xy(double x, double y){
        this.x = x;
        this.y = y;
    }
}

class Main{
    static int[] parent;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        
        parent = new int[n+1];
        for (int i = 0; i<n+1; i++){
            parent[i] = i;
        }

        ArrayList<xy> a = new ArrayList<>();
        for (int i = 0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            double x = Double.parseDouble(st.nextToken());
            double y = Double.parseDouble(st.nextToken());
            a.add(new xy(x, y));
        }
        
        ArrayList<Edge> edgeList = new ArrayList<>();
        for (int i = 0; i<n; i++){
            for(int j = i+1; j<n; j++){
                edgeList.add(new Edge(i, j, Math.sqrt(Math.pow((a.get(i).x-a.get(j).x),2)+Math.pow((a.get(i).y-a.get(j).y),2))));
            }
        }
        PriorityQueue<Edge> edges = new PriorityQueue<>(edgeList);
        double cost = 0;

        for (int i = 0; i<edges.size(); i++){
            Edge ed = edges.poll();

            if (find(ed.u) != find(ed.v)){
                union(ed.u, ed.v);
                cost += ed.w;
            }
            
        }
        System.out.printf("%.2f", cost);
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
