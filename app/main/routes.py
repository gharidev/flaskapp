from flask import render_template, request, Blueprint
from app.models import Post

main = Blueprint('main', __name__)

@main.route("/home")
@main.route("/")
def home():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template("index.html", home_active='active', posts=posts)


@main.route("/contactus")
def contactus():
    return render_template("contactus.html",title='Contact Us', contactus_active='active')

@main.route("/aboutus")
def aboutus():
    return render_template("aboutus.html",title='About Us', aboutus_active='active')