# Memory Table

| Mechanism         | Authentication | Integrity | Confidentiality | Nonrepudiation |
| ----------------- | -------------- | --------- | --------------- | -------------- |
| Hash              | No             | Yes       | No              | No             |
| MAC               | Yes            | Yes       | No              | No             |
| Digital Signature | Yes            | Yes       | No              | Yes            |
| Encryption        | Sometimes      | Sometimes | Yes             | No             |

---
# Summary

```text
Hash
    → Detect modification

MAC
    → Detect modification
      + Verify sender

Digital Signature
    → Detect modification
      + Verify sender
      + Nonrepudiation
```

---
