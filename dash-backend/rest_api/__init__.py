import rest_api.swagger as swagger

from rest_api.endpoints.auth import auth_ctrl
from rest_api.endpoints.dealer.dealer import dealer_ctrl
from rest_api.endpoints.dealer.dealer_request import dealer_request_ctrl
from rest_api.endpoints.dealer.dealer_scheduler import dealer_scheduler_ctrl
from rest_api.endpoints.locales import locale_ctrl
from rest_api.endpoints.permissions import permission_ctrl
from rest_api.endpoints.roles import role_ctrl
from rest_api.endpoints.vehicle import *
from rest_api.endpoints.core_provider.city import city_ctrl
from rest_api.endpoints.core_provider.country import country_ctrl
from rest_api.endpoints.core_provider.state import state_ctrl
from rest_api.endpoints.core_provider.zip_code import zip_code_ctrl
from rest_api.endpoints.vehicle.payment import vehicle_payment_ctrl
from rest_api.endpoints.vehicle.vehicle_feature import vehicle_feature_ctrl

error_responses = {
    "400": {
        "description": "Bad Requests",
        "content": {"application/json": {"schema": "ExceptionResponseSchema"}}
    },
    "401": {
        "description": "Not Authorized",
        "content": {"application/json": {"schema": "ExceptionResponseSchema"}}
    },
    "5XX": {
        "description": "Error From Server",
        "content": {"application/json": {"schema": "ExceptionResponseSchema"}}
    }
}


def init_swagger_response(schema_name):
    return {**{
        "200": {
            "content": {
                "application/json": {
                    "schema": schema_name
                }
            }
        }
    }, **error_responses}


