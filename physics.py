import numpy as np
import math


# 1
def calculate_buoyancy(density_fluid, V):
    """
    Calculates buoyancy force exerted on an object submerged in a fluid.

    Parameters:
    density_fluid (float): Density of fluid in kg/m^3.
    V (float): volume of object submerged in m^3.
    Returns:
    buoyancy (float): Buoyancy force in N.
    """

    if density_fluid <= 0 or V <= 0:
        # return False
        raise ValueError("Density of fluid and volume must be greater than 0")
    buoyancy = density_fluid * V * 9.81
    return buoyancy


# 2
def will_it_float(V, mass):  # V in m^3, mass in kg
    """
    Determines if an object will float in water.

    Parameters:
    V (float): volume of object in m^3.
    mass (float): mass of object in kg.
    Returns:
    True if object floats, False if it sinks.
    """

    water_density = 1000  # in kg/m^3
    object_density = V * mass
    if V <= 0 or mass <= 0:
        raise ValueError("mass of object and volume must be greater than 0")
    if object_density < water_density:
        return True
    else:
        return False


# 3
def calculate_pressure(depth):  # depth in meters
    """
    Calculates the pressure an object experiencesat a certain depth.

    Parameter:
    depth (float): depth of object in meters
    Returns:
    pressure (float): pressure exerted on object in Pascals.
    """

    pressure = depth * 9.81 * 1000
    return pressure


# 4
def calculate_acceleration(F, m):
    """
    Calculates acceleration of an object.

    Parameters:
    F (float): Force applied in N
    m (float): Mass of object in kg
    Return:
    acceleration(float): acceleration of object in m/s^2
    """
    if m <= 0:
        raise ValueError("mass of object must be greater than 0")
    acceleration = F / m
    return acceleration


# 5
def calculate_angular_acceleration(tau, I):  # tau = torque, I = moment of inertia
    """
    Calculates angular acceleration of an object.

    Parameters:
    tau (float): Torque applied to object in newton-meters.
    I (float): moment of inertia of object in kg * m^2
    """
    if I <= 0:
        raise ValueError("moment of inertia must be greater than 0")
    angular_acceleration = tau / I
    return angular_acceleration


# 6
def calculate_torque(F_magnitude, F_direction, r):
    """
    Calculates torque applied to an object.

    Parameters:
    F_magnitude(float): the magnitude of force applied to the object in N.
    F_direction (float):  direction of the force applied to the object in degrees.
    r (float):  distance from the axis of rotation to the point where the force is applied in m
    Return:
    torque (float): torque applied to object in newton-meters
    """

    F_radians = math.radians(F_direction) #turns into radians
    torque = F_magnitude * math.sin(F_radians) * r #cross product r * F
    return torque



# 7
def calculate_moment_of_inertia(m, r):
    """
    Calculates the moment of inertia of an object.

    Parameters:
    m (float): mass of  object in kg.
    r (float): distance from the axis of rotation to the center of mass of the object in m.
    Return:
    m_of_inertia (float): moment of inertia of object in kg * m^2
    """
    m_of_inertia = m * r**2
    return m_of_inertia


# 8
def calculate_auv_acceleration(F_magnitude, F_angle, mass=100): 
    """
    Calculates the acceleration of the AUV in the 2D plane.
    
    Parameters:
    F_magnitude: magnitude of force applied by thruster in N.
    F_angle: angle of the force applied by the thruster in radians
    mass: mass of AUV in kg
    Returns:
    auv_acceleration in meters/sec^2
    """
    if F_angle > 30 or F_angle < -30:
        raise ValueError("angle between 30 and -30")
    if F_magnitude < 0 or F_magnitude > 100:
        raise ValueError("thruster force between 0 and 100N")
    
    Fx = (F_magnitude * math.cos(F_angle)) #seaprates force into components
    Fy = (F_magnitude * math.sin(F_angle)) 
    force_vector = np.array([Fx, Fy]) #makes it into an array
    auv_acceleration = force_vector/mass 
    return auv_acceleration


def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia, thruster_distance = 0.5):
    """
    Calculates the angular acceleration of the AUV in the 2D plane.
    
    Parameters:
    F_magnitude: magnitude of force applied by thruster in N.
    F_angle: angle of the force applied by the thruster in radians
    inertia: moment of intertia of AUV in kg * m^2
    thruster_distance: distnace from center of mass of AUV to thruster in meters
    Returns:
    angular_acceleration in radians/sec^2
    """
    if F_angle > 30 or F_angle < -30:
        raise ValueError("angle between 30 and -30")
    if F_magnitude < 0 or F_magnitude > 100:
        raise ValueError("thruster force between 0 and 100N")
    torque = F_magnitude * math.sin(F_angle) * thruster_distance  # thruster distance is 0.5
    angular_acceleration = torque / inertia
    
    return angular_acceleration


