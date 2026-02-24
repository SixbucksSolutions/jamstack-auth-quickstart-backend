# jamstack-auth-quickstart-backend

Serverless REST API backend for the JAMstack Auth Quickstart project

## Prepare API Backend

### Get project domain (Register if needed)

### Create Kinde Application

1. Log into kinde.com
1. Add Application
    * Enter a name
    * Type: "Front-end and mobile", then Save
    * In Quick start, select JavaScript then Save
    * Select Existing codebase tab (under Technology, next to "Starter kit")
    * Where is your project running: "https://[your domain]" and click Set
    * Click Set next to callback URL and logout URL (accept defaults)
    * Note your app-specific Kinde domain (e.g., `https://your-proj.kinde.com`)

### Get TLS cert for API Backend
 
#### Add DNS A/AAAA records

Add A and/or AAAA records for api.[your domain] that point at the host you're running certbot on.

#### Request cert

Using LetsEncrypt but lots of options.

1. Install LetsEncrypt certbot

```bash
sudo apt update
sudo apt install snapd
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

1. Allow port 80 all the way to your box (eg AWS security groups)

```bash
sudo ufw allow 80
```

1. Request backend cert using certbot in standalone HTTP server mode

```bash
sudo certbot certonly --standalone -d api.[your project domain]
```

1. Remove port 80 access

#### Remove DNS A/AAAA records

We'll be doing a CNAME later for this.


### Import the cert into AWS Certificate Manager (ACM)

1. Log into AWS console
1. Switch to region where API will be deployed
1. Go to Certificate Manager
1. Select Import Certificate
  * Paste contents of cert.pem into "Certificate body"
  * Paste contents of privkey.pem into "Certificate private key"
  * Paste contents of chain.pem into "Certificate chain"

Note the ARN for the cert; we'll need this in the next step.

### Modify serverless.yml

* Go to api/
* Update serverless.yml
    * provider.domain.name: api.[your domain]
    * provider.domain.certificateArn: [ARN of imported cert in ACM from last step]
    * provider.httpApi.authorizers.kinde.TokenAuthorizer.issuerUrl: https://[your-project].kinde.com 


## Deploy Backend

### Install Serverless Framework 

### Register/Login to Serverless 

Beyond scope.

### Deploy

```bash
serverless deploy
```

Output will be similar to:

```
endpoints:
  GET - https://8od6x91bvf.execute-api.af-south-1.amazonaws.com/api/v001/ping
  GET - https://8od6x91bvf.execute-api.af-south-1.amazonaws.com/api/v001/user
functions:
  ping: jamstack-auth-quickstart-dev-ping (1.1 kB)
  userGet: jamstack-auth-quickstart-dev-userGet (1.1 kB)
domain:
  name: api.jamstack-auth.publicntp.net
  target: d-tarosfuk7b.execute-api.af-south-1.amazonaws.com
  zone id: Z2DHW2332DAMTN
```

### Add CNAME

api.[your domain] CNAME to d-tarosfuk7b.execute-api.af-south-1.amazonaws.com

### What got deployed

## Test Backend

```
time curl -i -H"Origin: https://jamstack-auth.publicntp.net" https://api.jamstack-auth.publicntp.net/api/v001/ping
```

Result:
```
date: Tue, 24 Feb 2026 12:43:31 GMT
content-type: application/json
content-length: 26
access-control-allow-origin: https://jamstack-auth.publicntp.net
apigw-requestid: ZSV2Bh7CCfMEPSw=

{
    "message": "Pong!"
}
real    0m0.788s
user    0m0.019s
sys     0m0.003s
```

Note: we passed the Origin request header and the API replied saying it was an allowed origin, 
so this is a CORS-friendly API
