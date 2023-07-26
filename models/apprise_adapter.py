from odoo import models, fields
from odoo.exceptions import UserError
import logging
import apprise
logger = logging.getLogger(__name__)
    
class ResPartner(models.Model):
    _inherit = 'res.partner'
    apprise_services_urls = fields.Char(string='Apprise Services URLs')
    subject = fields.Char(string='Subject')
    message = fields.Text(string='Message')
    def action_notify(self):
        services_urls = self.apprise_services_urls
        subject = self.subject
        message = self.message
        if services_urls and subject and message:
            logger.info("[Apprise-Adapter]: preparing to send notification")
            if len(services_urls) > 10:
                # define apprise object
                apobj = apprise.Apprise()
                for url in services_urls.split(','):
                    apobj.add(url)
                logger.info("[Apprise-Adapter]: done adding urls to Apprise")
                if apobj.notify(body=message,title=subject):
                    notification = {
                        'type': 'ir.actions.client',
                        'tag': 'display_notification',
                        'params': {
                            'title': ('Success'),
                            'message': 'Notification Executed Successfully',
                            'type': 'success',
                            'sticky': True
                        }
                    } 
                    return notification
                else:
                    raise UserError("[Apprise]: unable to send notification check logs")  

            else:
                raise UserError("[Apprise-Adapter]: Please check services urls")
        else:
            raise UserError("[Apprise-Adapter]: Services URLS, Message and Subject shouldn't be empty")