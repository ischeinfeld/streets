from sklearn.linear_model import Lasso

f = open("streets128D.emb")
x = []
y = []
#N = 24
ids = []
vecs = {}
vals = {}
import random
import numpy as np
import matplotlib.pyplot as plt
for line in f:
    if len(line.split(" ")) <= 2:
        continue
    id, vec = line.split(" ")[0], line.split(" ")[1:]
    vec = np.array(list(map(float,vec)))
    ids.append(id)
    vecs[id] = vec 
    vals[id] = id # appending id as a y-value for now, just for the sake of getting Lasso code working



plt.show()
x1=[]
x2=[]
y1=[]
y2=[]
rand = random.choice(ids)
print(rand)
sims = []
for vec in vecs:
    # print(vecs[rand])
    top = vecs[rand].dot(vecs[vec]) 
    bottom = (np.linalg.norm(vecs[vec]) * np.linalg.norm(vecs[rand]))
    sim = top/bottom
    sims.append(sim)
    if (sim < 0.9):
        x1.append(vecs[vec][0])
        y1.append(vecs[vec][1])
    else:
        x2.append(vecs[vec][0])
        y2.append(vecs[vec][1])

#plt.hist(sims)
#plt.show()



# Lasso time
lasso = Lasso(alpha = 0.01, max_iter = 1e5)
keys = vecs.keys()
lasso.fit([vecs[key] for key in keys], [vals[key] for key in keys])
print(lasso.coef_)



plt.scatter(x1,y1, c="red")
plt.scatter(x2,y2, c="blue")
plt.show()
