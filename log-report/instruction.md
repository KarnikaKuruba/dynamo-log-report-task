There is an Apache-style access log at /app/access.log in your working directory.
Analyze the traffic and write a JSON summary report to the absolute path
/app/report.json.

The log is in the Common Log Format: each non-empty line begins with the client
IP address and contains a quoted request line such as "GET /example HTTP/1.1".

Your run is successful when all of the following hold:

1. A file exists at /app/report.json.
2. Its contents are a single valid JSON object.
3. The object has an integer field total_requests: the total number of requests
   (non-empty lines) in the log.
4. The object has an integer field unique_ips: the number of distinct client IP
   addresses that made requests.
5. The object has a string field top_path: the request path that was requested
   most often. If several paths tie, any one of the most-requested paths is
   acceptable.

As an illustration of the format only (these values are not the answer), a
report might look like: {"total_requests": 128, "unique_ips": 12, "top_path": "/login"}
