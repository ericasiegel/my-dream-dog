from django.shortcuts import render
from flask import Blueprint, request, redirect, jsonify, render_template, session, url_for
from app.models import User, Breed
from app.db import get_db
from app.utils.auth import login_required

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
            return redirect('/')
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
        return redirect('/dashboard')
    
    
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
    
@bp.route('/breeds', methods=['POST'])
@login_required
def saved_breeds():
    db = get_db()
    
    try:
        if request.method == 'POST':
            data = request.form

            # print(data['name'])
            newBreed = Breed(
                breed_id = data['id'],
                name = data['name'],
                user_id = session.get('user_id')
            )
            
            db.add(newBreed)
            db.commit()
            # breed_stats(data['id'])

            
            message = 'Breed Saved!'
            # return message
            return redirect('/dashboard')

           
    except:
        db.rollback()
        message = 'Breed Already Saved!'
        # return message
        return redirect('/')

@bp.route('/breeds/<int:id>', methods=['POST','DELETE'])
@login_required
def delete(id):
    db = get_db()
    # print(id)
    # id_delete = Breed.query.get(id)
    try:
        db.delete(db.query(Breed).filter(Breed.id == id).one())
        db.commit()
        return redirect('/dashboard')
    except:
        return('not deleted')