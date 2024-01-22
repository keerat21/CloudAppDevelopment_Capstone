const express = require('express');
const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

const app = express();
const port = process.env.PORT || 3000;

app.get('/api/dealerships', async (req, res) => {
  try {
    const authenticator = new IamAuthenticator({ apikey: "4H6r5yLf063cqa_eV72hBToLVPfyW40o6wGs7__0Mxq6" });
    const cloudant = CloudantV1.newInstance({
      authenticator: authenticator,
      serviceUrl: "https://f19604d8-0e51-42b7-89d0-960ab5ae6cb5-bluemix.cloudantnosqldb.appdomain.cloud"
    });

    client.getDatabaseInformation({ db: "dealerships" }).then((dbInfo) => {
        const documentCount = dbInfo.result.doc_count;
        const dbNameResult = dbInfo.result.db_name;});

        if(documentCount==0)
        res.status(404).json({ error: "The database is empty" });
    const state = req.query.state;

    if (!state){
        const getDocParams = { db: 'dealerships',
        includeDocs: true,
        limit: 10 };
        cloudant.postAllDocs(getDocParams).then(response => {
            res.json(response.result);
          });}
    if (state) {
        query = {
            selector: {
              state: state
            },
            limit: 10
          };
              // Fetch documents from Cloudant based on the state query parameter
    const response = await cloudant.postFind({
        db: 'dealerships',
        selector: query.selector,
        limit: query.limit
      });
  
      res.json(response.result.docs);
    }



  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
