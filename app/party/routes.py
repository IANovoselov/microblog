from flask import current_app
from flask import render_template, url_for, request
from flask_login import current_user, login_required

from app.party import bp


@bp.route('/parties',  methods=['GET', 'POST'])
@login_required
def parties():

    # form = PostForm()
    # if form.validate_on_submit():
    #     isReliable, textBytesFound, details = cld2.detect(form.post.data)
    #     if not details or details[0][1] == 'un':
    #         language = ''
    #     else:
    #         language = details[0][1]
    #     post = Post(body=form.post.data, author=current_user, language=language)
    #     db.session.add(post)
    #     db.session.commit()
    #     flash('Your post is now live!')
    #     return redirect(url_for('main.index'))
    #
    # if request.args.get('del_post'):
    #     del_post = request.args.get('del_post')
    #     post = Post.query.filter_by(id=int(del_post)).first()
    #     if post:
    #         post.delete_post()
    #         flash('Пост удален')

    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page=page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('main.index', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) if posts.has_prev else None
    return render_template('index.html', title='Home', form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url, page=page)
