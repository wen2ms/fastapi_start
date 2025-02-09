1. Based on TCP/IP

    HTTP is built on top of the TCP/IP stack.

2. Request-Response Pattern

    HTTP follows client-server modal, where the client(e.g. browser) sends a request and the server sends a response.

3. Stateless 

    The server does not remember previous requests from the same client.
 
4. Persistent/Short Connection

    Persistent Connection(HTTP/1.1 and later) remains open for multiple requests. Uses the Connection: keep-alive header to avoid reopening connections.

    Short Connection (HTTP/1.0) closes after each request-response.
