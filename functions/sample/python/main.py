"""IBM Cloud Function that gets all reviews for a dealership

Returns:
    List: List of reviews for the given dealership
"""
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests


param_dict = {
    "COUCH_URL": "https://f19604d8-0e51-42b7-89d0-960ab5ae6cb5-bluemix.cloudantnosqldb.appdomain.cloud",
    "IAM_API_KEY": "4H6r5yLf063cqa_eV72hBToLVPfyW40o6wGs7__0Mxq6",
    "COUCH_USERNAME": "f19604d8-0e51-42b7-89d0-960ab5ae6cb5-bluemix"
}

def main(param_dict):
    """Main Function

    Args:
        param_dict (Dict): input paramater

    Returns:
        _type_: _description_ TODO
    """

    try:
        client = Cloudant.iam(
            account_name=param_dict["COUCH_USERNAME"],
            api_key=param_dict["IAM_API_KEY"],
            connect=True,
        )
        print(f"Databases: {client.all_dbs()}")
    except CloudantException as cloudant_exception:
        print("unable to connect")
        return {"error": cloudant_exception}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return print({"dbs": client.all_dbs()})


main(param_dict)