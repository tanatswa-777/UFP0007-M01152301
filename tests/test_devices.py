import unittest

from devices import Computer, Printer, Sensor


class TestDeviceAttention(unittest.TestCase):
    def test_hot_sensor(self):
        sensor = Sensor("Server Room", "Block A", 34)
        self.assertFalse(sensor.needs_attention())

    def test_offline_computer(self):
        computer = Computer("Lab PC", "Lab 2", False)
        self.assertTrue(computer.needs_attention())

    def test_low_toner_printer(self):
        printer = Printer("Library Printer", "Library", 8)
        self.assertEqual(printer.status(), "Toner 8%")

    # TODO: add normal cases and test all details
