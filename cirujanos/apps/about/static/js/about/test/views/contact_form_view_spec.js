var aboutViews = window.app.module("about.Views");

describe("App.About.Views.ContactForm", function() {

  function fillContactForm(view, model) {
    view.$("#contact-name").attr("value", model.name);
    view.$("#contact-email").attr("value", model.email);
    view.$("#contact-phone").attr("value", model.phone);
    view.$("#contact-message").text(model.message);
  }

  before(function() {
    this.$fixture = $(
      "<div id='contact-form-fixture'>" +
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
    this.$fixture.appendTo($("#fixtures"));
    this.view = new aboutViews.ContactFormView({
      el: this.$fixture,
    });
  });
  afterEach(function() {
    this.view.remove();
    $('#contact-form-fixture').remove();
  });

  describe("events", function() {
    it("fires events on 'view' click", function() {
      var submitSpy = sinon.spy();
      this.view.on({
        "contact:form:submit": submitSpy
      });
      this.$fixture.find("#button-submit").click();
      expect(submitSpy).to.have.been.calledOnce;
    });
  });

  describe("#submit", function() {
    it("disables submit button", function() {
      this.view.submit();
      var disabledValue = this.view.$("#button-submit").attr("disabled");
      expect(disabledValue).to.equal("disabled");
    });
    describe("validations errors", function() {
      _.each(["name", "email", "phone", "message"], function(field) {
        it("shows an error message on empty '" + field + "'", function() {
          this.view.submit();
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
            this.view.submit();
            this.view.submit();
            var $el = this.view.$("#contact-" + field),
                $labels = $el.parent().find("label");
            expect($labels.size()).to.equal(1);
          });
        });
      });
      it("triggers a validation error", function() {
        var errorSpy = sinon.spy();
        this.view.on({ "contact:form:validation:error": errorSpy });
        this.view.submit();
        expect(errorSpy).to.have.been.calledOnce;
      });
    });
    describe("validations success", function() {
      beforeEach(function() {
        fillContactForm(this.view, this.contactExample);
      });
      it("triggers a save event", function() {
        var hideSpy = sinon.spy();
        this.view.on({ "contact:form:hide": hideSpy });
        this.view.submit();
        expect(hideSpy).to.have.been.calledOnce;
      });
    });
  });

  describe("#save", function() {
    describe("events", function() {
      beforeEach(function() {
        this.saveSpy = sinon.spy(aboutViews.ContactFormView.prototype, "save");
        this.view = new aboutViews.ContactFormView();
        sinon.stub(this.view.model, "save", function() {
          return false;
        });
      });
      afterEach(function() {
        this.saveSpy.restore();
      });
      it("is called when a save event is triggered", function() {
        this.view.trigger("contact:form:save");
        expect(this.saveSpy.calledOnce).to.equal(true);
      });
    });
    describe("server response", function() {
      beforeEach(function() {
        fillContactForm(this.view, this.contactExample);
        this.view.model.set(this.contactExample);
      });
      describe("sucess server response", function() {
        beforeEach(function() {
          var json_string = '{ "title": "ok", "message": "success" }';
          fakeResponse(json_string, {}, _.bind(function() {
            this.view.save();
          }, this));
        });
        it("shows a success message", function() {
          var $alert = this.view.$(".alert.alert-success");
          expect($alert.length).to.equal(1);
        });
        it("takes the message from response", function() {
          var $alert = this.view.$(".alert.alert-success");
          expect($alert.text()).to.equal("oksuccess");
        });
        _.each(["name", "email", "phone", "message"], function(field) {
          it("clears the input " + field + " field", function() {
            expect(this.view.$("#contact-" + field).val()).to.equal("");
          });
        });
      });
      describe("error server response", function() {
        beforeEach(function() {
          fakeResponse('{ "error": "" }', { statusCode: 500 }, _.bind(function() {
            this.view.save();
          }, this));
        });
        it("shows an error message", function() {
          var $alert = this.view.$(".alert.alert-error");
          expect($alert.length).to.equal(1);
        });
        it("shows last error message on multiple error calls", function() {
          fakeResponse('{ "error": "" }', { statusCode: 500 }, _.bind(function() {
            this.view.save();
          }, this));
          var $alert = this.view.$(".alert.alert-error");
          expect($alert.length).to.equal(1);
        });
        it("keeps the fields with the user information", function() {
        });
      });
    });
  });

  describe("#render", function() {
    _.each(["name", "email", "phone", "message"], function(field) {
      it("renders the input " + field + " field", function() {
        expect(this.view.render().$('#contact-' + field).length).to.equal(1);
      });
    });
    it("enables submit button case it is disabled", function() {
      this.view.$("#button-submit").attr("disabled", "disabled");
      this.view.render();
      var disabledValue = this.view.$("#button-submit").attr("disabled");
      expect(disabledValue).to.equal(undefined);
    });
  });
});
