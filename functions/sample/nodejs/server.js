const express = require('express');
const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');
require('dotenv').config(); // Load environment variables from .env file

const app = express();
const port = process.env.PORT || 3000;

app.get('/api/dealerships', async (req, res) => {
  const authenticator = new IamAuthenticator({ apikey: process.env.IAM_API_KEY });
  const cloudant = CloudantV1.newInstance({
    authenticator: authenticator
  });
  cloudant.setServiceUrl(process.env.COUCH_URL);

  try {
    let dbList = await cloudant.getAllDbs();
    res.json({ dbs: dbList.result });
  } catch (error) {
    res.status(500).json({ error: error.description });
  }
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
