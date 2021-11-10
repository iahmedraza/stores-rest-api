from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                type=str,
                required = True,
                help = "This field cannot be left blank!"
            ) 
    parser.add_argument("password",
                type=str,
                required = True,
                help = "This field cannot be left blank!"
            ) 
        
    def post(self):
        
        data =  UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "Username already exists"}, 400

        new_user = UserModel(data["username"], data["password"])
        new_user.add_new_user()

        return {"message": "User created sucessfully."}, 201

