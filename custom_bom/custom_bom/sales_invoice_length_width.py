from __future__ import unicode_literals
import frappe
from frappe import msgprint
from frappe.model.document import Document

def si_length_width(doc,method):
	for d in doc.items:
		d.amount = (d.length * d.width * d.qty * d.rate) / 1000000
