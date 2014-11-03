var aboutViews = window.app.module("about.Views");

describe("App.About.Views.Contact", function() {
  before(function() {
    this.$fixture = $(
      "<div id='contact-fixture'>" +
        "<button type='button' id='contact-show-form'></button>" +
      "</div>"
    );
  });
  beforeEach(function() {
    this.$fixture.empty().appendTo($("#fixtures"));
    this.view = new aboutViews.ContactView({
      el: this.$fixture,
    });
  });
  afterEach(function() {
    this.view.remove();
    $('#contact-fixture').remove();
  });

  it('Should be tied to a DOM element when created.', function() {
    // what html element tag name represents this view?
    expect(this.view.el.tagName.toLowerCase()).to.equal('div');
  });

  describe('events', function() {
    it("fires events on 'view' click", function() {
      var showFormSpy = sinon.spy();
      this.view.on({
        "contact:show:form": showFormSpy
      });
      this.$fixture.find("#contact-show-form").click();
      expect(showFormSpy).to.have.been.calledOnce;
    });
  });

  describe("#showForm", function() {
    it("shows modal with contact form", function() {
      var modal = { run: function () {} },
          mock = sinon.mock(modal),
          deferred = $.Deferred();
      mock.expects("run").once().returns(deferred);
      this.view.modal = modal;
      this.view.showForm();
      mock.verify();
    });
  });
});
