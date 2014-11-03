(function(app, Models) {

  Models.Contact = Backbone.Model.extend({
    urlRoot: "/about/contact/",
    validation: {
      name: {
        required: true,
        msg: "required-field-error"
      },
      email: {
        pattern: 'email',
        msg: "email-format-error"
      },
      phone: {
        required: true,
        msg: "required-field-error"
      },
      message: {
        required: true,
        msg: "required-field-error"
      }
    },
    className: function() {
      return "Contact";
    }
  });

})(this.app, this.app.module("about.Models"));

