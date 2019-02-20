import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import codecs

appName = ''


def emailReporting(reporterType):

        email_user = 'galifrah1357@gmail.com'
        email_password = '1357975321'
        email_send = 'gal.i@mycheck.co.il'

        subject = 'Test'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = 'Hi ' + email_send[0:email_send.index('@')] + ', \nTake a look at the ' + reporterType + ' automation report for: ' + appName + '!!'
        msg.attach(MIMEText(body, 'plain'))

        dirPath = ""

        ScreenShotsDirPath = 'C:\\Users\galif\PycharmProjects\WebAutomation\Reports\screenShots'
        ReportsDirPath = 'C:\\Users\galif\PycharmProjects\WebAutomation\Reports\htmlReports'


        if reporterType == 'png':
            dirPath = ScreenShotsDirPath

            attachmentsList = []

            i = 0

            for fileName in os.listdir(dirPath):

                attachmentsList.insert(i, open('C:\\Users\galif\PycharmProjects\WebAutomation\Reports\screenShots\\' + str(fileName), 'rb'))

                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachmentsList[i].read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= " + fileName)
                msg.attach(part)

                i += 1



        elif reporterType == 'html':
            dirPath = ReportsDirPath

            search_dir = dirPath
            os.chdir(search_dir)
            files = filter(os.path.isfile, os.listdir(search_dir))
            files = [os.path.join(search_dir, f) for f in files]  # add path to each file
            files.sort(key=lambda x: os.path.getmtime(x))

            latest_file = files[-1]
            latest = codecs.open(latest_file, 'r', 'utf-8')




            part = MIMEBase('application', 'octet-stream')
            part.set_payload(latest.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= " + latest_file) # .name[latest_file.name.index('_'):-1])
            msg.attach(part)





        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)


        server.sendmail(email_user, email_send, text)
        server.quit()