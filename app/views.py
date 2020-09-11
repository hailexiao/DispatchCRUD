from unicodedata import name
from alembic.config import main

from flask.helpers import flash
from sqlalchemy.orm import query
from app.auth.views import login
from flask import redirect, render_template, Blueprint, request, url_for
from flask_login import current_user, login_required

from . import db

from .forms import CompanyForm
from .models import Company

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    companies = Company.query.all()
    return render_template('index.html', companies=companies)

@main_blueprint.route('/companies')
def search_companies():
    field = request.args.get('field')
    value = request.args.get('value')
    print(f'field: {field}, value: {value}')
    field_to_filter = {
        'name': Company.query.filter(Company.name.like(f'%{value}%')).all,
        'industry': Company.query.filter(Company.industry.like(f'%{value}%')).all,
        'city': Company.query.filter(Company.city.like(f'%{value}%')).all,
        'state': Company.query.filter(Company.state.like(f'%{value}%')).all,
        'country': Company.query.filter(Company.country.like(f'%{value}%')).all,
        'phone': Company.query.filter(Company.phone.like(f'{value}%')).all,
        'max_revenue': Company.query.filter(Company.revenue <= value).all,
        'min_revenue': Company.query.filter(Company.revenue >= value).all
    }
    filter = field_to_filter.get(field, None)
    if filter is not None:
        companies = filter()
    else:
        companies = Company.query.all()
        flash('Cannot search by this field!', 'warning')
    return render_template('index.html', companies=companies, is_search=True)

@main_blueprint.route('/company/<int:id>', methods=['GET'])
def view_company(id):
    company = Company.query.get_or_404(id)

    return render_template('company.html', company=company)

@main_blueprint.route('/companies/add', methods=['GET', 'POST'])
@login_required
def add_company():
    form = CompanyForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            company = Company(
                name=form.name.data,
                industry=form.industry.data,
                city=form.city.data,
                state=form.state.data,
                country=form.country.data,
                phone=form.phone.data,
                revenue=form.revenue.data,
                notes=form.notes.data
            )
            try:
                db.session.add(company)
                db.session.commit()
                flash("Company successfully added!", "success")
                return redirect(url_for('main.index'))
            except Exception as e:
                print(e)
                db.session.rollback()
                flash('Unable to add company!', 'danger')
    return render_template(
        'add_company.html',
        method="post",
        add_company=True,
        title="Add Company",
        form=form
        )

@main_blueprint.route('/company/<int:id>', methods=['GET', 'PUT'])
@login_required
def edit_company(id):
    company = Company.query.get_or_404(id)
    form = CompanyForm(obj=company)
    if request.method == 'GET':
        return render_template(
            'add_company.html',
            method="put",
            add_company=False,
            company=company,
            form=form,
            title="Edit Company"
            )
    elif form.validate_on_submit():
        company.name = form.name.data
        company.industry = form.industry.data
        company.city = form.city.data
        company.state = form.state.data
        company.country = form.country.data
        company.phone = form.country.data
        company.revenue = form.revenue.data
        company.notes = form.notes.data
        try:
            db.session.commit()
            flash("Company successfully edited!", "success")
            return redirect(url_for('main.index'))
        except:
            flash("Unable to edit company!", "danger")

@main_blueprint.route('/company/<int:id>/delete', methods=['GET', 'DELETE'])
@login_required
def delete_company(id):
    company = Company.query.get_or_404(id)
    db.session.delete(company)
    db.session.commit()
    return redirect(url_for('main.index'))
