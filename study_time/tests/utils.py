from rest_framework.test import APIClient


def get_client(authenticated_user=None):
    client = APIClient()
    if authenticated_user:
        client.force_authenticate(user=authenticated_user)
    return client
