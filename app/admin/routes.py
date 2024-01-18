from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app.admin import bp

@bp.route('/')
def index():
    return 'This is The Admin Blueprint'

@bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role_id == 3: 
        return render_template("admin/index.html")
    return redirect(url_for("main.index"))

@bp.route('fonts/view/all')
@login_required
def viewAllFonts():
    if current_user.role_id == 3: 
        return "You want to view all the fonts and you're an admin."
    return redirect(url_for("main.index"))