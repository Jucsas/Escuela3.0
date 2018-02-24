import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass


    def GET(self, id_boleta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_boleta) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_boleta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_boleta) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_boleta, **k):
        message = None # Error message
        id_boleta = config.check_secure_val(str(id_boleta)) # HMAC id_boleta validate
        result = config.model.get_boleta(int(id_boleta)) # search  id_boleta
        result.id_boleta = config.make_secure_val(str(result.id_boleta)) # apply HMAC for id_boleta
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_boleta, **k):
        form = config.web.input() # get form data
        form['id_boleta'] = config.check_secure_val(str(form['id_boleta'])) # HMAC id_boleta validate
        result = config.model.delete_boleta(form['id_boleta']) # get boleta data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_boleta = config.check_secure_val(str(id_boleta))  # HMAC user validate
            id_boleta = config.check_secure_val(str(id_boleta))  # HMAC user validate
            result = config.model.get_boleta(int(id_boleta)) # get id_boleta data
            result.id_boleta = config.make_secure_val(str(result.id_boleta)) # apply HMAC to id_boleta
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/boleta') # render boleta delete.html 
