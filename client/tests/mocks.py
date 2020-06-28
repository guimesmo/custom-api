
class MockNoContentResponse:
    status_code = 204


class MockSuccessResponse:
    status_code = 200

    @staticmethod
    def json():
        return {'foo': 'bar'}


class MockNotFoundResponse:
    status_code = 404

    @staticmethod
    def json():
        return {'message': 'not found'}


class MockValidationErrorResponse:
    status_code = 400

    @staticmethod
    def json():
        return {'message': 'validation_error'}


