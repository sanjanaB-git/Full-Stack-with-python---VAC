from flask import Flask, render_template, request, redirect

from database import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")




@app.route("/create")
def create():
    return render_template("ticket_creation.html")


@app.route("/create_ticket", methods=["POST"])
def create_ticket_route():

    ticket = {
        "name": request.form["name"],
        "email": request.form["email"],
        "title": request.form["title"],
        "category": request.form["category"],
        "description": request.form["description"],
        "priority": "Low",
        "status": "Open",
        "assigned_to": "Not Assigned"
    }

    create_ticket(ticket)

    return redirect("/tickets")




@app.route("/tickets")
def tickets():

    ticket_list = get_all_tickets()

    return render_template(
        "tickets.html",
        tickets=ticket_list
    )




@app.route("/assignment")
def assignment():
    return render_template("ticket_assignment.html")


@app.route("/assign_ticket", methods=["POST"])
def assign():

    title = request.form["title"]
    assigned = request.form["assigned"]

    assign_ticket(title, assigned)

    return redirect("/reports")




@app.route("/priority")
def priority():
    return render_template("priority.html")


@app.route("/update_priority", methods=["POST"])
def priority_update():

    title = request.form["title"]
    priority = request.form["priority"]

    update_priority(title, priority)

    return redirect("/reports")




@app.route("/status")
def status():
    return render_template("status.html")


@app.route("/update_status", methods=["POST"])
def status_update():

    title = request.form["title"]
    status = request.form["status"]

    update_status(title, status)

    return redirect("/reports")




@app.route("/knowledge")
def knowledge():
    return render_template("knowledge.html")




@app.route("/reports")
def reports():

    ticket_list = get_all_tickets()

    return render_template(
        "reports.html",
        tickets=ticket_list
    )


if __name__ == "__main__":
    app.run(debug=True)