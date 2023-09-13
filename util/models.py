from util import db 
from datetime import datetime
class User(db.Model):
    __tablename__ = 'users'
    
    # columns
    pid       = db.Column(db.Integer, primary_key = True)
    wallet    = db.Column(db.String(42), nullable=False)
    swear     = db.Column(db.String(64), nullable=False)
    credit    = db.Column(db.String(42), nullable=False)
    val    = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(64), nullable=False)
    time = db.Column(db.String(64), nullable=False)
    done    = db.Column(db.Integer)
    
    def __init__(self, wallet, swear, credit, val, date, time, done):
        """初始化"""
        self.wallet = wallet
        self.swear = swear
        self.credit = credit
        self.val = val
        self.date=date
        self.time = time
        self.done = done
    

