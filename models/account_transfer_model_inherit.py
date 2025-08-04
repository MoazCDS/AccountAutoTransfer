from odoo import models, fields, api

class AccountAutomaticTransfer(models.Model):
    _inherit = 'account.transfer.model'

    frequency = fields.Selection(selection_add=[('daily', 'Daily')], ondelete={'daily': 'set default'})


    def _get_next_move_date(self, current_date):
        self.ensure_one()

        if self.frequency == 'daily':
            return current_date
        return super()._get_next_move_date(current_date)