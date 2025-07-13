import unittest
import physics
import math
import numpy as np


def calculate_auv_acceleration(F_magnitude, F_angle, mass=100):
    if F_angle > 30 or F_angle < -30:
        raise ValueError("angle between 30 and -30")
    if F_magnitude < 0 or F_magnitude > 100:
        raise ValueError("thruster force between 0 and 100N")

    Fx = F_magnitude * math.cos(F_angle)  # seaprates force into components
    Fy = F_magnitude * math.sin(F_angle)
    force_vector = np.array([Fx, Fy])  # makes it into an array
    auv_acceleration = force_vector / mass
    return auv_acceleration


class Test_(unittest.TestCase):
    def test_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(1, 2), 19.62)
        self.assertNotEqual(physics.calculate_buoyancy(1, 2), 20)
        self.assertRaises(ValueError, physics.calculate_buoyancy, -1, 2)

    def test_will_it_float(self):
        self.assertTrue(physics.will_it_float(0.09, 2))
        self.assertFalse(physics.will_it_float(40, 58))
        self.assertRaises(ValueError, physics.will_it_float, -0.09, -2)

    def test_pressure(self):
        self.assertAlmostEqual(physics.calculate_pressure(10), 98100)
        self.assertNotEqual(physics.calculate_pressure(20), 100000)

    def test_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(10, 2), 5)
        self.assertNotEqual(physics.calculate_acceleration(10, 7), 30)

    def test_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(10, 2), 5)
        self.assertNotEqual(physics.calculate_angular_acceleration(10, 2), 30)

    def test_torque(self):
        self.assertAlmostEqual(physics.calculate_torque(10, 30, 2), 10)
        self.assertNotAlmostEqual(physics.calculate_torque(10, 30, 2), 56)

    def test_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(3, 3), 27)
        self.assertNotEqual(physics.calculate_moment_of_inertia(3, 3), 20)

    def test_calculate_auv_acceleration(self):
        acc = calculate_auv_acceleration(10, math.radians(30), 100)
        # Expected values
        a_x = 0.0866025404
        a_y = 0.050
        #a_x = (10 * math.cos(math.radians(30))) / 100
        #a_y = (10 * math.sin(math.radians(30))) / 100
        self.assertAlmostEqual(acc[0], a_x)
        self.assertAlmostEqual(acc[1], a_y)

        with self.assertRaises(ValueError):
            physics.calculate_auv_acceleration(120, math.radians(10))
        with self.assertRaises(ValueError):
            physics.calculate_auv_acceleration(10, math.radians(-80))

    def test_calculate_auv_angular_acceleration(self):
        self.assertAlmostEqual(
            physics.calculate_auv_angular_acceleration(10, 0.4, 1, 0.5), 1.947091711543253)
        self.assertAlmostEqual(
            physics.calculate_auv_angular_acceleration(10, 0.4, 2, 0.5), 0.9735458557716263)
    
    def test_calculate_auv2_angular_acceleration(self):
        self.assertAlmostEqual(physics.calculate_auv2_angular_acceleration([10, 1, 4, 0], 0.12, 5, 4, 1), 3.8326606800413248)



if __name__ == "__main__":
    unittest.main()
