#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

void dijkstra(int start, int v, vector<vector<pair<int, int>>> &graph, vector<int> &dist)
{
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    dist[start] = 0;
    pq.push(make_pair(dist[start], start));

    while (!pq.empty())
    {
        pair<int, int> cur = pq.top();
        pq.pop();
        int cur_weight = cur.first;
        int cur_v = cur.second;

        if (cur_weight < dist[cur_v])
        {
            continue;
        }

        for (auto adj : graph[cur_v])
        {
            int adj_v = adj.first;
            int adj_weight = adj.second;

            int new_cost = cur_weight + adj_weight;
            if (new_cost < dist[adj_v])
            {
                dist[adj_v] = new_cost;
                pq.push(make_pair(new_cost, adj_v));
            }
        }
    }
}

int main()
{
    int v, e, k;
    scanf("%d %d %d", &v, &e, &k);

    vector<vector<pair<int, int>>> graph(v + 1);
    vector<int> dist(v + 1, numeric_limits<int>::max());


    for (int i = 0; i < e; i++)
    {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        graph[u].push_back(make_pair(v, w));
    }

    dijkstra(k, v, graph, dist);

    for (int i = 1; i <= v; i++)
    {
        if (dist[i] == numeric_limits<int>::max())
        {
            printf("INF\n");
        }
        else
        {
            printf("%d\n", dist[i]);
        }
    }

    return 0;
}