# PyHTTPServer
Simple HTTP Server using Python

  <h3>Getting started</h3>
  
  Consider you live in an apartment and the apartment can receive mails on it's address. The address consists of Apartment name and  Mailbox number
  Likewise the server has an address consists of  <b><i>HOST (example, localhost) </b></i> and  <b><i>port (example, 8080) </b></i>;
  
  HTTP runs over TCP protocol. Therefore two options  <b><i>AF_INIT </b></i> which stands for IPV4 and  <b><i>SOCK_STREAM </b></i> which stands for TDP are passed to the socket.
  
  <i><b>setsockopt()</b></i> function is for setting socket options. First parameter is the socket layer itself. The second and third parameters mean <b><i>Reuse the address? true</b></i>
    
  Then the address is bound to the socket and the socket is set active to listen for requests from clients.
  
  The loop is for accepting a connection request from client. Requet is accepted using recv().
  
  A response is send back to the client using  <b><i>sendall(response) </b></i>
  
  
  
