from flask import render_template, redirect, request, url_for, flash, abort
from util import app, db
from util.models import User
from util.forms import SwearForm, CreditForm, SearchForm
from datetime import datetime, timedelta
import time

@app.route('/admin/<int:page_num>')
def admin(page_num):
    threads = User.query.paginate(per_page=10, page=page_num, error_out=True) 
    return render_template('admin.html', threads=threads)

@app.route('/delete/<int:id>/<int:page_num>')
def delete(id,page_num):
    columndel = User.query.get_or_404(id)
    try:
        db.session.delete(columndel)
        db.session.commit()
        return redirect(url_for('admin', page_num=page_num))
    except:
        return "error delete"

@app.route('/approve/<int:id>/<data>/<int:page_num>')
def approve(id,data,page_num):
    columnapp = User.query.get_or_404(id)
    columnapp.done = 1
    columnapp.time = str(datetime.now())
    db.session.commit()
    time.sleep(1.5)
    return redirect(url_for('mycredit', data=data, page_num=page_num))

@app.route('/disapprove/<int:id>/<data>/<int:page_num>')
def disapprove(id,data,page_num):
    columnapp = User.query.get_or_404(id)
    columnapp.done = 2
    columnapp.time = str(datetime.now())
    db.session.commit()
    time.sleep(0.5)
    return redirect(url_for('mycredit', data=data, page_num=page_num))


@app.route('/')
def welcome():
    db.create_all()
    return render_template('welcome.html')

@app.route('/swear',methods=['GET','POST'])
def swear():
    form = SwearForm()
    if form.validate_on_submit():
        ans = User(wallet=form.wallet.data, swear=form.swear.data, credit=form.credit.data, val = form.val.data, date= str(datetime.now()), time='0',done=0)
        db.session.add(ans)
        db.session.commit()
        time.sleep(1.5)
        return redirect(url_for('myswear', data=form.wallet.data, page_num=1))
    return render_template('swear.html',form=form)

@app.route('/credit',methods=['GET','POST'])
def credit():
    form = CreditForm()
    if form.validate_on_submit():
        return redirect(url_for('mycredit', data = form.wallet.data, page_num = 1))
    return render_template('credit.html',form=form)

@app.route('/mycredit/<data>/<int:page_num>',methods=['GET','POST'])
def mycredit(data, page_num):
    qry = db.session.query(User).filter_by(credit=data)
    threads = qry.paginate(per_page=5, page=page_num, error_out=True)
    return render_template('mycredit.html', data=data,threads=threads)


@app.route('/search',methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('myswear', data = form.wallet.data, page_num = 1))
    return render_template('search.html',form=form)

@app.route('/myswear/<data>/<int:page_num>',methods=['GET','POST'])
def myswear(data,page_num):
    qry = db.session.query(User).filter_by(wallet=data)
    threads = qry.paginate(per_page=5, page=page_num, error_out=True)
    return render_template('myswear.html', data=data,threads=threads)

if __name__ == '__main__':
    app.run(debug=True)
