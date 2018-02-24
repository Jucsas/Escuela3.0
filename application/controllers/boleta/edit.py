import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    def GET(self, id_boleta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_boleta) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_boleta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_boleta) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_boleta, **k):
        message = None # Error message
        id_boleta = config.check_secure_val(str(id_boleta)) # HMAC id_boleta validate
        result = config.model.get_boleta(int(id_boleta)) # search for the id_boleta
        result.id_boleta = config.make_secure_val(str(result.id_boleta)) # apply HMAC for id_boleta
        return config.render.edit(result, message) # render boleta edit.html

    @staticmethod
    def POST_EDIT(id_boleta, **k):
        form = config.web.input()  # get form data
        form['id_boleta'] = config.check_secure_val(str(form['id_boleta'])) # HMAC id_boleta validate
        # edit user with new data
        result = config.model.edit_boleta(
            form['id_boleta'],form['calificacion'],form['username'],
        )
        if result == None: # Error on udpate data
            id_boleta = config.check_secure_val(str(id_boleta)) # validate HMAC id_boleta
            result = config.model.get_boleta(int(id_boleta)) # search for id_boleta data
            result.id_boleta = config.make_secure_val(str(result.id_boleta)) # apply HMAC to id_boleta
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/boleta') # render boleta index.html
