class HyperGraph:
    """
    A simplified class to represent a Hypergraph.
    Hypergraphs are defined by a set of nodes (vertices) and a set of hyperedges.
    """
    def __init__(self):
        # Nodes: A simple set of unique identifiers (e.g., strings or integers)
        self.nodes = set()
        # Hyperedges: A list of sets, where each set contains the nodes 
        # connected by that specific hyperedge.
        self.hyperedges = []

    def add_node(self, node_id):
        """Adds a single node to the graph."""
        self.nodes.add(node_id)

    def add_hyperedge(self, node_ids):
        """
        Adds a hyperedge connecting a list/set of nodes.
        All nodes in the hyperedge must already exist in the graph (or be added).
        """
        # Ensure all nodes in the hyperedge are tracked by the graph
        for node in node_ids:
            self.add_node(node)
            
        # Add the hyperedge as a set for efficient lookup
        self.hyperedges.append(set(node_ids))
        # Return the index of the newly added hyperedge for reference
        return len(self.hyperedges) - 1

    def get_node_degree(self, node_id):
        """
        Calculates the degree of a node: the number of hyperedges it belongs to.
        """
        if node_id not in self.nodes:
            return 0
            
        degree = 0
        for h_edge in self.hyperedges:
            if node_id in h_edge:
                degree += 1
        return degree

    def get_hyperedge_size(self, hyperedge_index):
        """
        Calculates the size of a hyperedge: the number of nodes it connects.
        """
        if hyperedge_index < 0 or hyperedge_index >= len(self.hyperedges):
            return 0
        return len(self.hyperedges[hyperedge_index])

    def get_incidence_matrix(self):
        """
        Calculates and returns the incidence matrix for the hypergraph.
        
        The matrix M is |Nodes| x |Hyperedges|.
        M[i][j] = 1 if Node i is in Hyperedge j, and 0 otherwise.
        
        Returns: A dictionary containing:
            'matrix': list of lists (the matrix)
            'nodes': list of node IDs (row headers)
            'hyperedges': list of hyperedge indices (column headers)
        """
        # Get sorted list of nodes and hyperedge indices for consistent indexing
        node_list = sorted(list(self.nodes))
        
        # Initialize the matrix with zeros: |Nodes| rows x |Hyperedges| columns
        matrix = [[0] * len(self.hyperedges) for _ in node_list]
        
        # Populate the matrix
        for j, h_edge in enumerate(self.hyperedges):
            for i, node_id in enumerate(node_list):
                if node_id in h_edge:
                    matrix[i][j] = 1
                    
        return {
            'matrix': matrix,
            'nodes': node_list,
            'hyperedges': list(range(len(self.hyperedges)))
        }

    def get_2_section_graph(self):
        """
        Calculates the 2-section graph (primal graph) of the hypergraph.
        
        The 2-section graph is a simple graph where an edge (u, v) exists
        if nodes u and v belong to at least one common hyperedge.
        
        Returns: A list of link objects: [{source: u, target: v}, ...]
        """
        links = set()
        node_list = list(self.nodes)

        for h_edge in self.hyperedges:
            # Check all unique pairs within the hyperedge
            nodes_in_edge = list(h_edge)
            
            # Using itertools.combinations would be cleaner, but using nested loops
            # to avoid external dependency and keep it simple.
            for i in range(len(nodes_in_edge)):
                u = nodes_in_edge[i]
                for j in range(i + 1, len(nodes_in_edge)):
                    v = nodes_in_edge[j]
                    
                    # Ensure consistent order (e.g., sort the pair) to avoid duplicates like (A, B) and (B, A)
                    link = tuple(sorted((u, v)))
                    links.add(link)
                    
        # Convert the set of tuples back to the required list of dictionaries
        return [{'source': u, 'target': v} for u, v in links]

# --- Example Usage ---
if __name__ == "__main__":
    hg = HyperGraph()

    # 1. Define Nodes
    hg.add_node("A")
    hg.add_node("B")
    hg.add_node("C")
    hg.add_node("D")
    hg.add_node("E")

    # 2. Define Hyperedges (Relationships)
    # H0: A, B, C 
    h0_index = hg.add_hyperedge(["A", "B", "C"]) 
    # H1: B, D, E 
    h1_index = hg.add_hyperedge(["B", "D", "E"])
    # H2: C, E 
    h2_index = hg.add_hyperedge(["C", "E"]) 
    
    print(f"Total Nodes: {hg.nodes}")
    print(f"Total Hyperedges: {hg.hyperedges}")
    print("--- Analysis ---")

    # 3. Analysis Example 1: Node Degree
    print(f"Degree of Node 'B': {hg.get_node_degree('B')} (Belongs to H0, H1)")

    # 4. NEW Analysis Example: 2-Section Graph
    two_section_links = hg.get_2_section_graph()
    print("\n--- 2-Section Graph Links ---")
    for link in two_section_links:
        print(f"Edge: {link['source']} - {link['target']}")
    
    # Expected Edges:
    # From H0: A-B, A-C, B-C
    # From H1: B-D, B-E, D-E
    # From H2: C-E
    # Total unique edges: (A, B), (A, C), (B, C), (B, D), (B, E), (C, E), (D, E)
