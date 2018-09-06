from __future__ import unicode_literals
import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

from datetime import datetime
from frappe.utils import getdate, validate_email_add, today, add_years,add_days,format_datetime
from erpnext.selling.doctype.sales_order.sales_order import make_sales_invoice
from frappe.model.naming import make_autoname
from frappe import throw, _, scrub
import frappe.permissions
from frappe.model.document import Document
import json
import collections
# import urllib
# import urllib2

@frappe.whitelist()
def getPrices():
	return []

