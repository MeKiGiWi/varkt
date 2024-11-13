import matplotlib.pyplot as plt
from json import load 


plt.ylabel('Height')
plt.xlabel('Time')
plt.grid(True)
with open('data.json', 'r') as f:
    database = load(f)
    plt.plot([x[0] for x in database], [x[1] for x in database])
with open('our_data.json', 'r') as f:
    database = load(f)
    plt.plot([x[0] for x in database], [x[1] for x in database], color='r')
plt.show()