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
        return '', 204