import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass


    def GET(self, id_materia, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_materia) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_materia, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_materia) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_materia, **k):
        message = None # Error message
        id_materia = config.check_secure_val(str(id_materia)) # HMAC id_materia validate
        result = config.model.get_materia(int(id_materia)) # search for the id_materia
        result.id_materia = config.make_secure_val(str(result.id_materia)) # apply HMAC for id_materia
        return config.render.edit(result, message) # render materia edit.html

    @staticmethod
    def POST_EDIT(id_materia, **k):
        form = config.web.input()  # get form data
        form['id_materia'] = config.check_secure_val(str(form['id_materia'])) # HMAC id_materia validate
        # edit user with new data
        result = config.model.edit_materia(
            form['id_materia'],form['nombre'],form['periodo'],form['username'],
        )
        if result == None: # Error on udpate data
            id_materia = config.check_secure_val(str(id_materia)) # validate HMAC id_materia
            result = config.model.get_materia(int(id_materia)) # search for id_materia data
            result.id_materia = config.make_secure_val(str(result.id_materia)) # apply HMAC to id_materia
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/materia') # render materia index.html
