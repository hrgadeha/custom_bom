from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def getBOMList(item_code):
	return frappe.get_list("BOM",filters=[["item","=",item_code]],fields=["*"])

@frappe.whitelist()
def getBomDetail(bom_no):
	return frappe.get_doc("BOM",bom_no)


