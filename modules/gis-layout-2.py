from pylayers.gis.layout import  *
import matplotlib.pyplot as plt
L = Layout('exemple.str')
L.buildGt()
L.buildGr()
L.buildGv()
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(221)
fig,ax = L.showG('s',fig=fig,ax=ax)
tis = plt.title("Gs")
ax = fig.add_subplot(222)
fig,ax = L.showG('r',fig=fig,ax=ax)
tit = plt.title("Gt")
ax = fig.add_subplot(223)
fig,ax = L.showG('c',fig=fig,ax=ax)
tic = plt.title("Gc")
ax = fig.add_subplot(224)
fig,ax = L.showG('v',fig=fig,ax=ax)
tiv = plt.title("Gv")
plt.show()