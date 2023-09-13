from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired

class SwearForm(FlaskForm):
    wallet = StringField('我的錢包', validators=[DataRequired()])
    swear = StringField('發誓內容',validators=[DataRequired()])
    credit = StringField('保證人',validators=[DataRequired()])
    val = IntegerField('發誓金額',validators=[DataRequired()])
    submit = SubmitField('確認發誓')

class CreditForm(FlaskForm):
    wallet = StringField('我的錢包', validators=[DataRequired()])
    submit = SubmitField('確認')

class SearchForm(FlaskForm):
    wallet = StringField('錢包地址', validators=[DataRequired()])
    submit = SubmitField('確認')



