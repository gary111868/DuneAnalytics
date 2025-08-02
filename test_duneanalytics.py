# test_duneanalytics.py
"""
Tests for DuneAnalytics module.
"""

import unittest
from duneanalytics import DuneAnalytics

class TestDuneAnalytics(unittest.TestCase):
    """Test cases for DuneAnalytics class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DuneAnalytics()
        self.assertIsInstance(instance, DuneAnalytics)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DuneAnalytics()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
