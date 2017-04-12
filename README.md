# HII-C MongoDB Interface

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
