function fakeResponse(response, options, callback) {
  var statusCode, headers, server, resp;

  // some default values, so we don't have to set status code and
  // content type all the time.
  statusCode = options.statusCode || 200;
  headers = options.headers || { "Content-Type": "application/json" };

  // we create what Sinon.js calls a fake server. This is basically just
  // a name for mocking out all XMLHttpRequests. (There are no actual
  // servers involved.)
  server = sinon.fakeServer.create();

  // we tell Sinon.js what we want to respond with
  server.respondWith([statusCode, headers, response]);

  callback();

  // this actually makes Sinon.js respond to the Ajax request. As we can
  // choose when to respond to a request, it is for example possible to
  // test that spinners start and stop, that we handle timeouts
  // properly, and so on.
  server.respond();

  server.restore();
}
