#include <iostream>
#include <cstring>
using namespace std;

#define V 8 

#define INF 9999999

int G[V][V] = {
              {INF,   1,    6,    2,   INF,  INF,  INF,  INF},
              {  1,  INF,  INF,  INF,    9,    5,  INF,  INF},
              {  6,  INF,  INF,    4,  INF,    8,  INF,    9},
              {  2,  INF,    4,  INF,    1,  INF,  INF,  INF},
              {INF,    9,  INF,    1,  INF,  INF,    6,  INF},
              {INF,    5,    8,  INF,  INF,  INF,    2,  INF},
              {INF,  INF,  INF,  INF,    6,    2,  INF,    4},
              {INF,  INF,    9,  INF,  INF,  INF,    4,  INF}
};

int main() {
    int no_edge;
    int selected[V];
    // Обнулення масиву 'selected'
    memset(selected, false, sizeof(selected)); 
    no_edge = 0;

    // Починаємо з вершини 0
    selected[0] = true;
    int x, y;

    cout << "Edge : Weight" << endl;

    // Цикл триває V-1 разів (поки не знайдено V-1 ребер)
    while (no_edge < V - 1) {
        int min = INF;
        x = 0;
        y = 0;

        // Перевіряємо всі обрані вершини 'i'
        for (int i = 0; i < V; i++) {
            if (selected[i]) {
                // Перевіряємо всі необрані вершини 'j'
                for (int j = 0; j < V; j++) {
                    // Перевіряємо, чи G[i][j] менше за INF, 
                    // що означає, що ребро існує
                    if (!selected[j] && G[i][j] < INF) { 
                        if (min > G[i][j]) {
                            min = G[i][j];
                            x = i;
                            y = j;
                        }
                    }
                }
            }
        }

        cout << x+1 << " - " << y+1 << " : " << G[x][y] << endl; // +1 до вершин x і y, щоб було виведення як на графі
        // Додаємо знайдену вершину 'y' до MST
        selected[y] = true;
        no_edge++;
    }

    return 0;
}