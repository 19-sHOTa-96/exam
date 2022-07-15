## WEBSITE LINK -->| http://shottt.pythonanywhere.com |<--


from flask import Flask, render_template, request, redirect, url_for
from hashids import Hashids
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a7135969a1f3466fb05f0c5d95fa7b4f'
hashids = Hashids(min_length=6)

@app.route('/', methods=['POST', 'GET'])
def home():
	connection = sqlite3.connect("urls.db")
	cursor = connection.cursor()

	default = "Enter URL"

	if request.method == 'POST':
		url = request.form.get('url')
		url_base = cursor.execute("INSERT INTO urls (url) VALUES(?)", (url,))

		connection.commit()
		connection.close()

		uid = url_base.lastrowid
		h_id = hashids.encode(uid)

		default = request.host_url + h_id

	return render_template('index.html', default=default)


@app.route('/<id>')
def short_url(id):
	connection = sqlite3.connect("urls.db")
	cursor = connection.cursor()
	uid = hashids.decode(id)

	if uid:
		uid = uid[0]
		url_base = cursor.execute("SELECT url FROM urls WHERE id = (?)", (uid,)).fetchone()
		data = url_base[0]

		connection.commit()
		connection.close()

		return redirect(data)

	else:
		redirect(url_for('home'))	





if __name__ == "__main__":
	app.run(debug=True)