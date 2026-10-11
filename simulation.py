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

def F_MS(rS):
    """Computes the gravitational force on Earth due to the Moon."""
    return F_gravity(rS,r0['sun'],mass['moon'],mass['sun'] )

def integrate_system(tmax, dt = 0.001):

    rE = r0['earth'].copy()
    rS = r0['sun'].copy()
    rM = r0['moon'].copy()
    vE = v0['earth'].copy()
    vS = v0['sun'].copy()
    vM = v0['moon'].copy()
    
    steps = int(round(tmax / dt))
    earth_positions = [rE.copy()]
    moon_positions = [rM.copy()]
    sun_positions = [rS.copy()]
    for i in range(steps):
    #here are the accelerations for the earth from the sun and the moon from the earth
        aE = (F_gravity(rE,rS,mass['earth'],mass['sun']) + F_gravity(rE,rM,mass['earth'],mass['moon'])) / mass['earth']
        aM = (F_gravity(rM,rE,mass['moon'],mass['earth']) + F_gravity(rM, rS, mass['moon'],mass['sun']))  / mass['moon']
        aS = (F_gravity(rS,rE,mass['sun'],mass['earth']) + F_gravity(rS,rM,mass['sun'],mass['moon'])) / mass['sun']

    #here we calculate the new velocities and position of the earth

        vE_new = vE + aE*dt
        rE_new = rE + vE_new * dt

  

    #here we find the velocity and position of the moon
        vM_new = vM + aM*dt
        rM_new = rM + vM_new * dt
    

    #here we find the velocity and position of the sun
        vS_new = vS + aS*dt
        rS_new = rS + vS_new * dt

    #now we update our new positions
        rE = rE_new
        rM = rM_new
        rS = rS_new

        vE = vE_new
        vM = vM_new
        vS = vS_new

        earth_positions.append(rE.copy())
        moon_positions.append(rM.copy())
        sun_positions.append(rS.copy())

    return (
        np.array(earth_positions),
        np.array(moon_positions),
        np.array(sun_positions)
    )


if __name__ == "__main__":


    earth, moon, sun = integrate_system(1)



    plt.figure(figsize=(8, 8))

    plt.plot(earth[:, 0], earth[:, 1], label='Earth', color='blue')
    plt.plot(moon[:, 0], moon[:, 1], label='Moon', color='gray')
    plt.plot(sun[:, 0], sun[:, 1], label='Sun', color='orange')

    plt.xlabel('X Position (AU)')
    plt.ylabel('Y Position (AU)')
    plt.title('Sun-Earth-Moon Three-Body Simulation')

    plt.axis('equal')
    plt.legend()
    plt.grid(True)
    plt.show()

print("Earth:", earth.shape)
print("Moon:", moon.shape)
print("Sun:", sun.shape)

relative_moon = moon - earth

plt.figure(figsize=(8, 8))

plt.plot(
    relative_moon[:, 0],
    relative_moon[:, 1],
    color='gray',
    label='Moon'
)

plt.scatter(0, 0, color='blue', label='Earth')

plt.xlabel('X Position Relative to Earth (AU)')
plt.ylabel('Y Position Relative to Earth (AU)')
plt.title('Moon Orbit in Earth-Centered Coordinates')

plt.axis('equal')
plt.legend()
plt.grid(True)
plt.show()