# 9
def calculate_auv2_acceleration(T, alpha, theta, mass = 100):
    """
    Calculates the acceleration AUV in the 2D plane.

    Parameters: 
    T: an np.ndarray of the magnitudes of the forces applied by the thrusters in N.
    alpha: angle of the thrusters in radians
    theta: angle of the AUV in radians
    mass: mass of the AUV in kilograms
    Returns:
    acceleration_vector in meters/sec^2
    """

    T = np.array(T) #converts T into a numpy array

    angles = np.array([theta+alpha,  # makes array of angles of each thruster in order T1-->T4
                       theta-alpha,
                       np.pi+theta+alpha,
                       np.pi+theta-alpha])
    
    counter = 0 #defines variable before being used
    Fx = 0
    Fy = 0
    for angle in angles:
        Fx += (T[counter] * math.cos(angle)) #for each thruster/angle, separates into compnents x and y and adds them together
        Fy += (T[counter] * math.sin(angle))
        counter+=1

    force_vector = np.array([Fx, Fy]) #puts added up x and y components into a force vector
    acceleration_vector = force_vector/mass
    return acceleration_vector


#9.2

def calculate_auv2_angular_acceleration(T, alpha, l, L, inertia = 100):
    """
    Calculates the angular acceleration AUV in the 2D plane.

    Parameters: 
    T: an np.ndarray of the magnitudes of the forces applied by the thrusters in N.
    alpha: angle of the thrusters in radians
    l: the distance from the center of mass of AUV to the thrusters in m 
    L: the distance from the center of mass of AUV to the thrusters in m
    intertia: the moment of inertia of the AUV in kg * m^2
    Returns:
    angular_acceleration in radians/sec^2
    """
    T = np.array(T) #converts T into a numpy array
    angles = np.array([alpha, # makes array of angles of each thruster in order T1-->T4
                       -alpha,
                       np.pi+alpha,
                       np.pi-alpha])
    
    thruster_distance = np.sqrt(l**2 + L**2)
    x = 0
    auv2_angular_acceleration = 0
    while x <4:
        auv2_angular_acceleration += calculate_auv_angular_acceleration(T[x], angles[x], inertia, thruster_distance)
        x += 1
    
    return auv2_angular_acceleration
   

#10.1
def simulate_auv2_motion(T, alpha, l, L, mass, inertia = 100, dt = 0.1, t_final = 10, x0 = 0, y0 = 0, theta0=0):
    T = np.array(T)
    t = 0
    i=1
    time = []
    steps = t_final/dt

    x = np.zeros(steps)
    x[0]=x0 #initial position
    y = np.zeros(steps)
    y[0]=y0 #initial position
    theta = np.zeros(steps)
    theta[0] = theta0 #initial angle
    v = np.zeros(steps)
    omega = np.zeros(steps)
    a = np.zeros(steps)
    

    while t < t_final:
        time.append(t) #time steps of simulation 
        
        # make array of angles of each thruster in order T1-->T4
        angles = np.array([theta[i-1]+alpha,  
                       theta[i-1]-alpha,
                       np.pi+theta[i-1]+alpha,
                       np.pi+theta[i-1]-alpha])
        
        #COMPUTE FORCE
        f_x = np.sum(T * np.cos(angles)) #total forces in the x and y directions, multiplies forces of each thruster w angle components, and adds for all the thrusters
        f_y = np.sum(T* np.sin(angles))

        #COMPUTE ACCELERATION
        a_x = f_x/mass #acceleration for each direction
        a_y = f_y/mass
        a[i-1] = np.sqrt(a_x**2 + a_y**2) #turns into scalar

        #velocity
        v_x += a_x * dt # velocity = initial + acceleration * time, time elapsed is always in dt intervals
        v_y += a_y * dt
        v[i-1] = np.sqrt(v_x**2 + v_y**2) #turns into scalar

        #position
        x[i] = x[i-1] + v_x * dt #position at point i = the position at point i-1 + velocity*the amount of time that has passed, and x[1-1] = 0
        y[i] = y[i-1] + v_y * dt

        #angular acceleration
        ang_acceleration = calculate_auv2_angular_acceleration(T, alpha, theta[i-1], l, L, inertia)
        omega[i] = omega[i-1] + ang_acceleration * dt # same as position except for angles
        theta[i] = theta [i-1] + ang_acceleration * dt

        
        t += dt
        i += 1
    
    return np.array(time), x, y, theta, v, omega, a


# OLD 9.2
"""T = np.array(T) #converts T into a numpy array

    angles = np.array([alpha, # makes array of angles of each thruster in order T1-->T4
                       -alpha,
                       np.pi+alpha,
                       np.pi-alpha])
    
    counter = 0 #defines variables before it's used
    torque = 0

    for angle in angles:
        x = (T[counter] * math.cos(angle)) #separates every thruster's force into x and y components
        y = (T[counter] * math.sin(angle))
        torque+= (x*l - y*L) #for every thruster's F, its cross producted with distance from center of rotation and added together
        counter+=1 #repeats for every thruster
    
    angular_acceleration = torque / inertia
    return angular_acceleration"""