# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "custom_bom"
app_title = "Custom Bom"
app_publisher = "techerp@gmail.com"
app_description = "To Genrate and change bom material in sales order item table"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "techerp@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/custom_bom/css/custom_bom.css"
# app_include_js = "/assets/custom_bom/js/custom_bom.js"

# include js, css files in header of web template
# web_include_css = "/assets/custom_bom/css/custom_bom.css"
# web_include_js = "/assets/custom_bom/js/custom_bom.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "custom_bom.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "custom_bom.install.before_install"
# after_install = "custom_bom.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "custom_bom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

#Hook on document methods and events

doc_events = {
 	"Sales Invoice": {
 		"on_submit": "custom_bom.custom_bom.doctype.sales_invoice_length_width.si_length_width"
	},
	"Delivery Note": {
 		"on_submit": "custom_bom.custom_bom.doctype.sales_invoice_length_width.si_length_width"
	},
	"Quotation": {
 		"on_submit": "custom_bom.custom_bom.doctype.sales_invoice_length_width.si_length_width"
	},
	"Sales Order": {
 		"on_submit": "custom_bom.custom_bom.doctype.sales_invoice_length_width.si_length_width"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"custom_bom.tasks.all"
# 	],
# 	"daily": [
# 		"custom_bom.tasks.daily"
# 	],
# 	"hourly": [
# 		"custom_bom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"custom_bom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"custom_bom.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "custom_bom.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "custom_bom.event.get_events"
# }

