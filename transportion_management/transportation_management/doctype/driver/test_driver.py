# Copyright (c) 2013, Arun Logistics and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Driver')

class TestDriver(unittest.TestCase):
	pass
