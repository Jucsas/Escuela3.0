import web
import config
import json


class Api_boleta:
    def get(self, id_boleta):
        try:
            # http://0.0.0.0:8080/api_boleta?user_hash=12345&action=get
            if id_boleta is None:
                result = config.model.get_all_boleta()
                boleta_json = []
                for row in result:
                    tmp = dict(row)
                    boleta_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(boleta_json)
            else:
                # http://0.0.0.0:8080/api_boleta?user_hash=12345&action=get&id_boleta=1
                result = config.model.get_boleta(int(id_boleta))
                boleta_json = []
                boleta_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(boleta_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            boleta_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(boleta_json)

# http://0.0.0.0:8080/api_boleta?user_hash=12345&action=put&id_boleta=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, calificacion,username):
        try:
            config.model.insert_boleta(calificacion,username)
            boleta_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(boleta_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_boleta?user_hash=12345&action=delete&id_boleta=1
    def delete(self, id_boleta):
        try:
            config.model.delete_boleta(id_boleta)
            boleta_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(boleta_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_boleta?user_hash=12345&action=update&id_boleta=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_boleta, calificacion,username):
        try:
            config.model.edit_boleta(id_boleta,calificacion,username)
            boleta_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(boleta_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            boleta_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(boleta_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_boleta=None,
            calificacion=None,
            username=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_boleta=user_data.id_boleta
            calificacion=user_data.calificacion
            username=user_data.username
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_boleta)
                elif action == 'put':
                    return self.put(calificacion,username)
                elif action == 'delete':
                    return self.delete(id_boleta)
                elif action == 'update':
                    return self.update(id_boleta, calificacion,username)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
