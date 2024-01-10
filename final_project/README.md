# Algorytm Dijkstry - Dokumentacja

***1) Wprowadzenie***

Algorytm Dijkstry to efektywna metoda znajdowania najkrótszych ścieżek w grafie ważonym, skierowanym lub nieskierowanym.
Algorytm ten ma zastosowanie w różnych dziedzinach, takich jak sieci komunikacyjne czy trasowanie w systemach
informatycznych.

Algorytm Dijkstry opiera się na koncepcji relaksacji krawędzi, iteracyjnie aktualizując odległości od wierzchołka
źródłowego do pozostałych wierzchołków. Pozwala to znaleźć najkrótsze ścieżki w grafie.

***2)  Implementacja grafu***

Implementacja grafu w tym programie wykorzystuje strukturę skierowanego grafu ważonego w postaci listy sąsiedztwa.
Każdy wierzchołek grafu ma przypisaną listę sąsiednich wierzchołków wraz z wagami krawędzi.
Struktura ta umożliwia efektywne przetwarzanie grafów, szczególnie przy zastosowaniu algorytmów wyszukiwania ścieżek.

`Graph`:

Klasa Graph reprezentuje graf. Do jej głównych funkcji należą:

`add_edge(u, v, w)`: Dodaje krawędź od wierzchołka u do v o wadze w.

`remove_edge(u, v)`: Usuwa krawędź z wierzchołka u do v.

`get_adjacent_vertices(u)`: Zwraca listę wierzchołków sąsiadujących z wierzchołkiem u.

`display_graph()`: Wyświetla reprezentację grafu.

***3) Implementacja algorytmu***

**`dijkstra(graph,source)`**

Funkcja przyjmuje graf w postaci listy sąsiedztwa oraz wierzchołek źródłowy. Zwraca listę odległości od źródła do
każdego innego wierzchołka w grafie.

![image](https://github.com/Kamma121/python_lab/assets/109139766/72d543a8-34c3-45dc-808b-cbc462664874)

- Algorytm obsługuje błędy, takie jak nieprawidłowy wierzchołek źródłowy

```
if source >= graph.vertices or source < 0:
    raise ValueError("Invalid source vertex. Must be within the range [0, {}]".format(graph.vertices - 1))
``` 

- Algorytm korzysta z kolejki do implementacji przeszukania grafu wszerz (BFS)

```
distances[source] = 0
q = queue.Queue()
q.put(source)
    while not q.empty():
        current_node = q.get()
        if not visited[current_node]:
            visited[current_node] = True
            for neighbor, weight in graph.graph[current_node]:
                distance = distances[current_node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    q.put(neighbor)
```

***4) Podsumowanie i wyniki testów***

Algorytm Dijkstry został przetestowany pod kątem poprawności i wydajności. Poniżej znajdują się przykłady testów z
modułu `test_dijkstra` dla różnych przypadków, w tym dla przypadków brzegowych. Wszystkie testy zostały przeprwoadzone
dla poniższego grafu:

![image](https://github.com/Kamma121/python_lab/assets/109139766/4f75f8c5-e2e0-4d6a-a8b7-a4eec54f5eb4)

- *Testy znajdowania najkrótszych ścieżek dla kilku wierzchołków:*

```
def test_dijkstra_for_source_root_0(self):
    result = dijkstra(self.graph, 0)
    self.assertEqual(result[0], [0, 4, 12, 19, 27, 17, 13, 8, 14])

def test_dijkstra_for_source_root_1(self):
    result = dijkstra(self.graph, 1)
    self.assertEqual(result[0], [sys.maxsize, 0, 8, 15, 24, 14, 10, 5, 11])

def test_dijkstra_for_source_root_5(self):
    result = dijkstra(self.graph, 5)
    self.assertEqual(result[0], [sys.maxsize, sys.maxsize, sys.maxsize,
                                sys.maxsize, 10, 0, sys.maxsize,
                                sys.maxsize, sys.maxsize])
```                                  

- *Test dla grafu o jednym wierzchołku:*

```
def test_single_vertex_graph(self):
    graph = Graph(1)
    result = dijkstra(graph, 0)
    self.assertEqual(result[0], [0])
```

- *Testy dla nieprawidłowych wierzchołków:*

```
def test_invalid_source_vertex(self):
    with self.assertRaises(ValueError):
        dijkstra(self.graph, 9)

def test_invalid_source_vertex_negative(self):
    with self.assertRaises(ValueError):
        dijkstra(self.graph, -1)
```

- *Test dla wierzchołka bez krawędzi wychodzących:*

```
def test_dijkstra_for_unreachable_source_4(self):
    result = dijkstra(self.graph, 4)
    expected_result = [sys.maxsize] * 9
    expected_result[4] = 0
    self.assertEqual(result[0], expected_result)
```

***5) Źródła***

- [Wikipedia - Algorytm Dijkstry](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

- [Narzędzie do stworzenia wizualizacji grafu](https://visualgo.net/en/graphds)
