from odoo import models, fields, api

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    dependency_team_id = fields.Many2one(
        'helpdesk.ticket.team',
        string='Delivery dependency',
        tracking=True,
        ondelete='set null',  # Permite limpar o campo
        context={'show_null_option': True}  # ← Linha-chave!
    )
    dependency_history_ids = fields.One2many(
        'helpdesk.ticket.dependency.history',
        'ticket_id',
        string='Dependency History',
        readonly=True
    )

    def write(self, vals):
        if 'dependency_team_id' in vals:
            for ticket in self:
                # Cria histórico apenas se houver mudança REAL (incluindo para None)
                if ticket.dependency_team_id.id != vals['dependency_team_id']:
                    ticket._create_dependency_history(vals['dependency_team_id'])
        return super().write(vals)

    def _create_dependency_history(self, team_id):
        self.ensure_one()
        # Permite team_id=False (quando o campo é limpo)
        self.env['helpdesk.ticket.dependency.history'].sudo().create({
            'ticket_id': self.id,
            'team_id': team_id  # Pode ser None
        })
