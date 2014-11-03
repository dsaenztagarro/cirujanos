((app, Main)->

  # Dependencies
  Web = app.module "web"
  aboutViews = app.module "about.Views"

  class Main.AppRouter extends Backbone.Router

    initialize: ->
      # pass

    routes:
      "web/": "web"
      "web/pathology/": "pathology"
      "web/procedure/": "procedure"
      "about/": "about"
      "about/contact/": "contact"
      "about/doctor/:doctor/": "aboutDoctor"

    web: ->
      console.log "router:web"
      $('.carouserl').carousel()

    about: ->
      new aboutViews.ContactView()

    contact: ->
      new aboutViews.ContactFormView()
      new aboutViews.GoogleMapsView()

    aboutDoctor: ->
      new aboutViews.DoctorView()

  app.router = new Main.AppRouter()

)(@app, @app.module "main")

Backbone.history.start({ pushState: false, hashChange: false})
