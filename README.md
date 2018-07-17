A cache buster for GitHub markdown.

Some image service don't use proper headers which breaks proper cache refresh in GutHub. This service adds Cache-Control:
no-cache header to responses.
More information at: https://github.com/github/markup/issues/224

Service hosted at: https://cache-buster.appspot.com/?redirecturl={your_image_url_here}

Running the service:
- Download SDK: https://cloud.google.com/sdk/docs/quickstart-linux
- Run: google-cloud-sdk/bin/dev_appserver.py ./src/
- Deploy: google-cloud-sdk/bin/gcloud app deploy ./src/app.yaml

