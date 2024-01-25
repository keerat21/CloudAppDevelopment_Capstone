const express = require('express');
const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

const app = express();
const port = process.env.PORT || 4000;

app.get('/api/dealerships', async (req, res) => {
    try {
        const authenticator = new IamAuthenticator({ apikey: "4H6r5yLf063cqa_eV72hBToLVPfyW40o6wGs7__0Mxq6" });
        const cloudant = CloudantV1.newInstance({
            authenticator: authenticator,
            serviceUrl: "https://f19604d8-0e51-42b7-89d0-960ab5ae6cb5-bluemix.cloudantnosqldb.appdomain.cloud"
        });

        // client.getDatabaseInformation({ db: "dealerships" }).then((dbInfo) => {
        //     const documentCount = dbInfo.result.doc_count;
        //     const dbNameResult = dbInfo.result.db_name;});

        // if(documentCount==0)
        // res.status(404).json({ error: "The database is empty" });
        const state = req.query.state;

        const getDocParams = { db: 'dealerships', includeDocs: true };
        const response = await cloudant.postAllDocs(getDocParams);

        if (state) {
            // Initialize an array to store the matching documents
            var stateReturn = [];

            for (const [key, document] of Object.entries(response.result)) {
                // Check if the document has a "rows" property
                if (key === "rows") {
                    for (const doc of Object.values(document)) {
                        for (const [key, element] of Object.entries(doc)) {
                            if (key === "doc") {
                                for (const [key, info] of Object.entries(element)) {
                                    if (key == "state") {
                                        if (info.toLowerCase() === state) {
                                            // Check if the row has a "doc" property and if the "state" matches
                                            stateReturn.push(element);
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

            // Send the array of matching documents as a JSON response
            await res.json(stateReturn);
        } else {
            res.json(response.result);
        }

    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
