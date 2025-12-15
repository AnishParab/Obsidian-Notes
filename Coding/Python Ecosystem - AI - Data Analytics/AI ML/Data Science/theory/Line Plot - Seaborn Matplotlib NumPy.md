# Line Plot
``` python
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line Plot
# Pass as kwargs
sb.lineplot(x=x, y=y)

plt.show()
```

---
