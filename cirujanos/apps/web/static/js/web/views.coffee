((app, Web)->

  class Web.NavigationView extends Backbone.View

    # Mandatory options:
    # - el
    # - targetPathname
    initialize: (options)->
      _.extend(@, options)
      # $("body").attr("data-spy", "scroll").attr("data-target", "js-left-nav")
      $('body').scrollspy({ target: '.js-left-nav' })

    events:
      'click .js-link': 'clickLink'

    clickLink: (e)->
      e.preventDefault()
      anchor = $(e.currentTarget).attr('href')
      @navTo(anchor)

    goLink: (idEl)->
      @navTo $(idEl)

    navTo: (anchor)->
      if @targetPathname == window.location.pathname
        @scrollTo(anchor)
      else
        window.location.href = @targetPathname + anchor

    scrollTo: (anchor)->
      if $(anchor).length > 0
        $("html, body").animate({scrollTop: this.getAnchorTop(anchor) }, "slow")


    getAnchorTop: (anchor)->
      headerHeight = 50
      $(anchor).offset().top - headerHeight


)(@app, @app.module "web")
