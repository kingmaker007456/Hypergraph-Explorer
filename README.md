📚 Hypergraph Data Modeling and VisualizationThis repository contains Python code for modeling hypergraph data and corresponding HTML files for visualizing these structures using D3.js and Vis.js.

A hypergraph generalizes the concept of a standard graph: while a regular graph edge connects exactly two nodes, a **hyperedge** can connect any arbitrary number of nodes.

---

###1. Data Model (`hypergraph_data_model.py`)The Python file implements a core `HyperGraph` class to handle the fundamental structure and basic analysis of hypergraph data.

####Key Features:* **`HyperGraph` Class**: Initializes and manages the set of unique `nodes` and a list of `hyperedges` (represented as sets of nodes).
* **`add_node(node_id)`**: Adds a single node to the graph.
* **`add_hyperedge(node_ids)`**: Adds a new relationship (hyperedge) connecting a list of nodes.
* **`get_node_degree(node_id)`**: Calculates the **degree** of a node, defined as the total number of hyperedges the node belongs to.
* **`get_hyperedge_size(hyperedge_index)`**: Calculates the **size** of a hyperedge, defined as the number of nodes connected by that hyperedge.

####Example Data Structure:The included example defines nodes A, B, C, D, E and three hyperedges:

* **H1**: \{A, B, C\}
* **H2**: \{B, D, E\}
* **H3**: \{C, E\}

Running the script provides analytical output:

```bash
$ python hypergraph_data_model.py
Total Nodes: {'E', 'D', 'C', 'A', 'B'}
Total Hyperedges: [{'A', 'B', 'C'}, {'E', 'B', 'D'}, {'E', 'C'}]
--- Analysis ---
Degree of Node 'B': 2 (Belongs to 2 hyperedges)
Size of Hyperedge H1 (Index 0): 3 nodes
Size of Hyperedge H3 (Index 2): 2 nodes

```

---

###2. Visualization (Bipartite Projection)Since traditional graph libraries do not inherently draw hyperedges as multi-way connections, these visualizations use the common **Bipartite Projection** method. This method introduces **proxy nodes** (the pink squares/circles) to represent each hyperedge, which are then connected to their member nodes (the blue circles).

####2.1. D3.js Visualization (`explorer_d3_visualization.html`)This file uses the D3.js library to create a force-directed layout:

* **Bipartite Layout**: Displays entity nodes (blue circles) and hyperedge proxy nodes (pink circles).
* **Interactive Highlighting**: Clicking on a pink **Hyperedge Proxy** node highlights all connected entity nodes (turning them orange) and their corresponding links, while fading out the rest of the network.
* **Status Message**: A dynamic message indicates which group is currently selected and the number of members it contains, enhancing user clarity.

####2.2. Vis.js Visualization (`explorer_visualization.html`)This file uses the Vis.js Network library to generate a force-directed layout quickly:

* **Bipartite Layout**: Nodes are separated into two groups using colors and shapes:
* **Entities**: Light Blue dots.
* **Hyperedges**: Light Pink boxes.


* **Physics Simulation**: Uses built-in physics to arrange the network, making it suitable for exploring larger datasets.

###How to Run the Visualizations1. **Visualization Files**: Open `explorer_d3_visualization.html` or `explorer_visualization.html` directly in any modern web browser.
2. **Data Model File**: Run `python hypergraph_data_model.py` from your terminal to see the analysis output.