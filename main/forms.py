from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CreateListForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Create List", render_kw={"class": "cssbuttons-io"})
