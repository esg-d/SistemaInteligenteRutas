import heapq

class SistemaRutas:
    def __init__(self):
        # Base de conocimiento: estaciones y distancias
        self.conexiones = {
            "A": {"B": 5, "C": 2},
            "B": {"D": 4, "E": 6},
            "C": {"B": 1, "D": 7},
            "D": {"F": 3},
            "E": {"F": 2},
            "F": {}
        }

    def mejor_ruta(self, origen, destino):
        """Encuentra la mejor ruta usando Dijkstra"""
        cola = [(0, origen, [])]
        visitados = set()

        while cola:
            (costo, nodo, ruta) = heapq.heappop(cola)
            if nodo in visitados:
                continue
            ruta = ruta + [nodo]
            visitados.add(nodo)

            if nodo == destino:
                return costo, ruta

            for vecino, peso in self.conexiones.get(nodo, {}).items():
                if vecino not in visitados:
                    heapq.heappush(cola, (costo + peso, vecino, ruta))
        return None

if __name__ == "__main__":
    sistema = SistemaRutas()

    # Ejemplo: encontrar la mejor ruta de A a F
    origen = "A"
    destino = "F"
    resultado = sistema.mejor_ruta(origen, destino)

    if resultado:
        costo, ruta = resultado
        print(f"Mejor ruta de {origen} a {destino}: {' -> '.join(ruta)}")
        print(f"Costo total: {costo}")
    else:
        print(f"No existe una ruta de {origen} a {destino}.")
