from flask import jsonify
from flask_restful import Resource, reqparse

class OrganizationList(Resource):
    def get(self):
        return {
            "error_code": 0,
            "error_message": '',
            "list":[
                {
                    "id": 1,
                    "name": "Oakridge Biz",                                
                    "parent_id": 0,
                    "children": [
                        {
                            "id": 2,
                            "name": "Hangzhou Site",
                            "address": "",
                            "country": "CN",
                            "zond_id": "Asia/ShangHai",
                            "parent_id": 1,
                        },
                        {
                            "id": 3,
                            "name": "US Site",
                            "address": "",
                            "country": "US",
                            "zond_id": "America/Los_Angeles",
                            "parent_id": 1,
                        }                        
                    ],
                    "customer_type": 1
                },
                {
                    "id": 100,
                    "name": "OutSpace Biz",                                
                    "parent_id": 0,
                    "children": [
                        {
                            "id": 101,
                            "name": "Mars Site",
                            "address": "",
                            "country": "CN",
                            "zond_id": "Asia/ShangHai",
                            "parent_id": 100,
                        },
                        {
                            "id": 102,
                            "name": "Earth Site",
                            "address": "",
                            "country": "US",
                            "zond_id": "America/Los_Angeles",
                            "parent_id": 100,
                        }                        
                    ],
                    "customer_type": 2
                }                
            ]
        }
