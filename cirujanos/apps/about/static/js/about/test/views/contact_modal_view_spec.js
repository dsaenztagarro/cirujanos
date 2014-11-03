var aboutViews = window.app.module("about.Views");

describe("App.About.Views.ContactModal", function() {

  function fillContactForm(view, model) {
    view.$("#contact-name").attr("value", model.name);
    view.$("#contact-email").attr("value", model.email);
    view.$("#contact-phone").attr("value", model.phone);
    view.$("#contact-message").text(model.message);
  }

  before(function() {
    this.$fixture = $(
      "<div id='contact-modal-fixture' class='modal hide fade'>" +
      "</div>"
    );
    this.$template = _.template(
      "<div class='modal-body js-modal-body'>" +
        "<form>" +
          "<div id='alert-container'></div>" +
          "<div class='form-group'>" +
            "<input type='text' id='contact-name' name='name'>" +
          "</div>" +
          "<div class='form-group'>" +
            "<input type='text' id='contact-email' name='email'>" +
          "</div>" +
          "<div class='form-group'>" +
            "<input type='text' id='contact-phone' name='phone'>" +
          "</div>" +
          "<div class='form-group'>" +
            "<textarea id='contact-message' name='message'></textarea>" +
          "</div>" +
          "<button type='button' id='button-cancel'></button>" +
          "<button type='button' id='button-submit'></button>" +
        "</form>" +
      "</div>"
    );
    this.contactExample = {
      name: "John Snow",
      email: "john.snow@gmail.com",
      phone: "000 000 000",
      message: "Message from John Snow"
    };
  });
  beforeEach(function() {
    this.$fixture.empty().appendTo($("#fixtures"));
    this.view = new aboutViews.ContactModalView({
      el: this.$fixture,
      template: this.$template
    });
  });
  afterEach(function() {
    this.view.remove();
    $('#contact-modal-fixture').remove();
  });

  describe("events", function() {
    it("fires events on 'view' click", function() {
      var cancelSpy = sinon.spy(),
          submitSpy = sinon.spy();
      this.view.on({
        "contact:form:cancel": cancelSpy,
        "contact:form:submit": submitSpy
      });
      this.$fixture.find("#button-cancel").click();
      this.$fixture.find("#button-submit").click();
      expect(cancelSpy).to.have.been.calledOnce;
      expect(submitSpy).to.have.been.calledOnce;
    });
  });

  describe("#cancel", function() {
    it("triggers a hide event", function() {
      var hideSpy = sinon.spy();
      this.view.on({ "contact:form:hide": hideSpy });
      this.view.cancel();
      expect(hideSpy).to.have.been.calledOnce;
    });
  });

  describe("#render", function() {
    _.each(["name", "email", "phone", "message"], function(field) {
      it("renders the input " + field + " field", function() {
        expect(this.view.render().$('#contact-' + field).length).to.equal(1);
      });
    });
  });

  describe("#run", function() {
    it("triggers a show event", function() {
      var showSpy = sinon.spy();
      this.view.on({ "contact:form:show": showSpy });
      this.view.run();
      expect(showSpy).to.have.been.calledOnce;
    });
  });

  describe("Click on submit button", function() {
    describe("validations errors", function() {
      _.each(["name", "email", "phone", "message"], function(field) {
        it("shows an error message on empty '" + field + "'", function() {
          this.view.$("#button-submit").trigger("click");
          var $el = this.view.$("#contact-" + field),
              $label = $el.next(),
              $groupClass = $el.parent().prop("class");
          expect(typeof($label)).to.equal("object");
          expect($label.prop("tagName").toLowerCase()).to.equal("label");
          expect($groupClass.indexOf("has-error") > 0).to.equal(true);
          expect($groupClass.indexOf("has-feedback") > 0).to.equal(true);
        });
      });
      describe("multiple validation error submissions", function() {
        _.each(["name", "email", "phone", "message"], function(field) {
          it("shows only one error message on empty '" + field + "'", function() {
            this.view.$("#button-submit").trigger("click");
            this.view.$("#button-submit").trigger("click");
            var $el = this.view.$("#contact-" + field),
                $labels = $el.parent().find("label");
            expect($labels.size()).to.equal(1);
          });
        });
      });
      it("triggers a validation error", function() {
        var errorSpy = sinon.spy();
        this.view.on({ "contact:form:validation:error": errorSpy });
        this.view.$("#button-submit").trigger("click");
        expect(errorSpy).to.have.been.calledOnce;
      });
    })
    describe("validations success", function() {
      beforeEach(function() {
        fillContactForm(this.view, this.contactExample);
      });
      it("triggers a save event", function() {
        var hideSpy = sinon.spy();
        this.view.on({ "contact:form:hide": hideSpy });
        this.view.$("#button-submit").trigger("click");
        expect(hideSpy).to.have.been.calledOnce;
      });
    });
  });

});
