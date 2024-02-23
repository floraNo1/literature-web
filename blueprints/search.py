from flask import Blueprint, request, render_template
from models import SearchModel

# from decorators import login_required

bp = Blueprint("search", __name__, url_prefix="/")


@bp.route("/")
def index():
    return render_template("index1.html")


@bp.route("/more")
def index1():
    return render_template("index2.html")


@bp.route("/team")
def detail():
    return render_template("team_detail.html")


@bp.route("/search_Doc",methods=['post', 'get'])
def search1():
    content = request.args.get("q")
    if content is None:
        content = " "

    quotes = SearchModel.query.filter(
        SearchModel.Article_Title.like("%" + content + "%") if content is not None else "").all()

    return render_template('1.html', quotes=quotes)


@bp.route("/search_Author")
def search2():
    content = request.args.get("q")

    if content is None:
        content = " "

    content = ' ' + content
    quotes = SearchModel.query.filter(
        SearchModel.Authors.like("%" + content + "%") if content is not None else "",
        SearchModel.Author_Full_Names.like("%" + content + "%") if content is not None else "").all()

    return render_template('2.html', quotes=quotes, author=content)
