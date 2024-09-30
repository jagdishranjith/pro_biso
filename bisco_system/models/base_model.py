from odoo import models

class BaseModel(models.AbstractModel):
    _inherit = 'base'

    def _check_company(self, fnames=None):
        """ Override company check to disable it """
        return

    def _check_company_domain(self, companies):
        """Domain to be used for company consistency between records regarding this model.

        :param companies: the allowed companies for the related record
        :type companies: BaseModel or list or tuple or int or unquote
        """
        return []
