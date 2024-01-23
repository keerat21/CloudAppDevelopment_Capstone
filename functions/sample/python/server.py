from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests
from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibmcloudant.cloudant_v1 import CloudantV1, Document, AllDocsQuery

param_dict = {
    "URL": "https://f19604d8-0e51-42b7-89d0-960ab5ae6cb5-bluemix.cloudantnosqldb.appdomain.cloud",
    "APIKEY": "4H6r5yLf063cqa_eV72hBToLVPfyW40o6wGs7__0Mxq6",
    "COUCH_USERNAME": "f19604d8-0e51-42b7-89d0-960ab5ae6cb5-bluemix"
}


from flask import Flask, request, jsonify

app = Flask(__name__)
# client = Cloudant.iam(
# account_name=param_dict["COUCH_USERNAME"],
# api_key=param_dict["IAM_API_KEY"],
# connect=True,
# )

authenticator = IAMAuthenticator(param_dict["APIKEY"])
cloudant = CloudantV1(authenticator=authenticator)
cloudant.set_service_url(param_dict["URL"])


# Sample data (replace with your actual data retrieval logic)

@app.route('/api/review', methods=['GET','POST'])
def get_reviews():
    # Get the dealerId from the query parameters
    response = "no post/get"
    if request.method=="GET":
        dealer_id = int(request.args.get('dealerid'))
                # Define a query to retrieve reviews for the specified dealer
        query = {
            "include_docs":True,}

        print(dealer_id)
        response = cloudant.post_find(
        db='reviews',
        selector={"id":dealer_id},
        queries=[query]
        ).get_result()



    if request.method=="POST":
        response = "In POST"
        review_data = request.get_json()
        print(review_data)
        try:
            # Extract review data from JSON request
            

            # Validate required fields
            required_fields = ['id', 'name', 'dealership', 'review', 'purchase', 'purchase_date', 'car_make', 'car_model', 'car_year']
           
            
            if not all(field in review_data for field in required_fields):
                return jsonify({"error": "Incomplete review data. Please provide all required fields."}), 400
            
            # Add the review to Cloudant database
            
            documentadd: Document = Document()
            for attribute in review_data:
                setattr(documentadd, attribute, review_data.get(attribute, None))


            response = cloudant.post_document(db='reviews',document=documentadd).get_result()

            return jsonify({"success": "Review submitted successfully!"})

        except CloudantException as e:
            return jsonify({"error": f"Cloudant error: {e.errors()}"}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=3000)

