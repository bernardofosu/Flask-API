class ApiFeatures:
    def __init__(self, collection, query_params):
        self.collection = collection
        self.query_params = query_params
        self.pipeline = []

    def filter(self):
        query_obj = {k: v for k, v in self.query_params.items() if k not in ['page', 'sort', 'limit', 'fields']}
        
        mongo_query = {}
        for key, value in query_obj.items():
            if '__' in key:
                field, operator = key.split('__')
                operator_map = {'gte': '$gte', 'gt': '$gt', 'lte': '$lte', 'lt': '$lt'}
                if operator in operator_map:
                    mongo_query[field] = {operator_map[operator]: float(value)}
            else:
                mongo_query[key] = value
        
        self.pipeline.append({'$match': mongo_query})
        return self

    def sort(self):
        sort_by = self.query_params.get('sort')
        if sort_by:
            sort_fields = [(field.lstrip('-'), -1 if field.startswith('-') else 1) for field in sort_by.split(',')]
            self.pipeline.append({'$sort': dict(sort_fields)})
        else:
            self.pipeline.append({'$sort': {'created_at': -1}})
        return self

    def limit_fields(self):
        fields = self.query_params.get('fields')
        if fields:
            field_list = fields.split(',')
            projection = {field: 1 for field in field_list}
            self.pipeline.append({'$project': projection})
        return self

    def paginate(self):
        page = int(self.query_params.get('page', 1))
        limit = int(self.query_params.get('limit', 100))
        skip = (page - 1) * limit

        self.pipeline.append({'$skip': skip})
        self.pipeline.append({'$limit': limit})
        return self

    def execute(self):
        return list(self.collection.aggregate(self.pipeline))
