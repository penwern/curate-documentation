## OAI-PMH Server

Curate can be configured to expose records in your Curate instance to harvesters and other systems that support OAI-PMH. This allows them to harvest metadata from your records and make it available to other systems.

### Setting up an OAI-PMH Server

To enable your Curate instances OAI-PMH server, you will need to contact support to discuss the configuration. If you are a new customer, please notify us of your requirement for an OAI-PMH server during your onboarding process. If you are an existing customer who is now looking to integrate an OAI-PMH server with Curate, please create a support ticket and a representative will be in touch to configure the connection.

By default, Curate will expose your OAI-PMH server at the following recommended URL: https://your-curate-instance.com/oai

Queries can then be made to this URL using the OAI-PMH protocol. For more information on the OAI-PMH protocol, please see the [OAI-PMH website](https://www.openarchives.org/OAI/openarchivesprotocol.html).

**By default, Curate will expose your OAI-PMH server to the public. If you would like to restrict access to your OAI-PMH server, please contact support to discuss the configuration.**

### Enabling OAI-PMH Harvesting for a Record

To expose a record via OAI-PMH, you just need to select the object which is associated with the metadata you would like to expose, open the metadata panel in the object information area, and then open the "Export" section. You can then enable the "Enable OAI-PMH Harvesting" option, and Curate will automatically expose the record to harvesters. If your change the harvesting option for a folder, then Curate will ask if you would also like to apply the option to the folders immediate file (not folder) children.

Each of your enabled records will then be discoverable by OAI-PMH queries to your Curate instance that capture them. You can test your OAI-PMH server by sending a basic listRecords query to it with a metadata prefix that matches one of the supported schemas (oai_dc or oai_ead). For more information on the OAI-PMH protocol, please see the [OAI-PMH website](https://www.openarchives.org/OAI/openarchivesprotocol.html).
