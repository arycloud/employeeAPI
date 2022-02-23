from flask import Blueprint
from flask import request, jsonify, abort
from app.models import Employee

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/employees', methods=['GET', 'POST'])
def get_all_employees():
    if request.method == "POST":
        email = str(request.data.get('email', ''))
        full_name = str(request.data.get('full_name', ''))
        address = str(request.data.get('address', ''))
        if email:
            employee = Employee(email=email, full_name=full_name,
                                address=address)
            employee.save()
            response = jsonify({
                'id': employee.id,
                'email': employee.email,
                'address': employee.address
            })
            response.status_code = 201
            return response
    else:
        # GET
        employees = Employee.get_all()
        results = []

        for employee in employees:
            obj = {
                'id': employee.id,
                'email': employee.email,
                'address': employee.address
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response


@api_blueprint.route('/employee/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def employee_manipulation(id, **kwargs):
    # retrieve an employee using it's ID
    employee = Employee.query.filter_by(id=id).first()
    if not employee:
        # Raise an HTTPException with a 404 not found status code
        abort(404)

    if request.method == 'DELETE':
        employee.delete()
        return {
                   "message": "employee {} deleted successfully".format(employee.full_name)
               }, 200

    elif request.method == 'PUT':
        email = str(request.data.get('email', ''))
        full_name = str(request.data.get('full_name', ''))
        address = str(request.data.get('address', ''))
        employee.email = email
        employee.full_name = full_name
        employee.address = address
        employee.save()
        response = jsonify({
            'id': employee.id,
            'email': employee.email,
            'full_name': employee.full_name,
            'address': employee.address
        })
        response.status_code = 200
        return response
    else:
        # GET
        response = jsonify({
            'id': employee.id,
            'email': employee.email,
            'full_name': employee.full_name,
            'address': employee.address
        })
        response.status_code = 200
        return response
