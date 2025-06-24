#!/usr/bin/env python3

from mininet.topo import Topo

class SpineLeaf(Topo):
    def build(self):
        # Spine switches
        spine1 = self.addSwitch("s1", dpid="0000000000000001")
        spine2 = self.addSwitch("s2", dpid="0000000000000002")

        # Leaf switches
        leaf1 = self.addSwitch("l1", dpid="0000000000000003")
        leaf2 = self.addSwitch("l2", dpid="0000000000000004")

        # Hosts for leaf1
        h1 = self.addHost("h1")
        h2 = self.addHost("h2")

        # Hosts for leaf2
        h3 = self.addHost("h3")
        h4 = self.addHost("h4")

        # Connect hosts to leaves
        self.addLink(h1, leaf1)
        self.addLink(h2, leaf1)
        self.addLink(h3, leaf2)
        self.addLink(h4, leaf2)

        # Full-mesh links between leaves and spines
        for leaf in (leaf1, leaf2):
            for spine in (spine1, spine2):
                self.addLink(leaf, spine)

topos = {'spine_leaf': (lambda: SpineLeaf())}
