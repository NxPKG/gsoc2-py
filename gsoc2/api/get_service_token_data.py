from requests import Session

from gsoc2.api.models import GetServiceTokenDetailsResponse


def get_service_token_data_req(
    api_request: Session,
) -> GetServiceTokenDetailsResponse:
    """Send request again Gsoc2 API to fetch service token data.
    See more information on https://soc2.khulnasoft.com/docs/api-reference/endpoints/service-tokens/get

    :param api_request: The :class:`requests.Session` instance used to perform the request
    :return: Returns the API response as-is
    """
    response = api_request.get("/api/v2/service-token")

    return GetServiceTokenDetailsResponse.parse_obj(response.json())
