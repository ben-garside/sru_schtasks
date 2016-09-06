from . import routes

def setup(app):
    app.router.add_route("POST", "/schtasks/query", routes.query)
    app.router.add_route("POST", "/schtasks/edit", routes.edit)
    app.router.add_route("POST", "/schtasks/control", routes.control)