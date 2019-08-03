import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from app import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    width, height = i.size
    if height>width:
        up=(height-width)/2
        dw=width+((height-width)/2)
        box=(0,up,width,dw)
    else:
        le=(width-height)/2
        ri=height+(width-height)/2
        box=(le,0,ri,height)
    im=i.crop(box)
    im.thumbnail(output_size)
    im.save(picture_path)
    return picture_fn

#def save_post_picture(form_picture):
#    random_hex = secrets.token_hex(8)
#    _, f_ext = os.path.splitext(form_picture.filename)
#    picture_fn = random_hex + f_ext
#    picture_path = os.path.join(current_app.root_path, 'static/post_pics', picture_fn)
#    #output_size = (500)
#    i = Image.open(form_picture)
#    #width, height = i.size
#    #i.thumbnail(output_size)
#    i.save(picture_path)
#    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
