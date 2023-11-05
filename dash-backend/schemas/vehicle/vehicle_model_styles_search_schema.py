from marshmallow import fields, Schema


class VehicleModelStylesSearchSchema(Schema):
    filter_search = fields.String(required=False)
    filter_brand_id = fields.Integer(required=False)
    filter_model_id = fields.Integer(required=False)
    filter_year_model_id = fields.Integer(required=False)
    filter_model_style_id = fields.Integer(required=False)
    filter_model_style_color_code = fields.String(required=False)
    filter_body_id = fields.Integer(required=False)
    filter_offset = fields.Int(required=True, default=0)
    filter_limit = fields.Int(required=True, default=100)
    filter_price_from = fields.Float(required=False)
    filter_price_to = fields.Float(required=False)

vehicle_model_style_search_schema = VehicleModelStylesSearchSchema()
vehicle_model_style_searchs_schema = VehicleModelStylesSearchSchema(many=True)
