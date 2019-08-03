from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
#from flask_wtf.file import FileField, FileAllowed

class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	#picture = FileField('Upload Image (Optional)', validators=[FileAllowed(['jpg','png','jpeg'])])
	submit = SubmitField('Post')
