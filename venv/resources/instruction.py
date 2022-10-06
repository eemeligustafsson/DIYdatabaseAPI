from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.instruction import Instruction, instruction_list


class InstructionListResource(Resource):

    def get(self):

        data = []

        for instruction in instruction_list:
            data.append(instruction.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        
        name = data.get('name')
        description = data.get('description')
        steps = data.get('steps')
        tools = data.get('tools')
        cost = data.get('cost')
        duration = data.get('duration')

        instruction = Instruction(name=name,
                        description=description,
                        steps=steps,
                        tools=tools,
                        cost=cost,
                        duration=duration)

        instruction_list.append(instruction)


        return instruction, HTTPStatus.CREATED


class InstructionResource(Resource):

    def get(self, instruction_id):
        instruction = next((instruction for instruction in instruction_list if instruction.id == instruction_id), None)

        if instruction is None:
            return {'message': 'instruction not found'}, HTTPStatus.NOT_FOUND

        return instruction.data, HTTPStatus.OK

    def put(self, instruction_id):
        data = request.get_json()

        instruction = next((instruction for instruction in instruction_list if instruction.id == instruction_id), None)

        if instruction is None:
            return {'message': 'instruction not found'}, HTTPStatus.NOT_FOUND

        instruction.name = data['name']
        instruction.description = data['description']
        instruction.steps = data['steps']
        instruction.tools = data['tools']
        instruction.cost = data['cost']
        instruction.duration = data['duration']

        return instruction.data, HTTPStatus.OK
