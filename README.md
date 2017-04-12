# HII-C MongoDB Interface

## Sample Requests

### Storing a new Loupe query:

```curl -H "Content-Type: application/json" -X POST -d '{"hash": "ABC", "output": [ { "filteredCodes": [ { "code": "118932009", "codeSystem": "SNOMEDCT_US" }, { "code": "13644009", "codeSystem": "SNOMEDCT_US" }, { "code": "280136002", "codeSystem": "SNOMEDCT_US" } ] } ] }' http://localhost:5000/loupe_query
```

### Retrieving a cached Loupe query:

curl localhost:5000/loupe_query/ABC

## Running with Docker

After cloning into the git repository, first run this command:

```
docker build -t hii-c_interface:latest .
```

Then, run the following command to start the container:

```
docker run -d -e DB="---" -p 5000:5000 hii-c_interface:latest
```

**Note:** In the above command, "---" should be replaced with the
connection string for the Mongo DB.

Now, you should be able to connect to the API through the browser at
[localhost:5000](localhost:5000).
