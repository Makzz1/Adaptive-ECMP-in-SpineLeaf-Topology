#!/bin/bash

# Start Open vSwitch
echo "[INFO] Starting Open vSwitch..."
/usr/share/openvswitch/scripts/ovs-ctl start

# Wait for Ryu controller to be ready
echo "[INFO] Waiting for Ryu controller at 172.31.0.2..."
sleep 5

# Launch Mininet with custom topology
echo "[INFO] Launching Mininet..."
mn --custom /opt/topo/spine_leaf_topology.py \
   --topo spine_leaf \
   --controller=remote,ip=172.31.0.2 \
   --switch=ovs,protocols=OpenFlow13
