# jamstack-auth-quickstart-backend

Serverless REST API backend for the JAMstack Auth Quickstart project

## Prepare API Backend

### Get project domain (Register if needed)

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
