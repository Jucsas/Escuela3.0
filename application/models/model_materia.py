import web
import config

db = config.db


def get_all_materia():
    try:
        return db.select('materia')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_materia(id_materia):
    try:
        return db.select('materia', where='id_materia=$id_materia', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_materia(id_materia):
    try:
        return db.delete('materia', where='id_materia=$id_materia', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_materia(nombre,periodo,username):
    try:
        return db.insert('materia',nombre=nombre,
        periodo=periodo,
        username=username)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_materia(id_materia,nombre,periodo,username):
    try:
        return db.update('materia',id_materia=id_materia,
        nombre=nombre,
        periodo=periodo,
        username=username,
                  where='id_materia=$id_materia',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
