# HII-C MongoDB Interface

## Sample Requests

### Storing a new Loupe query:

```
curl -H "Content-Type: application/json" -X POST -d '{"hash": "ABC", "output": [ { "filteredCodes": [ { "code": "118932009", "codeSystem": "SNOMEDCT_US" }, { "code": "13644009", "codeSystem": "SNOMEDCT_US" }, { "code": "280136002", "codeSystem": "SNOMEDCT_US" } ] } ] }' http://localhost:5000/loupe_query
```

### Retrieving a cached Loupe query:

```
curl localhost:5000/loupe_query/ABC
```

### Retrieving a LOINC code:

```
curl localhost:5000/loinc_code/9970-5
```

The JSON response will include the long name for the LOINC term as well as the
system the term belongs to.

## Running with Docker for Development

After cloning into the git repository, first run this command:

```
docker build -t p3000/mongo-proxy:latest .
```

Then, run the following command to start the container:

```
docker run -d -e DB="mongodb://username:password@host.example.com:27017" -p 3060:5000 p3000/mongo-proxy:latest
```

## Production Deployment with Docker

A live instance is currently deployed at http://mongo-proxy.healthcreek.org, physically running on docker01.healthcreek.org at ASU BMI. The command string is only slightly different.

```
docker run -d -p 3060:5000 --name mongo-proxy --restart unless-stopped -e "DB=mongo://admin:the_password@db01.healthcreek.org" p3000/mongo-proxy:latest
```


Now, you should be able to connect to the API through the browser at
[localhost:3060](localhost:3060).
