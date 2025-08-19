#  **`ping`** – Check connectivity

**Purpose**: Sends ICMP echo requests to test if a host is reachable and measure latency.

``` bash
ping google.com
```

---
#  **`traceroute`** – Trace route to destination

**Purpose**: Shows the **hops** (routers) a packet takes to reach a destination.

``` bash
sudo pacman -S traceroute      # Install if not available
```

``` bash
traceroute google.com
```

---
# **`nslookup`** – Query DNS servers

**Purpose**: Translates domain names to IP addresses and vice versa.

``` bash
nslookup google.com
```

---
