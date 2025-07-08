import numpy as np
import matplotlib.pyplot as plt
import attoworld as aw
#aw.plot.set_style(theme="light", font_size=14)



x = np.linspace(0, 10, 100)
y = [i**6 for i in x]
z = [i*3 + 1 for i in x]



fig, axis = plt.subplots(1, 2, figsize=(12, 6))
axis[0].plot(x, y)
# axis[1].plot(x, z)
# aw.plot.label_letter("a", axis=axis[0], style="Nature")
# aw.plot.label_letter("b", axis=axis[1], style="Nature")
plt.show()
