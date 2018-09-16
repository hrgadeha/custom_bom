from __future__ import unicode_literals
import frappe
import json

@frappe.whitelist()
def getBOMList(item_code):
	try:
		return frappe.get_list("BOM",filters=[["item","=",item_code]],fields=["*"])
	except:
		frappe.msgprint("Problem with fetching information of BOM List")

@frappe.whitelist()
def getBomDetail(bom_no):
	try:
		return frappe.get_doc("BOM",bom_no)
	except:
		frappe.msgprint("Problem with fetching information of BOM")
@frappe.whitelist()
def saveBOM(item,items,currency):
	try:
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
			"items":json.loads(items),
			"item":item
			})
		return doc.insert()
	except:
		frappe.msgprint("Problem in BOM Creation")
		


