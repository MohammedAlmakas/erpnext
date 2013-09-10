# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd.
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import webnotes

def get_context():
	from portal.website_transactions import get_transaction_context
	context = get_transaction_context("Sales Invoice", webnotes.form_dict.name)
	context.update({
		"parent_link": "invoices",
		"parent_title": "Invoices"
	})
	return context