from sru.routes import windows


app.router.add_route("POST", "/schtasks/query", schtasks.query)
app.router.add_route("POST", "/schtasks/edit", schtasks.edit)
app.router.add_route("POST", "/schtasks/control", schtasks.control)