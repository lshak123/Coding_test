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
    static int[] distance;
    static ArrayList<ArrayList<Edge>> graph;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        distance = new int[n+1];
        for (int i = 0; i<n+1; i++){
            distance[i] = 99999999;
        }

        graph = new ArrayList<>();
        for (int i = 0; i<n+1; i++){
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph.get(a).add(new Edge(a, b, w));
        }
        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        dijkstra(start);

        System.out.println(distance[end]-distance[start]); 
    }    
    public static void dijkstra(int start){
        PriorityQueue<Edge> q = new PriorityQueue<>();
        q.add(new Edge(start, start, 0));
        distance[start] = 0;

        while (!q.isEmpty()){
            Edge ed = q.poll();
            int dist = ed.w;
            int node = ed.v;

            if (dist>distance[node]){
                continue;
            }
            for (int i = 0; i<graph.get(node).size() ;i++){
                int cost = dist + graph.get(node).get(i).w;
                if (cost < distance[graph.get(node).get(i).v]){
                    distance[graph.get(node).get(i).v] = cost;
                    q.add(new Edge(graph.get(node).get(i).u,graph.get(node).get(i).v, cost));
                }
            }
        }
    }
}