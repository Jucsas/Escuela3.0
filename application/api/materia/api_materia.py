import web
import config
import json


class Api_materia:
    def get(self, id_materia):
        try:
            # http://0.0.0.0:8080/api_materia?user_hash=12345&action=get
            if id_materia is None:
                result = config.model.get_all_materia()
                materia_json = []
                for row in result:
                    tmp = dict(row)
                    materia_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(materia_json)
            else:
                # http://0.0.0.0:8080/api_materia?user_hash=12345&action=get&id_materia=1
                result = config.model.get_materia(int(id_materia))
                materia_json = []
                materia_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(materia_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            materia_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(materia_json)

# http://0.0.0.0:8080/api_materia?user_hash=12345&action=put&id_materia=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,periodo,username):
        try:
            config.model.insert_materia(nombre,periodo,username)
            materia_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(materia_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_materia?user_hash=12345&action=delete&id_materia=1
    def delete(self, id_materia):
        try:
            config.model.delete_materia(id_materia)
            materia_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(materia_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_materia?user_hash=12345&action=update&id_materia=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_materia, nombre,periodo,username):
        try:
            config.model.edit_materia(id_materia,nombre,periodo,username)
            materia_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(materia_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            materia_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(materia_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_materia=None,
            nombre=None,
            periodo=None,
            username=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_materia=user_data.id_materia
            nombre=user_data.nombre
            periodo=user_data.periodo
            username=user_data.username
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_materia)
                elif action == 'put':
                    return self.put(nombre,periodo,username)
                elif action == 'delete':
                    return self.delete(id_materia)
                elif action == 'update':
                    return self.update(id_materia, nombre,periodo,username)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
