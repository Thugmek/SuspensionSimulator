import matplotlib.pyplot as plt

m = 1
dm = 0.1
cm = 0.01
mm = 0.001

N = 1

s = 1

mass = 8
v_start = 1
l0 = 200*mm
l9 = 30*mm
c = 10*N/mm

t_step = 0.0001*s
v_treshold = 0.01
a_treshold = 0.01
t_treshold = 1

t_data = []
v_data = []
z_data = []
a_data = []

v = v_start
z = l0
t = 0
a = 0
v_data.append(v)
t_data.append(t)
z_data.append(z)
a_data.append(a)
while (abs(a) > a_treshold or abs(v) > v_treshold) and t <= t_treshold:
    l = l0-z
    f = l*c
    a = f/mass - 10 + v*0 if l>0 else -10
    v = v-a*t_step
    z = z-v*t_step
    t += t_step
    print(f"l: {l}, f: {f}, a: {a}, v: {v}, z: {z}")
    v_data.append(v)
    t_data.append(t)
    z_data.append(z)
    a_data.append(a)

fig, ax = plt.subplots(2, 2)
ax[0,0].plot(t_data,z_data)
ax[0,0].set_title("Position (m)")
ax[0,1].plot(t_data,v_data)
ax[0,1].set_title("Velocity (m/s)")
ax[1,0].plot(t_data,a_data)
ax[1,0].set_title("Acceleration (G)")
plt.show()