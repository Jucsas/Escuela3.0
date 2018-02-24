import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_materia, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_materia) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_materia, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_materia) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_materia, **k):
        message = None # Error message
        id_materia = config.check_secure_val(str(id_materia)) # HMAC id_materia validate
        result = config.model.get_materia(int(id_materia)) # search  id_materia
        result.id_materia = config.make_secure_val(str(result.id_materia)) # apply HMAC for id_materia
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_materia, **k):
        form = config.web.input() # get form data
        form['id_materia'] = config.check_secure_val(str(form['id_materia'])) # HMAC id_materia validate
        result = config.model.delete_materia(form['id_materia']) # get materia data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_materia = config.check_secure_val(str(id_materia))  # HMAC user validate
            id_materia = config.check_secure_val(str(id_materia))  # HMAC user validate
            result = config.model.get_materia(int(id_materia)) # get id_materia data
            result.id_materia = config.make_secure_val(str(result.id_materia)) # apply HMAC to id_materia
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/materia') # render materia delete.html 
