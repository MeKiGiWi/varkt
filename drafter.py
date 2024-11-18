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
    plt.plot([x[0] for x in database], [x[3] for x in database], color='r')
#     fig, ax = plt.subplots(4)
#     def mat(x):
#         return 0 <= x <= 500
#     ax[0].plot([x[0] for x in database if mat(x[0])], [x[1] for x in database if mat(x[0])])
#     ax[1].plot([x[0] for x in database if mat(x[0])], [x[2] for x in database if mat(x[0])], color='r')
#     ax[2].plot([x[0] for x in database if mat(x[0])], [x[3] for x in database if mat(x[0])], color='y')
#     ax[3].plot([x[0] for x in database if mat(x[0])], [x[4] for x in database if mat(x[0])], color='g')
plt.show()