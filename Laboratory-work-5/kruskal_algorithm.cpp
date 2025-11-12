#include <iostream>
#include <vector>
#include <algorithm>
#include <utility> // Для make_pair та pair

using namespace std;

#define edge pair<int,int>

class Graph {
private:
    // G: Вектор пар (Вага, Ребро(u, v))
    vector<pair<int, edge>> G; 
    // T: Вектор пар для Мінімального Остового Дерева (MST)
    vector<pair<int, edge>> T; 
    int *parent; // Масив для структури Disjoint Set Union (DSU)
    int V; // Кількість вершин
public:
    Graph(int V);
    void AddWeightedEdge(int u, int v, int w);
    int find_set(int i);
    void union_set(int u, int v);
    void kruskal();
    void print();
};

// --- Ініціалізація ---
Graph::Graph(int V) {
    this->V = V;
    parent = new int[V];
    // Кожна вершина спочатку є коренем свого власного набору
    for (int i = 0; i < V; i++)
        parent[i] = i;
    G.clear();
    T.clear();
}

// --- Додавання ребра ---
void Graph::AddWeightedEdge(int u, int v, int w) {
    // Зберігаємо ребро у форматі: (вага, (вершина_u, вершина_v))
    G.push_back(make_pair(w, edge(u, v)));
}

// --- Операція Find (Пошук кореня) ---
int Graph::find_set(int i) {
    // Якщо i є батьком самого себе, то це корінь набору
    if (i == parent[i])
        return i;
    else
        // Стискання шляху (Path Compression) для ефективності
        return parent[i] = find_set(parent[i]); 
}

// --- Операція Union (Об'єднання наборів) ---
void Graph::union_set(int u, int v) {
    // Просте об'єднання за коренями
    u = find_set(u);
    v = find_set(v);
    parent[u] = v;
}

// --- Алгоритм Крускала ---
void Graph::kruskal() {
    int uRep, vRep;
    // 1. Сортуємо всі ребра за зростанням ваги
    sort(G.begin(), G.end()); 
    
    // 2. Перебираємо відсортовані ребра
    for (size_t i = 0; i < G.size(); i++) {
        // Знаходимо корінь (представника набору) для обох вершин ребра
        uRep = find_set(G[i].second.first);
        vRep = find_set(G[i].second.second);

        // 3. Якщо корені різні, ребро НЕ утворює цикл
        if (uRep != vRep) {
            T.push_back(G[i]); // Додаємо ребро до MST
            union_set(uRep, vRep); // Об'єднуємо набори вершин
        }
    }
}

// --- Виведення результату ---
void Graph::print() {
    long long total_weight = 0;
    cout << "Edge (V-V) : Weight" << endl;
    for (size_t i = 0; i < T.size(); i++) {
        int u = T[i].second.first;
        int v = T[i].second.second;
        int w = T[i].first;

        cout << u + 1 << " - " << v + 1 << " : " << w << endl; // +1 при виведенні щоб співпадало з графом
        total_weight += w;
    }
    cout << "Total MST weight: " << total_weight << endl;
}

// --- Головна функція ---
int main() {
    Graph g(8); 

    // Додаємо лише одне ребро для кожної пари (U, V), оскільки граф неорієнтований
    // (1-2) вага 1
    g.AddWeightedEdge(0, 1, 1);
    // (1-3) вага 6
    g.AddWeightedEdge(0, 2, 6);
    // (1-4) вага 2
    g.AddWeightedEdge(0, 3, 2);
    
    // (2-5) вага 9
    g.AddWeightedEdge(1, 4, 9);
    // (2-6) вага 5
    g.AddWeightedEdge(1, 5, 5);
    
    // (3-4) вага 4
    g.AddWeightedEdge(2, 3, 4);
    // (3-6) вага 8
    g.AddWeightedEdge(2, 5, 8);
    // (3-8) вага 9
    g.AddWeightedEdge(2, 7, 9);
    
    // (4-5) вага 1
    g.AddWeightedEdge(3, 4, 1);
    
    // (5-7) вага 6
    g.AddWeightedEdge(4, 6, 6);
    
    // (6-7) вага 2
    g.AddWeightedEdge(5, 6, 2);
    
    // (7-8) вага 4
    g.AddWeightedEdge(6, 7, 4);

    // Виконання алгоритму
    g.kruskal(); 
    
    // Виведення результату
    g.print();

    return 0;
}