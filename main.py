import matplotlib.pyplot as plt
import networkx as nx
import heapq
import itertools

class Node:
    def __init__(self, name, role):
        self.name = name
        self.role = role  # spine or leaf
        self.links = []
        self.received_packets = []

    def connect_link(self, link):
        self.links.append(link)
        print(f"Link added to {self.name}")

    def receive_packet(self, packet):
        self.received_packets.append((packet.seq_num, packet.data))

    def reconstruct_message(self):
        self.received_packets.sort(key=lambda x: x[0])
        return " ".join(word for _, word in self.received_packets)

class Link:
    def __init__(self, name, node1, node2):
        self.name = name
        self.node1 = node1
        self.node2 = node2
        self.bandwidth_occ = 0
        self.bandwidth_tot = 10

    def use_link(self, packet):
        if self.bandwidth_occ + packet.size <= self.bandwidth_tot:
            self.bandwidth_occ += packet.size
            return True
        return False

    def get_load(self):
        return self.bandwidth_occ / self.bandwidth_tot

    def get_cost(self):
        return 1 + self.get_load()  # Base cost + dynamic load cost

class Packet:
    def __init__(self, size, seq_num=None, data=None):
        self.size = size
        self.seq_num = seq_num
        self.data = data

class Network:
    def __init__(self):
        self.nodes = {}
        self.links = []

    def add_node(self, name, role):
        node = Node(name, role)
        self.nodes[name] = node
        return node

    def add_link(self, name, node1_name, node2_name):
        node1 = self.nodes[node1_name]
        node2 = self.nodes[node2_name]
        link = Link(name, node1, node2)
        node1.connect_link(link)
        node2.connect_link(link)
        self.links.append(link)

    def find_path(self, src_name, dst_name):
        pq = []
        counter = itertools.count()
        heapq.heappush(pq, (0, next(counter), src_name, []))
        visited = set()

        while pq:
            cost_so_far, _, current, path = heapq.heappop(pq)

            if current in visited:
                continue
            visited.add(current)

            if current == dst_name:
                return path

            current_node = self.nodes[current]
            for link in current_node.links:
                next_node = link.node2.name if link.node1.name == current else link.node1.name
                if next_node not in visited:
                    total_cost = cost_so_far + link.get_cost()
                    heapq.heappush(pq, (total_cost, next(counter), next_node, path + [(link, next_node)]))

        return []

    def send_packet(self, src, dst, packet):
        path = self.find_path(src, dst)
        if not path:
            print(f"No path found from {src} to {dst}")
            return

        print(f"Packet {packet.seq_num} traveling from {src} to {dst} via:")
        for link, node in path:
            if link.use_link(packet):
                print(f"  {link.node1.name} <-> {link.node2.name} (Load: {link.bandwidth_occ}/{link.bandwidth_tot})")
            else:
                print(f"  Link {link.name} overloaded!")

        self.nodes[dst].receive_packet(packet)

    def visualize_topology(self):
        G = nx.Graph()
        for name, node in self.nodes.items():
            G.add_node(name, role=node.role)

        for link in self.links:
            G.add_edge(link.node1.name, link.node2.name, label=link.name)

        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12)
        edge_labels = {(u, v): G[u][v]['label'] for u, v in G.edges()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Network Topology")
        plt.show()

# Set up network
network = Network()

# Add nodes
network.add_node("LeafA", "leaf")
network.add_node("LeafB", "leaf")
network.add_node("LeafC", "leaf")
network.add_node("SpineA", "spine")
network.add_node("SpineB", "spine")

# Add links (bi-directional simulation)
network.add_link("L1", "LeafA", "SpineA")
network.add_link("L2", "LeafA", "SpineB")
network.add_link("L3", "SpineA", "LeafB")
network.add_link("L4", "SpineB", "LeafB")
network.add_link("L5", "SpineA", "LeafC")
network.add_link("L6", "SpineB", "LeafC")

# Simulate sending message split into packets
message = "hi how are you"
words = message.split()

for i, word in enumerate(words):
    packet = Packet(size=1, seq_num=i, data=word)
    network.send_packet("LeafA", "LeafB", packet)

# Reconstruct message at destination
reconstructed_message = network.nodes["LeafB"].reconstruct_message()
print(f"\n📥 Reconstructed message at LeafB: '{reconstructed_message}'")

# Visualize
topology = network.visualize_topology()
