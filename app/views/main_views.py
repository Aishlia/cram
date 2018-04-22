# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import Blueprint, redirect, render_template
from flask import request, url_for
from flask_user import current_user, login_required, roles_required

from app import db
from app.models.user_models import UserProfileForm, User, RegisteredClass, AddClassForm, DeleteClassForm

main_blueprint = Blueprint('main', __name__, template_folder='templates')

# The Home page is accessible to anyone
@main_blueprint.route('/')
def home_page():
    return render_template('main/home_page.html')


# The User page is accessible to authenticated users (users that have logged in)
@main_blueprint.route('/dashboard', methods=['GET', 'POST'])
@login_required  # Limits access to authenticated users
def member_page():
    # Initialize form
    form = AddClassForm(request.form)
    
    # Process valid POST
    if request.method == 'POST' and form.validate():

        print(form.name.data, form)

        single_class = RegisteredClass(name=form.name.data, user_id=current_user.id)
        db.session.add(single_class)
        db.session.commit()

        # db.session.commit()
        return redirect(url_for('main.member_page'))

    classes = RegisteredClass.query.filter_by(user_id=current_user.id).all()
    return render_template('main/dashboard.html', classes = classes, form=form)

@main_blueprint.route('/upload')
@login_required  # Limits access to authenticated users
def upload_page():
    return render_template('main/upload.html')


# The Admin page is accessible to users with the 'admin' role
@main_blueprint.route('/admin')
@roles_required('admin')  # Limits access to users with the 'admin' role
def admin_page():
    return render_template('main/admin_page.html')

# @main_blueprint.route("/deleteClass", methods=["POST"])
# @login_required
# def delete_class():
#     form = DeleteClassForm(request.form)
#     id_delete = request.form.get("id")
#     print(id_delete)
#     # classes = RegisteredClass.query.filter_by(id_delete).first()
#     # db.session.delete(classes)
#     # db.session.commit()
#     return render_template('main/dashboard.html',
#                            form=form)

@main_blueprint.route('/classes/<int:id>', methods=['DELETE'])
def delete_entry(id):
    classes = RegisteredClass.query.filter_by(id).first()
    db.session.delete(classes)
    db.session.commit()
    return render_template('main/dashboard.html')


@main_blueprint.route('/main/profile', methods=['GET', 'POST'])
@login_required
def user_profile_page():
    # Initialize form
    form = UserProfileForm(request.form, obj=current_user)

    # Process valid POST
    if request.method == 'POST' and form.validate():
        # Copy form fields to user_profile fields
        form.populate_obj(current_user)

        # Save user_profile
        db.session.commit()

        # Redirect to home page
        return redirect(url_for('main.home_page'))

    # Process GET or invalid POST
    return render_template('main/user_profile_page.html',
                           form=form)
