=============
Apprise Module
=============



Installation
============

To install this module, you need to:

1. Install via pip `pip install apprise`
2. Download the module and add it to your Odoo addons folder. Afterward, log on to
your Odoo server and go to the Apps menu. Trigger the debug mode and update the
list by clicking on the "Update Apps List" link. Now install the module by
clicking on the install button.

Upgrade
============

To upgrade this module, you need to:

Download the module and add it to your Odoo addons folder. Restart the server
and log on to your Odoo server. Select the Apps menu and upgrade the module by
clicking on the upgrade button.

Configuration
=============

No additional configuration is needed to use this module.

Usage
=============

After the module is installed, the design is adjusted accordingly.

* Currently it's working with Contacts/Partners within a notebook page
* Each Contact profile will need to set apprise services urls sepearated by comma. For further information about the services urls, please refer to `apprise wiki <https://github.com/caronc/apprise/wiki>`
* Once the services urls , subject and message are set. The admin/agent will be able to send notifications to the selected services by clicking on the "Notify" button


Future Plans
=======

* clear the notification fields after sending the notification
* add a notification history page
* inherit report module to send reports as attachement to coresponding notification services


Credits
=======

Author & Contributors
------------

* Jean Khawand <jk@jeankhawand.com> (Author)

Images
------------

Some pictures are based on or inspired by:

* `Freepik <https://www.flaticon.com/authors/freepik>`_

Projects
------------

Parts of the module are inspired by:

* `Web Responsive <https://github.com/OCA/web>`_
* `List Range Selection <https://github.com/OCA/web>`_
* `Openworx Backend Theme <https://github.com/Openworx/backend_theme>`_
* Special thanks to Chris for `Apprise <https://github.com/caronc/apprise>`_
