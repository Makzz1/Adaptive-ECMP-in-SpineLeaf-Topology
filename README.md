**EX18 : Mini Project
Adaptive ECMP Simulation with Dynamic Load-Based Routing
Spine–Leaf Topology**

**Project Description**
This project focuses on addressing key flaws in the traditional Spine–Leaf topology used in data center networks. While the Spine–Leaf architecture is known for its scalability and redundancy, it still faces challenges related to congestion, scalability limitations due to fixed port counts, and inefficiencies in Equal-Cost Multi-Path (ECMP) routing. Our aim is to simulate a more adaptive and efficient solution that mitigates these issues through dynamic load-aware routing.

**What is Spine–Leaf Topology?**
A Spine–Leaf topology is a two-tier network architecture widely used in data centers. It consists of:
- Leaf nodes (Access Layer): Connect directly to end devices such as servers.
- Spine nodes (Core Layer): Connect all leaf switches together.
Every leaf is connected to every spine, ensuring high bandwidth, low latency, and minimal bottlenecks. This structure supports horizontal scalability and efficient east–west traffic flow.

**Why We Chose This Topic**
We selected this project because Nokia systems often implement ECMP in their data center and backbone networks. Since ECMP is widely adopted for load balancing in such environments, understanding its limitations and improving it felt highly relevant. Our work specifically targets one of ECMP’s main drawbacks—static path selection—by proposing an adaptive and dynamic routing strategy that better reflects real-world network conditions.

**Flaws in Traditional ECMP**
- Uses fixed hashing, which may overload certain paths.
- Ignores real-time link utilization, leading to imbalanced traffic.
- Does not scale well when adding more leaf nodes.
  
**Exploration of Solutions**
1. Adding More Spines (2-Tier Expansion)
Our first approach involved adding extra spines to increase available paths and improve load balancing. However:
- It did not significantly improve scalability, since spine ports still became a bottleneck.
- It was not cost-effective, due to the high cost of additional spine hardware.

![image](https://github.com/user-attachments/assets/03e5e137-c680-4cfb-a16b-3a46bf2587e7)

2. Creating a 3-Tier Spine–Leaf Topology
We introduced a third vertical layer of spines. This architecture provided:
- More routing options, reducing congestion.
- Improved scalability, enabling more leaf nodes via expanded spine ports.

  ![image](https://github.com/user-attachments/assets/bff9fd7d-4e2f-4b59-b361-18366723eb0d)


However, this came with:
- Higher complexity in configuration and maintenance.
- Greater cost, as even a single spine is expensive—multiplying them made it impractical.

3. Final Solution: Adaptive ECMP Algorithm
Acknowledging the limitations of hardware-based solutions, we shifted focus to the routing algorithm itself. Traditional ECMP assigns paths without awareness of current network load.

We developed an Adaptive ECMP system that:
- Evaluates real-time link congestion.
- Selects the least loaded path dynamically for each packet.
- Requires no hardware upgrades and fits existing topologies.

We also incorporated:
- Packet fragmentation with sequence numbers.
- Reordering at the destination to reconstruct the original message.

This adaptive approach offers a scalable, efficient, and cost-effective solution for modern networks.
Final Solution Components
Node
- Represents a switch (spine or leaf).
- Maintains connected links.
- Reconstructs messages from received packets using sequence numbers.
Link
- Bi-directional connection between two nodes.
- Has:
  - bandwidth_occ: Current usage.
  - bandwidth_tot: Total capacity.
- Computes cost dynamically: cost = 1 + (bandwidth_occ / bandwidth_tot)
Packet
- Contains:
  - size: Packet size.
  - seq_num: Sequence number.
  - data: Payload.
Network
- Manages nodes and links.
- Uses a Dijkstra-like algorithm with dynamic link costs.
- Sends packets over least loaded paths.
- Provides topology visualization using NetworkX.

Key Features
- Adaptive Routing: Selects the optimal path based on link load.
- Message Reconstruction: Rebuilds messages using sequence numbers.
- Graph Visualization: Displays nodes and links using NetworkX.
  
Example Workflow
1. Topology Setup
   - Nodes: LeafA, LeafB, LeafC, SpineA, SpineB
   - Links: L1 to L6 (bi-directional)
2. Packet Transmission
   - Input: "hi how are you"
   - Split into packets: ["hi", "how", "are", "you"]
   - Each packet is routed from LeafA to LeafB based on current load.
3. Reconstruction
   - LeafB receives the packets.
   - Reorders them by seq_num.
   - Final message: "hi how are you"
4. Visualization
   - Network structure is rendered graphically using Matplotlib and NetworkX.
     
Tools Used 
- Python – for simulation logic
- NetworkX and Matplotlib – for visualization 

Applications and Future Scope

This simulation provides a testbed for experimenting with load balancing, congestion control, and dynamic routing techniques. It lays the groundwork for advanced research into data center architectures and real-world deployment strategies in ECMP-based networks.

Why Our Approach Stands Out

Adaptive ECMP methods are already used in real-world networks to improve routing decisions. However, a major limitation in existing implementations is that all packets belonging to a single data flow are typically sent through the same path. This is done to avoid packet reordering at the receiver. Our solution breaks away from this convention by allowing each packet to take the least congested path individually—even if they belong to the same message. While this raises concerns of packet reordering, we leverage well-established principles from packet-switched networks where reordering is routinely handled at the receiver. By combining dynamic load-based routing with packet-level reordering, our method maximizes bandwidth utilization, reduces congestion, and introduces a novel way to handle ECMP limitations.

