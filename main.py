from flask import Flask, render_template, request, redirect, send_file
from extractors.wanted import Wanted
from extractors.berlin import extract_berlin_jobs
from extractors.web3 import extract_web3_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html", name="nico")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        wanted = Wanted()
        content = wanted.get_pages(keyword)
        jobs = wanted.scrape_page(content) + extract_berlin_jobs(keyword) + extract_web3_jobs(keyword)
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run("127.0.0.1", debug=True)