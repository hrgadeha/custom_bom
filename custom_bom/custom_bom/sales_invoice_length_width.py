from __future__ import unicode_literals
import frappe
from frappe import msgprint
from frappe.model.document import Document

def si_length_width(doc,method):
	from frappe.utils import flt
	total = 0.0
	for d in doc.items:
		d.amount = (flt(d.length) * flt(d.width) * flt(d.qty) * flt(d.rate)) / 1000000
		total += d.amount
		frappe.msgprint(total)
	
	#doc.new_total = total
