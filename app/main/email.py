from flask import render_template, current_app
from flask_babel import _
from app.email import send_email


def send_copy_email(user, postBody, postAuthor):
    send_email(_('[Microblog] Post'),
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/send_copy.txt',
                                         user=user, postBody=postBody, postAuthor=postAuthor),
               html_body=render_template('email/send_copy.html',
                                         user=user, postBody=postBody, postAuthor=postAuthor))
