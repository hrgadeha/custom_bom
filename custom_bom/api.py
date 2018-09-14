from __future__ import unicode_literals
import frappe
import json

@frappe.whitelist()
def getBOMList(item_code):
	return frappe.get_list("BOM",filters=[["item","=",item_code]],fields=["*"])

@frappe.whitelist()
def getBomDetail(bom_no):
	return frappe.get_doc("BOM",bom_no)
	
@frappe.whitelist()
def saveBOM(item,items,currency):
	doc = frappe.get_doc({
		"docstatus":0,
		"doctype":"BOM",
		"name":"New BOM 1",
		"quantity":1,
		"is_active":1,
		"is_default":0,
		"rm_cost_as_per":"Price List",
		"buying_price_list":"Standard Selling",
		"company":frappe.defaults.get_user_default('company'),
		"currency":currency,
		"items":[json.loads(items)],
		"item":item
		})
	doc.insert()
		


