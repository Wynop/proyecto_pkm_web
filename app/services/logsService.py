from flask import redirect, render_template, session, url_for


class LogsService:
    
    @staticmethod
    def logIn(name):
        name = name.strip()
        if len(name) < 3 or len(name) > 15:
            return [False, "The name must be between 3 and 15 characters long."]
        session["name"] = name
        return [True, 200]
    
    @staticmethod
    def logOut():
        session.clear()
                