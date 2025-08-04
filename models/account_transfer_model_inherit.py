# I imported this at the beginning because I was going to use the same way as the original function
# But after reviewing I found the other way so I deleted this import line
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class AccountAutomaticTransfer(models.Model):
    _inherit = 'account.transfer.model'

# I didn't know it was possible to inherit and just add a new selection at the beginning so I just used this way
    frequency = fields.Selection([
        ('daily', 'Daily'),
        ('month', 'Monthly'),
        ('quarter', 'quarterly'),
        ('year', 'yearly')
    ])
# This is the way I found after reviewing the code with
    # frequency = fields.Selection(selection_add=[('daily', 'Daily')], ondelete={'daily': 'set default'})

# Here I debugged till I found the function name and inherited it and added this
    def _get_next_move_date(self, date):
        self.ensure_one()
        if self.frequency == 'daily':
# This is the same way as the original function but I replaced it later when I found the other way
            delta = relativedelta(days=1)
        else:
            return super()._get_next_move_date(date)
        return date + delta - relativedelta(days=1)

# This is the way I found after review
    # def _get_next_move_date(self, current_date):
    #     self.ensure_one()
    #
    #     if self.frequency == 'daily':
    #         return current_date
    #     return super()._get_next_move_date(current_date)