import unittest
import physics


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
        self.assertEqual(physics.calculate_angular_acceleration(10, 2), 20)
        self.assertNotEqual(physics.calculate_angular_acceleration(10, 2), 30)

    def test_torque(self):
        self.assertAlmostEqual(physics.calculate_torque(10, 30, 2), 10)
        self.assertNotAlmostEqual(physics.calculate_torque(10, 30, 2), 56)

    def test_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(3, 3), 27)
        self.assertNotEqual(physics.calculate_moment_of_inertia(3, 3), 20)


if __name__ == "__main__":
    unittest.main()
