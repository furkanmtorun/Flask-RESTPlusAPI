from flask import Flask
from flask_restplus import Api, Resource, fields, reqparse

app = Flask(__name__)
# API Configs
api = Api(app, version="0.1", title="People API with Flask-RESTPlus", description="A quite simple API to working with personal data") 

# Namespaces 
peopleCollection_api = api.namespace("peopleCollection", description="People Collection Operations")
person_api = api.namespace("person", description="Person Details Operations")
arg_api = api.namespace("argumentParser", description="Argument Parsing Operations")

# To parse the arguments
parser = reqparse.RequestParser()
parser.add_argument("page_number", type=int, default=1, required=False, help="Page number")
parser.add_argument("per_page", type=int, choices=[10, 20, 30, 40, 50], required=False, help="Page number")

# We define the parameters/schema for "people"
people_model = api.model("people", 
                {
                    "id": fields.Integer(description="ID Number", example=123456798, readonly=True),
                    "name": fields.String(description="Full name", example="Richard Hendricks", required=True, min=5),
                    "email": fields.String(description="Email Adress", example="richardhendricks@piedpier.com", required=True, min=10),
                    "github": fields.String(description="Github username", example="richardhendricks"),
                    "twitter": fields.String(description="Twitter username", example="richardhendricks"),
                    "country": fields.String(description="Country", example="USA")
                }
            )

# Initial data for list of people
peopleList = [
        {
            "id": 1,
            "name": "Furkan Torun",
            "email": "furkanmtorun@gmail.com",
            "github": "furkanmtorun",
            "twitter": "furkanmtorun",
            "country": "Turkey"
        }
    ]

# Create a Flask page
@app.route("/")
def about():
    return """<br><br><center>Hey! 
    <br> I am <b>Furkan Torun</b>. 
    <br> email: <a href="mailto:furkanmtorun@gmail.com">furkanmtorun@gmail.com</a>
    <br> github: <a href="http://github.com/furkanmtorun">@furkanmtorun</a>
    <br> twitter: <a href="http://twitter.com/furkanmtorun">@furkanmtorun</a>
    <br><br><hr><br> <i>* I have just tried to create a quite simple RESTful API and prepare a Turkish documentation to build it from scratch. </i>
    <br><br> Codes and Turkish documentation are available on <a href="http://github.com/furkanmtorun/Flask-RESTPlusAPI">http://github.com/furkanmtorun/Flask-RESTPlusAPI</a>.
    <br><br> Any feedback or suggestion will be appreciated!
    <br><br> <i>Thanks!</i>
    </center>"""

@peopleCollection_api.route("/")
class PeopleCollection(Resource):

    # @peopleCollection_api.marshal_with(people_model, envelope="peopleList")
    def get(self):
        return peopleList

    @peopleCollection_api.response(200, "Success")
    @peopleCollection_api.response(400, "Bad Request or Invalid Argument")
    @peopleCollection_api.expect(people_model)
    def post(self):
        new_person = api.payload
        new_person["id"] = max([temp_id["id"] for temp_id in peopleList]) + 1 
        peopleList.append(new_person)
        return new_person

@person_api.route("/<int:id>")
class PersonByID(Resource):

    @person_api.response(200, "Success")
    @person_api.response(404, "No results")
    @person_api.doc(params={"id":"ID number of the person"})
    def get(self, id):
        for person in peopleList:
            if person["id"] == id:
                return person
            else:
                return "The person with and ID of {} is not found!".format(id)

    @person_api.response(200, "Success")
    @person_api.response(404, "No such an person ID")
    @person_api.doc(params={"id":"ID number of the person"})
    def delete(self, id):
        for i in range(len(peopleList)):
            if peopleList[i]["id"] == id:
                del peopleList[i]
                return "The person with and ID of {} has been deleted!".format(id)
            else:
                return "The person with and ID of {} is not found!".format(id)

    @person_api.response(200, "Success")
    @person_api.response(404, "Ooops! Something went wrong!")
    @person_api.expect(people_model)
    @person_api.doc(params={"id":"ID number of the person"})
    def put(self, id):
        for person in peopleList:
            if person["id"] == id:
                person.update(api.payload)
                person["id"] = id 
                return person
            else:
                return "The person with and ID of {} is not found!".format(id)

@person_api.route("/<string:email>")
class PersonByMail(Resource):

    @person_api.response(200, "Success")
    @person_api.response(404, "No results")
    @person_api.doc(params={"email":"Email address of the person"})
    def get(self, email):
        for person in peopleList:
            if person["email"] == email:
                return person
            else:
                return "The person with an email of {} is not found!".format(email)

@arg_api.route("/")
class argParser(Resource):
    
    @arg_api.expect(parser)
    def get(self):
        args = parser.parse_args()
        page_number = args["page_number"]
        per_page = args["per_page"]
        return "{} records are shown per page in the {}. page.".format(per_page, page_number)

if __name__ == "__main__":
    app.secret_key = "Flask-RESTPlusAPI"
    app.run(debug=True)