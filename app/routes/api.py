from flask import Blueprint, request, redirect, jsonify, render_template, session
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    db = get_db()
    
    try:
        if request.method == 'POST':
            # get the data submitted through form
            data = request.form
            
            # create a new user
            newUser = User(
                username = data['username'],
                email = data['email'],
                password = data['password']
            )
            
            # save in the database
            db.add(newUser)
            db.commit()
            
            session.clear()
            session['user_id'] = newUser.id
            session['loggedIn'] = True
            #redirect user to dashboard after form is submitted
            return redirect('/dashboard')
    except:
        # insert failed, so send error to front end, and rollback
        db.rollback()
        message = 'Signup failed, try again'
        return render_template(
            'signup.html',
            message=message
            )
        
        
@bp.route('/users/logout', methods=['POST'])
def logout():
    #remove session variables
    if request.method=='POST':
        session.clear()
        return redirect('/')
    
    
@bp.route('/users/login', methods=['POST'])
def login():
    db = get_db()
    if request.method == 'POST':
        data = request.form
        try:
            user = db.query(User).filter(User.email == data['email']).one()
        except:
            message = "Email doesn't exist"
            return render_template(
                'login.html',
                message=message
                ) 
        if user.verify_password(data['password']) == False:
            message = 'Incorrect Password'
            return render_template(
                'login.html',
                message=message
                ) 
        session.clear()
        session['user_id'] = user.id
        session['loggedIn'] = True
        
        return redirect('/dashboard')