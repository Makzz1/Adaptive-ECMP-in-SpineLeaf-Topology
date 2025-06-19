<h1 align="center">🌀 Adaptive ECMP Simulation — Spine‑Leaf Topology</h1>

<p align="center">
  <b>EX18 : Mini‑Project · Dynamic Load‑Based Routing</b><br/>
  <i>A Python simulation of data‑center traffic that outsmarts traditional ECMP.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-brightgreen" />
  <img src="https://img.shields.io/badge/NetworkX-Graph%20Library-blue" />
  <img src="https://img.shields.io/badge/Matplotlib-Visualisation-orange" />
</p>

---

## 📑 Table of Contents

* [Project Motivation](#-project-motivation)
* [What is Spine–Leaf?](#-what-is-spine–leaf)
* [Flaws in Traditional ECMP](#-flaws-in-traditional-ecmp)
* [From Hardware to Algorithms](#-from-hardware-to-algorithms)

  * [➊ Add More Spines](#➊-add-more-spines)
  * [➋ 3‑Tier Spine–Leaf](#➋-3‑tier-spine–leaf)
  * [➌ Adaptive ECMP (Our Solution)](#➌-adaptive-ecmp-our-solution)
* [Architecture & Components](#-architecture--components)
* [Key Features](#-key-features)
* [Example Workflow](#-example-workflow)
* [Visualization](#-visualization)
* [Getting Started](#-getting-started)
* [Applications & Future Scope](#-applications--future-scope)
* [Why Our Approach Stands Out](#-why-our-approach-stands-out)
* [License](#-license)

---

## 🎯 Project Motivation

*Nokia* (and many others) rely on ECMP for load‑balancing in high‑throughput networks, yet its **static hashing** often causes uneven utilisation and congestion.
Our goal: **simulate a dynamic, load‑aware ECMP** that adapts in real time—no new hardware required.

---

## 🌳 What is Spine–Leaf?

A *two‑tier* data‑center fabric where every **leaf** (access) switch uplinks to every **spine** (core) switch, providing:

* **East‑west optimisation** (server‑to‑server traffic)
* **Predictable latency & bandwidth**
* **Horizontal scalability**

---

## ⚠️ Flaws in Traditional ECMP

| # | Issue                                  | Impact                               |
| - | -------------------------------------- | ------------------------------------ |
| 1 | Fixed flow‑hashing                     | Some paths run hot while others idle |
| 2 | Zero visibility into current link load | Congestion cannot be avoided         |
| 3 | Port‑count ceiling on spines           | Limits scale when adding leaves      |

---

## 🔍 From Hardware to Algorithms

### ➊ Add More Spines *(2‑Tier Expansion)*

> ✔️ More paths
> ❌ Expensive & still port‑bound

![2‑Tier Expansion](https://github.com/user-attachments/assets/03e5e137-c680-4cfb-a16b-3a46bf2587e7)

---

### ➋ 3‑Tier Spine–Leaf

> ✔️ Extra routing options
> ❌ Complex, high CapEx/Opex

![3‑Tier Topology](https://github.com/user-attachments/assets/bff9fd7d-4e2f-4b59-b361-18366723eb0d)

---

### ➌ Adaptive ECMP (Our Solution)

We **leave the iron alone** and upgrade the *algorithm*:

1. **Real‑time congestion sensing** per link
2. **Dynamic cost** = `1 + (occ / capacity)`
3. Modified **Dijkstra** chooses the *least‑loaded* path—*per packet*
4. Packets carry a **sequence number** → re‑ordered on arrival

---

## 🧩 Architecture & Components

| Entity      | Role                  | Notable Attributes                               |
| ----------- | --------------------- | ------------------------------------------------ |
| **Node**    | Switch (leaf / spine) | Stores neighbours, rebuilds messages             |
| **Link**    | Bi‑directional edge   | `bandwidth_occ`, `bandwidth_tot`, dynamic `cost` |
| **Packet**  | Data fragment         | `size`, `seq_num`, `payload`                     |
| **Network** | Controller            | Topology graph, adaptive Dijkstra, visualisation |

---

## ✨ Key Features

* ☑️ **Adaptive routing**—avoids hot links
* ☑️ **Packet‑level fragmentation & reassembly**
* ☑️ **Graph view** via NetworkX + Matplotlib
* ☑️ **Config‑free**: runs on any Spine–Leaf size
* ☑️ Pythonic, \~200 LOC

---

## 🛠️ Example Workflow

```text
1️⃣  Topology  : LeafA, LeafB, LeafC ⇄ SpineA, SpineB  
2️⃣  Message   : "hi how are you" → 4 packets  
3️⃣  Routing   : each packet picks least‑loaded path  
4️⃣  Receiver  : LeafB reorders by seq_num → original message  
```

> 🔍 *Watch congestion shift in real‑time in the console/logs.*

---

## 🖼️ Visualization

The simulation auto‑generates a PNG like:

![Network Graph](docs/topology_example.png)

> *Edges are labelled with live utilisation; greener = lighter load.*

---

## 🚀 Getting Started

```bash
# Clone
git clone https://github.com/your‑username/adaptive‑ecmp-sim.git
cd adaptive‑ecmp-sim

# (Optional) create virtualenv
python -m venv venv && source venv/bin/activate

# Install deps
pip install -r requirements.txt   # networkx matplotlib

# Run simulation
python main.py --topology sample_topo.yaml --message "hello spine‑leaf"
```

> **Tip:** tweak `sample_topo.yaml` to model any fabric size or link bandwidths.

---

## 🔭 Applications & Future Scope

* Test‑bed for **congestion‑control** research
* Benchmark **traffic engineering** heuristics
* Extend to **BGP‑ECMP** or **MPLS** scenarios
* Add **gRPC** hooks for live network telemetry

---

## 🌟 Why Our Approach Stands Out

Unlike most adaptive ECMP schemes that stick to *per‑flow* routing (to avoid out‑of‑order packets), we route **per packet** and handle resequencing at the edge—borrowing battle‑tested logic from TCP stacks.
Result: **higher link utilisation**, **flatter latency curves**, **zero hardware spend**.

---


<p align="center"><b>Made with 💙 by Maghizh & Team</b></p>
