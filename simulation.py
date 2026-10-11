import numpy as np 
import matplotlib.pyplot as plt



G = 4*np.pi**2

mass = {
    'sun': 1.0,
    'earth': 3.0034e-6,
    'moon': 3.6923e-8}

r0 = {
    'sun': np.array([0,0,0]),
    'earth': np.array([9.978977040419635E-01, 6.586825681892025E-02, -6.320430920521123E-06]),
    'moon': np.array([9.956768547953816E-01, 6.676030485840675E-02, 1.641093070596718E-04])
     }
v0 = {
    'sun': np.array([0,0,0]),
    'earth': np.array([-4.70015711e-01, 6.25165839e+00, -3.40817831e-04]),
    'moon': np.array([-0.55065949, 6.03534661, 0.01111456])
}

t = 0

def F_gravity(ri,rj,mi,mj):
    
    r_vector = (ri - rj) 
    r_square = np.dot(r_vector,r_vector)
    r_unit = r_vector / np.sqrt(r_square)
    magnitude = (-G * mi * mj) 
    F = (magnitude / r_square) * r_unit
    return F 

def F_ES(rE):
    """Computes the gravitational force on Earth due to the Sun."""
    return F_gravity(rE,r0['sun'],mass['earth'],mass['sun'] )

def F_ME(rE):
    """Computes the gravitational force on Earth due to the Moon."""
    return F_gravity(rE,r0['moon'],mass['earth'],mass['moon'] )




def integrate_earth(tmax, dt = .001):
    steps = (int(tmax / dt) + 1)
 
    rE = r0['earth'].copy()
    rS = r0['sun'].copy()
    rM = r0['moon'].copy()
    vE = v0['earth'].copy()
    vS = v0['sun'].copy()
    vM = v0['moon'].copy()
    rvalues = [rE.copy()]
    for i in range(steps):
        #here we calculate the acceleration on earth from the moon and the sun, we need to correct the function for the moon as it's position too will change over time!
        aE =  (F_ES(rE) + F_ME(rE)) / mass['earth']
        v_new = vE + aE*dt
        r_new = rE + v_new * dt
        #here we update our velocity and position vectors with the new updated ones we calculate
        vE = v_new
        rE = r_new
        #here we update our list of position vectors with the new positions
        rvalues.append(rE.copy())
  
       
    
    return np.array(rvalues)
#here is a function that calculates the position of the moon as well, we'll need to return a list of values to feed 
def mE(tmax, dt = .001):
    rE = r0['earth'].copy()
    rS = r0['sun'].copy()
    rM = r0['moon'].copy()
    vE = v0['earth'].copy()
    vS = v0['sun'].copy()
    vM = v0['moon'].copy()




if __name__ == "__main__":
    positions = integrate_earth(1)

    plt.plot(positions[:,0], positions[:,1], label = "Earth")
    plt.scatter(0,0, color="orange", label="Sun")

    plt.xlabel("x (AU)")
    plt.ylabel("y (AU)")
    plt.axis("equal")
    plt.legend()
    plt.plot()
