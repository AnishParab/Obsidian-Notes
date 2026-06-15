# NOTE:

Arch Linux uses KVM/QEMU natively, so the best path is **virt-manager** (libvirt frontend) with KVM acceleration. Way faster than VirtualBox for this use case.

---
## **Step 1: Install the stack**

```bash
sudo pacman -S virt-manager qemu-full libvirt dnsmasq bridge-utils vde2 openbsd-netcat
```

---
## **Step 2: Enable and start libvirt**

```bash
sudo systemctl enable --now libvirtd
```

---
## **Step 3: Add your user to the libvirt group** (avoids running virt-manager as root)

```bash
sudo usermod -aG libvirt $(whoami)
```

Log out and back in for the group change to take effect.

---
## **Step 4: Download Kali ISO**

Get the installer ISO from [kali.org/get-kali](https://www.kali.org/get-kali/) — pick **Installer** (not live), 64-bit. The "Everything" image includes all tools; the default image lets you install metapackages post-install. Either works.

---
## **Step 5: Create the VM**

```bash
virt-manager
```

New VM → Local install media → point to the Kali ISO.

Recommended specs for ethical hacking use:

- RAM: 4GB minimum, 8GB if your system allows
- Disk: 50GB+ (tools eat space)
- CPUs: 2–4 cores
- Enable **VirtIO** for disk and network (better perf than emulated)

---
## **Step 6: Install Kali**

Standard guided install. Create a non-root user. Pick the `kali-linux-default` metapackage during install — gives you the core tools without 60GB of everything.

---
## **Step 7: Enable clipboard + display quality** (optional but useful)

Install guest agents inside the Kali VM after booting:

```bash
sudo apt install spice-vdagent qemu-guest-agent
```

This enables copy-paste between host/guest and dynamic display resizing.

---
**Gotcha**: If `virt-manager` can't connect to libvirt, check that the service is running and your user is actually in the group (`groups` in a new terminal).

**Gotcha**: KVM requires virtualization to be enabled in BIOS/UEFI (Intel VT-x / AMD-V). Verify with:

```bash
grep -E 'vmx|svm' /proc/cpuinfo | head -1
```

No output = needs to be enabled in BIOS.

---
