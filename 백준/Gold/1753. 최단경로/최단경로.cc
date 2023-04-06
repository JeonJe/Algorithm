#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

vector<vector<pair<int, int>>> graph(200001);
vector<int> dist(200001, numeric_limits<int>::max());
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

void dijkstra(int start)
{
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
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int v, e, k;
    cin >> v >> e >> k;

    for (int i = 0; i < e; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back(make_pair(v, w));
    }

    dijkstra(k);

    for (int i = 1; i <= v; i++)
    {
        if (dist[i] == numeric_limits<int>::max())
        {
            cout << "INF" << endl;
        }
        else
        {
            cout << dist[i] << endl;
        }
    }

    return 0;
}