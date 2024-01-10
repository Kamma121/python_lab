import queue
import sys


def dijkstra(graph, source):
    """
        Funkcja wykonuje algorytm Dijkstry na ważonym grafie skierowanym
        w celu znalezienia najkrótszych ścieżek z wierzchołka źródłowego
        do wszystkich innych wierzchołków w grafie.

        Parametry:
        - graph (Graph):Skierowany graf ważony reprezentowany jako
                        lista sąsiedztwa.
        - source (int): Wierzchołek źródłowy, dla którego obliczane
                        są najkrótsze ścieżki.

        Zwraca:
        - list: Lista odległości od wierzchołka źródłowego do
                wszystkich innych wierzchołków w grafie.
        """
    # Sprawdzenie, czy wierzchołek źródłowy jest poprwany
    if source >= graph.vertices or source < 0:
        raise ValueError("Invalid source vertex. Must be within the range [0, {}]".format(graph.vertices - 1))

    # Inicjalizacja tablic odległości i odwiedzonych wierzchołków
    distances = [sys.maxsize] * graph.vertices
    visited = [False] * graph.vertices
    parents = [-1] * graph.vertices

    # Inicjalizacja kolejki i umieszczenie w niej wierzchołka źródłowego
    distances[source] = 0
    q = queue.Queue()
    q.put(source)

    while not q.empty():
        # Zdjęcie wierzchołka z kolejki
        current_node = q.get()

        # Przetwarzanie bieżącego wierzchołka tylko, jeśli nie został jeszcze odwiedzony
        if not visited[current_node]:
            visited[current_node] = True

            # Sprawdzenie sąsiednich wierzchołków
            for neighbor, weight in graph.graph[current_node]:
                distance = distances[current_node] + weight
                if distance < distances[neighbor]:
                    # Aktualizacja odległości i dodanie sąsiada kolejki
                    distances[neighbor] = distance
                    parents[neighbor] = current_node
                    q.put(neighbor)

    return distances, parents


def print_dijkstra_results(graph, source):
    """
    Wyświetla wyniki algorytmu Dijkstry.

    Parametry:
    - graph (Graph):Skierowany graf ważony reprezentowany jako
                    lista sąsiedztwa.
    - source (int): Wierzchołek źródłowy, dla którego obliczane
                    są najkrótsze ścieżki.
    """
    distances, parents = dijkstra(graph, source)
    print("Wybrany wierzchołek źródłowy: ", source)
    print("Wierzchołek:\tOdległość od źródła:")
    for vertex, distance in enumerate(distances):
        print(f"{vertex}\t\t\t{distance}")