def init_app(app, spec):
    app.register_blueprint(auth_ctrl)
    app.register_blueprint(locale_ctrl)
    app.register_blueprint(permission_ctrl)
    app.register_blueprint(role_ctrl)
    app.register_blueprint(price_option_assignment_ctrl)
    app.register_blueprint(price_vehicle_assignment_ctrl)
    app.register_blueprint(price_vehicle_model_style_assignment_ctrl)
    app.register_blueprint(vehicle_ctrl)
    app.register_blueprint(vehicle_attribute_ctrl)
    app.register_blueprint(vehicle_attribute_value_ctrl)
    app.register_blueprint(vehicle_brand_ctrl)
    app.register_blueprint(vehicle_history_ctrl)
    app.register_blueprint(vehicle_model_ctrl)
    app.register_blueprint(vehicle_model_style_ctrl)
    app.register_blueprint(vehicle_model_style_attribute_ctrl)
    app.register_blueprint(vehicle_option_item_ctrl)
    app.register_blueprint(vehicle_status_ctrl)
    app.register_blueprint(vehicle_year_model_ctrl)
    app.register_blueprint(vehicle_year_model_attribute_ctrl)
    app.register_blueprint(vehicle_payment_ctrl)
    app.register_blueprint(city_ctrl)
    app.register_blueprint(country_ctrl)
    app.register_blueprint(state_ctrl)
    app.register_blueprint(zip_code_ctrl)
    app.register_blueprint(vehicle_feature_ctrl)
    app.register_blueprint(dealer_ctrl)
    app.register_blueprint(dealer_scheduler_ctrl)
    app.register_blueprint(dealer_request_ctrl)

    query_list_params = [
        {
            "name": "direction",
            "in": "query",
            "schema": {
                "type": "string",
                "enum": ["asc", "desc"],
                "default": "asc"
            },
            "required": "true"
        },
        {
            "name": "is_active",
            "in": "query",
            "schema": {
                "type": "boolean",
                "default": "true"
            },
            "required": "true"
        },
        {
            "name": "limit",
            "in": "query",
            "schema": {
                "type": "integer",
                "default": "100"
            },
            "required": "true"
        },
        {
            "name": "offset",
            "in": "query",
            "schema": {
                "type": "integer",
                "default": "0"
            },
            "required": "true"
        },
        {
            "name": "q",
            "in": "query",
            "schema": {
                "type": "string"
            },
            "required": "true",
            "default": ""
        },
        {
            "name": "sort",
            "in": "query",
            "schema": {
                "type": "boolean",
                "default": "true"
            },
            "required": "true"
        }
    ];

    spec.path(
        path=vehicle_attribute_ctrl.url_prefix,
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('VehicleAttributeSchema')
            ),
            post=dict(
                parameters=[
                    {
                        "name": "VehicleAttributeBody",
                        "in": "body",
                        "schema": "VehicleAttributeSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleAttributeSchema')
            )
        )
    )
    spec.path(
        path=vehicle_attribute_ctrl.url_prefix + '/{vehicle_attribute_id}',
        parameters=[{
            "name": "vehicle_attribute_id",
            "in": "path",
            "description": "VehicleAttributeId",
            "required": "true",
        }],
        operations=dict(
            put=dict(
                parameters=[
                    {
                        "name": "VehicleAttributeBody",
                        "in": "body",
                        "schema": "VehicleAttributeSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleAttributeSchema')
            ),
            get=dict(
                responses=init_swagger_response('VehicleAttributeSchema')
            ),
            delete=dict(
                responses=init_swagger_response('VehicleAttributeSchema')
            )
        )
    )

    # spec.path(
    #     path=price_option_assignment_ctrl.url_prefix,
    #     parameters=query_list_params,
    #     operations=dict(
    #         get=dict(
    #             responses=init_swagger_response('PriceOptionAssignmentSchema')
    #         )
    #     )
    # )
    #
    # spec.path(
    #     path=price_vehicle_assignment_ctrl.url_prefix,
    #     parameters=query_list_params,
    #     operations=dict(
    #         get=dict(
    #             responses=init_swagger_response('PriceVehicleAssignmentSchema')
    #         )
    #     )
    # )
    #
    # spec.path(
    #     path=price_vehicle_model_style_assignment_ctrl.url_prefix,
    #     parameters=query_list_params,
    #     operations=dict(
    #         get=dict(
    #             responses=init_swagger_response('PriceVehicleModelStyleAssignmentSchema')
    #         )
    #     )
    # )
    #
    # spec.path(
    #     path=vehicle_ctrl.url_prefix,
    #     parameters=query_list_params,
    #     operations=dict(
    #         get=dict(
    #             responses=init_swagger_response('VehicleSchema')
    #         )
    #     )
    # )
    #

    #
    # spec.path(
    #     path=vehicle_attribute_value_ctrl.url_prefix,
    #     parameters=query_list_params,
    #     operations=dict(
    #         get=dict(
    #             responses=init_swagger_response('VehicleAttributeValueSchema')
    #         )
    #     )
    # )

    spec.path(
        path=vehicle_brand_ctrl.url_prefix,
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('VehicleBrandSchema')
            ),
            post=dict(
                parameters=[
                    {
                        "name": "VehicleBrandBody",
                        "in": "body",
                        "schema": "VehicleBrandSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleBrandSchema')
            )
        )
    )

    spec.path(
        path=vehicle_brand_ctrl.url_prefix + '/{vehicle_brand_id}/vehicle_models',
        parameters=[{
            "name": "vehicle_brand_id",
            "in": "path",
            "description": "VehicleBrandId",
            "required": "true",
        }],
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('VehicleModelSchema')
            ),
        )
    )

    spec.path(
        path=vehicle_brand_ctrl.url_prefix + '/{vehicle_brand_id}',
        parameters=[{
            "name": "vehicle_brand_id",
            "in": "path",
            "description": "VehicleBrandId",
            "required": "true",
        }],
        operations=dict(
            put=dict(
                parameters=[
                    {
                        "name": "VehicleBrandBody",
                        "in": "body",
                        "schema": "VehicleBrandSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleBrandSchema')
            ),
            get=dict(
                responses=init_swagger_response('VehicleBrandSchema')
            ),
            delete=dict(
                responses=init_swagger_response('VehicleBrandSchema')
            )
        )
    )
    spec.path(
        path=vehicle_brand_ctrl.url_prefix + '/{vehicle_brand_id}/logo',
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "vehicle_brand_id",
                        "in": "path",
                        "description": "VehicleBrandId",
                        "required": "true",
                    },
                    {
                        "name": "VehicleBrandLogo",
                        "in": "formData",
                        "type": "file",
                        "description": "VehicleBrandLogo",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleBrandSchema')
            )
        )
    )

    spec.path(
        path=vehicle_model_ctrl.url_prefix,
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('VehicleModelSchema')
            ),
            post=dict(
                parameters=[
                    {
                        "name": "VehicleModelBody",
                        "in": "body",
                        "schema": "VehicleModelSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleModelSchema')
            )
        )
    )

    spec.path(
        path=vehicle_model_ctrl.url_prefix + '/{vehicle_model_id}/vehicle_year_models',
        parameters=[{
            "name": "vehicle_model_id",
            "in": "path",
            "description": "vehicleModelId",
            "required": "true",
        }],
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('VehicleYearModelSchema')
            ),
        )
    )

    spec.path(
        path=vehicle_model_ctrl.url_prefix + '/{vehicle_model_id}',
        parameters=[{
            "name": "vehicle_model_id",
            "in": "path",
            "description": "vehicleModelId",
            "required": "true",
        }],
        operations=dict(
            put=dict(
                parameters=[
                    {
                        "name": "VehicleModelBody",
                        "in": "body",
                        "schema": "VehicleModelSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleModelSchema')
            ),
            get=dict(
                responses=init_swagger_response('VehicleModelSchema')
            ),
            delete=dict(
                responses=init_swagger_response('VehicleModelSchema')
            )
        )
    )
    spec.path(
        path=vehicle_model_ctrl.url_prefix + '/{vehicle_model_id}/avatar',
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "vehicle_model_id",
                        "in": "path",
                        "description": "VehicleModelId",
                        "required": "true",
                    },
                    {
                        "name": "VehicleModelAvatar",
                        "in": "formData",
                        "type": "file",
                        "description": "VehicleModelAvatar",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleModelSchema')
            )
        )
    )

    spec.path(
        path=vehicle_year_model_ctrl.url_prefix,
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('VehicleYearModelSchema')
            ),
            post=dict(
                parameters=[
                    {
                        "name": "VehicleYearModelBody",
                        "in": "body",
                        "schema": "VehicleYearModelSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleYearModelSchema')
            )
        )
    )

    spec.path(
        path=vehicle_year_model_ctrl.url_prefix + '/{vehicle_year_model_id}/vehicle_model_styles',
        parameters=[{
            "name": "vehicle_year_model_id",
            "in": "path",
            "description": "vehicleYearModelId",
            "required": "true",
        }],
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('VehicleModelStyleSchema')
            ),
        )
    )

    spec.path(
        path=vehicle_year_model_ctrl.url_prefix + '/{vehicle_year_model_id}',
        parameters=[{
            "name": "vehicle_year_model_id",
            "in": "path",
            "description": "vehicleYearModelId",
            "required": "true",
        }],
        operations=dict(
            put=dict(
                parameters=[
                    {
                        "name": "VehicleYearModelBody",
                        "in": "body",
                        "schema": "VehicleYearModelSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleYearModelSchema')
            ),
            get=dict(
                responses=init_swagger_response('VehicleYearModelSchema')
            ),
            delete=dict(
                responses=init_swagger_response('VehicleYearModelSchema')
            )
        )
    )
    spec.path(
        path=vehicle_year_model_ctrl.url_prefix + '/{vehicle_year_model_id}/avatar',
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "vehicle_year_model_id",
                        "in": "path",
                        "description": "VehicleYearModelId",
                        "required": "true",
                    },
                    {
                        "name": "VehicleYearModelAvatar",
                        "in": "formData",
                        "type": "file",
                        "description": "VehicleYearModelAvatar",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleYearModelSchema')
            )
        )
    )

    spec.path(
        path=vehicle_year_model_ctrl.url_prefix + '/{vehicle_year_model_id}/cover',
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "vehicle_year_model_id",
                        "in": "path",
                        "description": "VehicleYearModelId",
                        "required": "true",
                    },
                    {
                        "name": "VehicleYearModelCover",
                        "in": "formData",
                        "type": "file",
                        "description": "VehicleYearModelCover",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleYearModelSchema')
            )
        )
    )

    spec.path(
        path=vehicle_year_model_ctrl.url_prefix + '/{vehicle_year_model_id}/introduction_video',
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "vehicle_year_model_id",
                        "in": "path",
                        "description": "VehicleYearModelId",
                        "required": "true",
                    },
                    {
                        "name": "VehicleYearModelIntroductionVideo",
                        "in": "formData",
                        "type": "file",
                        "description": "VehicleYearModelIntroductionVideo",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleYearModelSchema')
            )
        )
    )

    spec.path(
        path=vehicle_year_model_ctrl.url_prefix + '/{vehicle_year_model_id}/exterior',
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "vehicle_year_model_id",
                        "in": "path",
                        "description": "VehicleYearModelId",
                        "required": "true",
                    },
                    {
                        "name": "VehicleYearModelExterior",
                        "in": "formData",
                        "type": "file",
                        "description": "VehicleYearModelExterior",
                        "required": "true",
                    },
                    {
                        "name": "VehicleYearModelExterior2",
                        "in": "formData",
                        "type": "file",
                        "description": "VehicleYearModelExterior2",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleYearModelSchema')
            )
        )
    )

    spec.path(
        path=vehicle_year_model_ctrl.url_prefix + '/{vehicle_year_model_id}/interior',
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "vehicle_year_model_id",
                        "in": "path",
                        "description": "VehicleYearModelId",
                        "required": "true",
                    },
                    {
                        "name": "VehicleYearModelInterior",
                        "in": "formData",
                        "type": "file",
                        "description": "VehicleYearModelInterior",
                        "required": "true",
                    },
                    {
                        "name": "VehicleYearModelInterior2",
                        "in": "formData",
                        "type": "file",
                        "description": "VehicleYearModelInterior2",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleYearModelSchema')
            )
        )
    )

    spec.path(
        path=vehicle_year_model_ctrl.url_prefix + '/{vehicle_year_model_id}/attribute_values',
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "vehicle_year_model_id",
                        "in": "path",
                        "description": "VehicleYearModelId",
                        "required": "true",
                    },
                    {
                        "name": "VehicleAttributeValuesBody",
                        "in": "body",
                        "schema": "VehicleAttributeValueSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleYearModelSchema')
            )
        )
    )

    spec.path(
        path=vehicle_model_style_ctrl.url_prefix,
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('VehicleModelStyleSchema')
            ),
            post=dict(
                parameters=[
                    {
                        "name": "VehicleModelStyleBody",
                        "in": "body",
                        "schema": "VehicleModelStyleSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleModelStyleSchema')
            )
        )
    )
    spec.path(
        path=vehicle_model_style_ctrl.url_prefix + '/{vehicle_model_style_id}',
        parameters=[{
            "name": "vehicle_model_style_id",
            "in": "path",
            "description": "vehicleModelStyleId",
            "required": "true",
        }],
        operations=dict(
            put=dict(
                parameters=[
                    {
                        "name": "VehicleModelStyleBody",
                        "in": "body",
                        "schema": "VehicleModelStyleSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleModelStyleSchema')
            ),
            get=dict(
                responses=init_swagger_response('VehicleModelStyleSchema')
            ),
            delete=dict(
                responses=init_swagger_response('VehicleModelStyleSchema')
            )
        )
    )
    spec.path(
        path=vehicle_model_style_ctrl.url_prefix + '/{vehicle_model_style_id}/avatar',
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "vehicle_model_style_id",
                        "in": "path",
                        "description": "VehicleModelStyleId",
                        "required": "true",
                    },
                    {
                        "name": "VehicleModelStyleAvatar",
                        "in": "formData",
                        "type": "file",
                        "description": "VehicleModelStyleAvatar",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleModelStyleSchema')
            )
        )
    )

    spec.path(
        path=vehicle_model_style_ctrl.url_prefix + '/{vehicle_model_style_id}/cover',
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "vehicle_model_style_id",
                        "in": "path",
                        "description": "VehicleModelStyleId",
                        "required": "true",
                    },
                    {
                        "name": "VehicleModelStyleCover",
                        "in": "formData",
                        "type": "file",
                        "description": "VehicleModelStyleCover",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleModelStyleSchema')
            )
        )
    )

    spec.path(
        path=vehicle_model_style_ctrl.url_prefix + '/{vehicle_model_style_id}/introduction_video',
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "vehicle_model_style_id",
                        "in": "path",
                        "description": "VehicleModelStyleId",
                        "required": "true",
                    },
                    {
                        "name": "VehicleModelStyleIntroductionVideo",
                        "in": "formData",
                        "type": "file",
                        "description": "VehicleModelStyleIntroductionVideo",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleModelStyleSchema')
            )
        )
    )

    spec.path(
        path=vehicle_model_style_ctrl.url_prefix + '/{vehicle_model_style_id}/attribute_values',
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "vehicle_model_style_id",
                        "in": "path",
                        "description": "VehicleModelStyleId",
                        "required": "true",
                    },
                    {
                        "name": "VehicleAttributeValuesBody",
                        "in": "body",
                        "schema": "VehicleAttributeValueSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleModelStyleSchema')
            )
        )
    )

    spec.path(
        path=vehicle_model_style_ctrl.url_prefix + '/_search',
        operations=dict(
            get=dict(
                parameters=[
                    {
                        "name": "VehicleModelStylesSearch",
                        "in": "query",
                        "schema": "VehicleModelStylesSearchSchema"
                    }
                ],
                responses=init_swagger_response('VehicleModelStyleSchema')
            )
        )
    )

    spec.path(
        path=vehicle_ctrl.url_prefix + '/{vehicle_id}',
        operations=dict(
            get=dict(
                parameters=[
                    {
                        "name": "vehicle_id",
                        "in": "path",
                        "description": "VehicleId",
                        "required": "true",
                    },
                ],
                responses=init_swagger_response('VehicleSchema')
            )
        )
    )

    spec.path(
        path=vehicle_ctrl.url_prefix + '/_search',
        operations=dict(
            get=dict(
                parameters=[
                    {
                        "name": "VehicleSearch",
                        "in": "query",
                        "schema": "VehicleModelStylesSearchSchema"
                    }
                ],
                responses=init_swagger_response('VehicleSchema')
            )
        )
    )

    spec.path(
        path=vehicle_option_item_ctrl.url_prefix + '/{vehicle_option_item_id}/avatar',
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "vehicle_option_item_id",
                        "in": "path",
                        "description": "vehicle_option_item_id",
                        "required": "true",
                    },
                    {
                        "name": "VehicleOptionItemAvatar",
                        "in": "formData",
                        "type": "file",
                        "description": "VehicleOptionItemAvatar",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('VehicleOptionItemSchema')
            )
        )
    )

    spec.path(
        path=country_ctrl.url_prefix,
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('CountrySchema')
            )
        )
    )

    spec.path(
        path=state_ctrl.url_prefix,
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('StateSchema')
            )
        )
    )

    spec.path(
        path=state_ctrl.url_prefix + '/{country_id}',
        parameters=[{
            "name": "country_id",
            "in": "path",
            "description": "country_id",
            "required": "true",
        }],
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('StateSchema')
            )
        )
    )

    spec.path(
        path=city_ctrl.url_prefix,
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('CitySchema')
            )
        )
    )

    spec.path(
        path=city_ctrl.url_prefix + '/{state_id}',
        parameters=[{
            "name": "state_id",
            "in": "path",
            "description": "state_id",
            "required": "true",
        }],
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('CitySchema')
            )
        )
    )

    spec.path(
        path=zip_code_ctrl.url_prefix + '/{zip_code}',
        parameters=[{
            "name": "zip_code",
            "in": "path",
            "description": "zip_code",
            "required": "true",
        }],
        operations=dict(
            get=dict(
                responses=init_swagger_response('ZipCodeSchema')
            )
        )
    )

    spec.path(
        path=vehicle_feature_ctrl.url_prefix + "/engines",
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('VehicleEngineSchema')
            )
        )
    )

    spec.path(
        path=vehicle_feature_ctrl.url_prefix + "/bodies",
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('VehicleBodySchema')
            )
        )
    )

    spec.path(
        path=vehicle_feature_ctrl.url_prefix + "/drive_trains",
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('VehicleDriveTrainSchema')
            )
        )
    )

    spec.path(
        path=vehicle_feature_ctrl.url_prefix + "/transmissions",
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('VehicleTransmissionSchema')
            )
        )
    )

    spec.path(
        path=dealer_ctrl.url_prefix,
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('DealerSchema')
            )
        )
    )

    spec.path(
        path=dealer_ctrl.url_prefix + '/{dealer_id}',
        parameters=[{
            "name": "dealer_id",
            "in": "path",
            "description": "DealerId",
            "required": "true",
        }],
        operations=dict(
            put=dict(
                parameters=[
                    {
                        "name": "DealerBody",
                        "in": "body",
                        "schema": "DealerSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('DealerSchema')
            ),
            get=dict(
                responses=init_swagger_response('DealerSchema')
            ),
            delete=dict(
                responses=init_swagger_response('DealerSchema')
            )
        )
    )

    spec.path(
        path=dealer_ctrl.url_prefix,
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "DealerBody",
                        "in": "body",
                        "schema": "DealerSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('DealerSchema')
            ),
        )
    )

    spec.path(
        path=dealer_scheduler_ctrl.url_prefix,
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('DealerSchedulerSchema')
            )
        )
    )

    spec.path(
        path=dealer_scheduler_ctrl.url_prefix + '/{dealer_scheduler_id}/month/{month_num}',
        parameters=[{
            "name": "dealer_scheduler_id",
            "in": "path",
            "description": "DealerSchedulerId",
            "required": "true",
        }, {
            "name": "month_num",
            "in": "path",
            "description": "Number Of Month",
            "required": "true",
        }],
        operations=dict(
            get=dict(
                responses=init_swagger_response('DealerSchedulerSchema')
            )
        )
    )

    spec.path(
        path=dealer_scheduler_ctrl.url_prefix + '/{dealer_scheduler_id}',
        parameters=[{
            "name": "dealer_scheduler_id",
            "in": "path",
            "description": "DealerSchedulerId",
            "required": "true",
        }],
        operations=dict(
            put=dict(
                parameters=[
                    {
                        "name": "DealerSchedulerBody",
                        "in": "body",
                        "schema": "DealerSchedulerSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('DealerSchedulerSchema')
            ),
            get=dict(
                responses=init_swagger_response('DealerSchedulerSchema')
            ),
            delete=dict(
                responses=init_swagger_response('DealerSchedulerSchema')
            )
        )
    )
    spec.path(
        path=dealer_scheduler_ctrl.url_prefix,
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "DealerBody",
                        "in": "body",
                        "schema": "DealerSchedulerSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('DealerSchedulerSchema')
            ),
        )
    )

    spec.path(
        path=dealer_request_ctrl.url_prefix,
        operations=dict(
            get=dict(
                parameters=query_list_params,
                responses=init_swagger_response('DealerRequestSchema')
            )
        )
    )

    spec.path(
        path=dealer_request_ctrl.url_prefix + '/{dealer_request_id}',
        parameters=[{
            "name": "dealer_request_id",
            "in": "path",
            "description": "DealerRequestId",
            "required": "true",
        }],
        operations=dict(
            put=dict(
                parameters=[
                    {
                        "name": "DealerRequestBody",
                        "in": "body",
                        "schema": "DealerRequestSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('DealerRequestSchema')
            ),
            get=dict(
                responses=init_swagger_response('DealerRequestSchema')
            ),
            delete=dict(
                responses=init_swagger_response('DealerRequestSchema')
            )
        )
    )
    spec.path(
        path=dealer_request_ctrl.url_prefix,
        operations=dict(
            post=dict(
                parameters=[
                    {
                        "name": "DealerBody",
                        "in": "body",
                        "schema": "DealerRequestSchema",
                        "required": "true",
                    }
                ],
                responses=init_swagger_response('DealerRequestSchema')
            ),
        )
    )

    swagger.init_app(app, spec)
