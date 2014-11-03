var aboutModels = this.app.module("about.Models");

describe("App.About.Models.Contact", function() {

  describe("#className", function() {
    it("returns the class name as a string", function() {
      var contact = new aboutModels.Contact();
      expect(contact.className()).to.equal("Contact");
    });
  });

  describe("#save", function() {
    beforeEach(function() {
      this.contact = new aboutModels.Contact({
        "name":"John Snow",
        "email": "john.snow@gmail.com",
        "phone": "000 000 000",
        "message": "john.snow@gmail.com",
      });
      this.server = sinon.fakeServer.create();
      this.responseBody  = '{}';
      this.server.respondWith(
        "POST",
        "/about/contact/",
        [200, { "Content-Type": "application/json" }, this.responseBody]
      );
    });
    afterEach(function() {
      this.server.restore();
    });
    it("should save contact", function() {
      this.contact.save();
      var request = this.server.requests[0];
      expect(request.method).to.be.equal("POST");
      expect(request.url).to.be.equal("/about/contact/");
      expect(request.requestBody).to.be.equal(JSON.stringify(this.contact.attributes));
    });
  });
});
