import web
import config

db = config.db


def get_all_boleta():
    try:
        return db.select('boleta')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_boleta(id_boleta):
    try:
        return db.select('boleta', where='id_boleta=$id_boleta', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_boleta(id_boleta):
    try:
        return db.delete('boleta', where='id_boleta=$id_boleta', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None

#if $users.username==$users.username:
def insert_boleta(calificacion,username):
    try:
        return db.insert('boleta',calificacion=calificacion,
            username=username)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None
#elif: 
 #   raise config.web.seeother('/logout')

def edit_boleta(id_boleta,calificacion,username):
    try:
        return db.update('boleta',id_boleta=id_boleta,
calificacion=calificacion,
username=username,
                  where='id_boleta=$id_boleta',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
