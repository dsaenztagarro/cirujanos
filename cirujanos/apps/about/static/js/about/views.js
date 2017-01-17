(function(app, Views, Models, Templates) {

  Views.ContactView = Backbone.View.extend({
    el: "body",
    initialize: function() {
      this.modal = new Views.ContactModalView();
      this.on({
        "contact:show:form": this.showForm,
      });
    },
    events: {
      'click #contact-show-form': 'clickShowForm'
    },
    clickShowForm: function() {
      this.trigger("contact:show:form");
      return false;
    },
    showForm: function() {
      this.modal.run();
    },
  });

  Views.ContactFormView = Backbone.View.extend({
    el: ".js-contact-form",
    initialize: function() {
      this.on({
        "contact:form:submit": this.submit,
        "contact:form:save": this.save,
        "contact:form:render": this.render
      });
      this.model = new Models.Contact();
      Backbone.Validation.bind(this);
    },
    events: {
      "click #button-submit": "clickSubmit"
    },
    clickCancel: function() {
      this.trigger("contact:form:cancel");
      return false;
    },
    clickSubmit: function() {
      this.trigger("contact:form:submit");
      return false;
    },
    submit: function() {
      this.submitBtn().attr("disabled", "disabled");
      var formData = this.$('form').serializeObject();
      this.model.set(formData);
      if (this.model.isValid(true)) {
        this.trigger("contact:form:save");
      } else {
        this.trigger("contact:form:validation:error");
      }
    },
    save: function() {
      var promise = this.model.save();
      if (promise) {
        promise.then(_.bind(function(data) {
          this.alert = Views.ContactModalView.newSuccessAlertMessage(data);
          this.resetForm();
          this.trigger("contact:form:render");
        }, this)).
        fail(_.bind(function() {
          this.alert = Views.ContactModalView.newErrorAlertMessage();
          this.trigger("contact:form:render");
        }, this));
      }
    },
    resetForm: function() {
      _.each(["name", "email", "phone", "message"], function(field) {
        this.$("#contact-" + field).val("");
      });
    },
    render: function() {
      this.submitBtn().removeAttr("disabled");
      if (this.alert) {
        this.$("#alert-container").empty().append(this.alert.$el);
      }
      return this;
    },
    submitBtn: function() {
      return this.$("#button-submit");
    }
  });

  Views.ContactModalView = Backbone.View.extend({
    className: "modal fade",
    attributes: {
      "id": "#contact-modal",
    },
    template: _.template(Templates.ContactModal),
    initialize: function(options) {
      options = options || {};
      this.on({
        "contact:form:show": this.show,
        "contact:form:hide": this.hide,
        "contact:form:cancel": this.cancel,
      });
      this.model = new Models.Contact();
      Backbone.Validation.bind(this);
      // Render HTML
      var template = options.template || this.template;
      this.$el.html(template());
      // Load Contact Form
      this.formView = new Views.ContactFormView({
        el: this.$(".js-modal-body")
      });
    },
    events: {
      "click #button-cancel": "clickCancel",
    },
    clickCancel: function() {
      this.trigger("contact:form:cancel");
      return false;
    },
    hide: function() {
      this.$el.modal('hide');
    },
    show: function() {
      this.$el.modal();
    },
    cancel: function() {
      this.trigger("contact:form:hide");
    },
    run: function() {
      this.trigger("contact:form:show");
    },
  }, {
    newSuccessAlertMessage: function(context) {
      return new Views.AlertMessageView({
        alertType: "success",
        templateContext: context
      });
    },
    newErrorAlertMessage: function() {
      return new Views.AlertMessageView({
        alertType: "error",
        templateContext: {
          title: "Upss!",
          message: "Parece que se ha producido un error."
        }
      });
    }
  });

  Views.AlertMessageView = Backbone.View.extend({
    className: "alert",
    template: _.template(Templates.AlertMessage),
    initialize: function(options) {
      options = options || {};
      this.on({
        "alert-message:close": this.close,
      });
      // Render HTML
      var template = options.template || this.template;
      this.$el.html(template(options.templateContext));
      this.$el.addClass("alert-" + options.alertType);
    }
  });

  Views.DoctorView = Backbone.View.extend({
    el: "body",
    initialize: function() {
      this.on({
        "doctor:toogle": "toggle"
      });
    },
    events: {
      'click .js-toggle': 'clickToggle'
    },
    clickToggle: function() {
      this.trigger("doctor:toggle");
      return false;
    },
    toggle: function() {
      $(e.currentTarget).parent("div").
        find(".section-details, .js-toggle").toggleClass("hidden");
    }
  });

  Views.GoogleMapsView = Backbone.View.extend({
    el: "#map_canvas",
    initialize: function() {
      var latitude  = $("#location_latitude").val();
      var longitude = $("#location_longitude").val();
      this.myLatlng = new google.maps.LatLng(latitude, longitude);
      this.showMap();
      this.showMarker();
      this.addListener();
    },
    showMap: function() {
      var mapCanvas = this.$el[0];
      var mapOptions = {
        center: this.myLatlng,
        zoom: 16,
        scrollwheel: false,
        // navigationControl: false,
        mapTypeControl: false,
        scaleControl: false,
        // draggable: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP
      };
      this.map = new google.maps.Map(mapCanvas, mapOptions);
    },
    showMarker: function() {
      this.marker = new google.maps.Marker({
        position: this.myLatlng,
        map: this.map,
        title:"Hello World!"
      });
    },
    addListener: function() {
      google.maps.event.addListener(this.map, 'bounds_changed', _.bind(function() {
        this.offsetCenter(this.myLatlng, 100, 0);
      }, this));
    },
    offsetCenter: function(latlng,offsetx,offsety) {
      // latlng is the apparent centre-point
      // offsetx is the distance you want that point to move to the right, in pixels
      // offsety is the distance you want that point to move upwards, in pixels
      // offset can be negative
      // offsetx and offsety are both optional

      var scale = Math.pow(2, this.map.getZoom());
      var nw = new google.maps.LatLng(
          this.map.getBounds().getNorthEast().lat(),
          this.map.getBounds().getSouthWest().lng()
      );

      var worldCoordinateCenter = this.map.getProjection().fromLatLngToPoint(latlng);
      var pixelOffset = new google.maps.Point((offsetx/scale) || 0,(offsety/scale) ||0);

      var worldCoordinateNewCenter = new google.maps.Point(
          worldCoordinateCenter.x - pixelOffset.x,
          worldCoordinateCenter.y + pixelOffset.y
      );

      var newCenter = this.map.getProjection().fromPointToLatLng(worldCoordinateNewCenter);

      this.map.setCenter(newCenter);
    }
  });
})(this.app,
   this.app.module("about.Views"),
   this.app.module("about.Models"),
   this.app.module("about.templates"));
