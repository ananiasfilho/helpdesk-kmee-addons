from odoo import models, fields, api

class HelpdeskTicketDependencyHistory(models.Model):
    _name = 'helpdesk.ticket.dependency.history'
    _description = 'Helpdesk Ticket Dependency History'
    _order = 'change_date desc'

    ticket_id = fields.Many2one('helpdesk.ticket', required=True, ondelete='cascade')
    team_id = fields.Many2one('helpdesk.ticket.team', ondelete='set null')  # Permite None
    change_date = fields.Datetime(default=fields.Datetime.now)
    duration = fields.Char(compute='_compute_duration', store=False)

    def _compute_duration(self):
        now = fields.Datetime.now()
        for record in self:
            if not record.team_id:  # Se não há time dependente
                record.duration = "Não rastreado"
                continue

            next_record = self.search([
                ('ticket_id', '=', record.ticket_id.id),
                ('change_date', '>', record.change_date)
            ], limit=1, order='change_date asc')

            end_date = next_record.change_date if next_record else now
            delta = end_date - record.change_date
            days = delta.days
            hours, remainder = divmod(delta.seconds, 3600)
            minutes = remainder // 60
            record.duration = f"{days} dias {hours:02d}:{minutes:02d} horas"
