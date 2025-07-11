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
    angular_acceleration = tau * I
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

    F_radians = math.radians(F_direction)
    sine_radians = math.sin(F_radians)
    torque = F_magnitude * sine_radians * r
    return torque


# 7
def calculate_moment_of_inertia(m, r):
    """
    Calculates the moment of inertia of an object.

    Parameters:
    m (float): mass of  object in kg.
    r (float): distance from the axis of rotation to the center of mass of the object in m.
    Return:
    m_of_inertai (float): moment of inertia of object in kg * m^2
    """
    m_of_inertia = m * r**2
    return m_of_inertia


# 8
def calculate_auv_acceleration(F_magnitude, mass):
    auv_acceleration = F_magnitude / mass
    return auv_acceleration


def calculate_auv_angular_acceleration(F_magnitude, F_angle):
    if F_angle > 30 or F_angle < -30:
        raise ValueError("input must be between 30 and -30")
    if F_magnitude < 0 or F_magnitude > 100:
        raise ValueError("the thruster force has to be between 0 and 100N")
    F_radians = math.radians(F_angle)
    torque = F_magnitude * math.sin(F_radians) * 0.5  # thruster distance is 0.5
    angular_acceleration = torque * 1  # inertia is 1
    return angular_acceleration


# 9
def calculate_auv2_acceleration(T, alpha, theta, mass):
    T = np.array([T1, T2, T3, T4])
    alpha_radians = math.radians(alpha)  # turns into radians
    theta_radians = math.radians(theta)  # turns into radians


# acceleration x
# T1*math.sin(alpha_radians + theta_radians) / mass #acceleration from T1 = F/m
