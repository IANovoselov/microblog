from flask import current_app, flash, redirect
from flask import render_template, url_for, request
from flask_login import current_user, login_required

from app.party import bp
from app.models import Party
from app.party.forms import PartyForm
from app import db


@bp.route('/parties',  methods=['GET', 'POST'])
@login_required
def parties():

    form = PartyForm()

    if not request.args.get('create') == 'True':
        form = None

    if form and form.validate_on_submit():
        party = Party(label=form.label.data, about=form.about.data, address=form.address.data,
                      owner_id=current_user.id)
        db.session.add(party)
        db.session.commit()
        flash('Вечеринка создана!')
        return redirect(url_for('party.parties'))

    page = request.args.get('page', 1, type=int)
    parties = Party.query.order_by(Party.id.desc()).paginate(
        page=page, per_page=current_app.config['PARTY_PER_PAGE'], error_out=False)
    next_url = url_for('party.parties', page=parties.next_num) if parties.has_next else None
    prev_url = url_for('party.parties', page=parties.prev_num) if parties.has_prev else None
    return render_template('parties.html', title='Вечеринки',
                           parties=parties.items, next_url=next_url,
                           prev_url=prev_url, page=page, form=form)
