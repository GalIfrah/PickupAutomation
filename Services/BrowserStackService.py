import requests

from Infrastructure.GenericPageObject import GenericPO
from Services.ErrorService import ErrorsHandler


class browserStack:

    def changeTestStatus(self, newStatus, reason):

        sessionId = GenericPO.webDriver.remoteWebDriver.session_id

        headers = {
            'Content-Type': 'application/json',
        }

        data = '{"status":"' + newStatus + '", "reason":"' + reason + '"}'

        requests.put('https://api.browserstack.com/automate/sessions/' + sessionId + '.json',
                    headers=headers, data=data, auth=('galifrah4', 'N4XNKDnwH5ipipycghhp'))
