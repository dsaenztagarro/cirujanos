var i18n = this.app.module("i18n");

_.extend(Backbone.Validation.callbacks, {
  valid: function(view, attr, selector) {
    var context = this._validationContext(view, attr);
    context.$formGroup.removeClass("has-error has-feedback");
    context.$field.next().remove();
  },
  invalid: function(view, attr, error, selector) {
    var context = this._validationContext(view, attr);
    var msg = i18n.es[attr][error];
    context.$formGroup.addClass("has-error has-feedback");
    context.$field.next().remove();
    $("<label class='control-label' for=''>" + msg + "</label>").
      insertAfter(context.$field);
  },
  _validationContext: function(view, attr) {
    var object = view.model.className().toLowerCase(),
        $field = view.$("#" + object + "-" + attr);
    return {
      $field: $field,
      $formGroup: $field.parent()
    };
  }
});

Backbone.$.fn.serializeObject = function() {
  var o = {};
  var a = this.serializeArray();
  $.each(a, function() {
    if (o[this.name] !== undefined) {
      if (!o[this.name].push) {
        o[this.name] = [o[this.name]];
      }
      o[this.name].push(this.value || '');
    } else {
      o[this.name] = this.value || '';
    }
  });
  return o;
};

Backbone.$.ajaxPrefilter(function(options, originalOptions, jqXHR) {
  var token;
  options.xhrFields = {
    withCredentials: true
  };
  // token = $('meta[name="csrf-token"]').attr('content');
  token = this.$("[name='csrfmiddlewaretoken']").val();
  if (token) {
    return jqXHR.setRequestHeader('X-CSRFToken', token);
  }
});
