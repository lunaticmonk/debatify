from flask_mail import Message
app.config['DEBATIFY_MAIL_SUBJECT_PREFIX'] = '[Debatify]'
app.config['DEBATIFY_MAIL_SENDER'] = 'Debatify Admin <debatify@example.com>'

def send_email(to, subject, template, **kwargs):
	msg = Message(app.config['DEBATIFY_MAIL_SUBJECT_PREFIX'] + subject,sender=app.config['DEBATIFY_MAIL_SENDER'], recipients=[to])
	msg.body = render_template(template + '.txt', **kwargs)
	msg.html = render_template(template + '.html', **kwargs)
	mail.send(msg)