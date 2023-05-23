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
        int INF = 99999999;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(br.readLine());

        distance = new int[V+1];
        for (int i = 0; i<V+1; i++){
            distance[i] = INF;
        }

        graph = new ArrayList<>();
        for (int i = 0; i<V+1; i++){
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i<E; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph.get(u).add(new Edge(u, v, w));
        }

        dijkstra(start);

        for (int i = 1; i<V+1; i++){
            if (distance[i] != INF){
                System.out.println(distance[i]);
            }else{
                System.out.println("INF");
            }
        }
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