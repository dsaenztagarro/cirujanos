((app, templates)->

  templates.AlertMessage = """
    <strong><%= title %></strong><%= message %>
  """

  templates.ContactModal = """
    <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
          <h4 class="modal-title">Contáctanos</h4>
        </div>
        <div class="modal-body js-modal-body">
          <div id="alert-container"></div>
          <form role="form">
            {% csrf_token %}
            <div class="form-group">
              <input type="text" class="form-control" id="contact-name"
                name="name" placeholder="Nombre">
            </div>
            <div class="form-group">
              <input type="email" class="form-control" id="contact-mail"
                name="email" placeholder="Email">
            </div>
            <div class="form-group">
              <input type="text" class="form-control" id="contact-phone"
                name="phone" placeholder="Teléfono">
            </div>
            <div class="form-group">
              <textarea id="contact-message" name="message" class="form-control"
                rows="5" placeholder="Escribe tu mensaje aquí..."></textarea>
            </div>
            <div class="row">
              <div class="span12">
                <br>
                <h4 id="message-response"></h4>
              </div>
            </div>
            <a href="#" class="btn btn-primary" id="button-submit">Enviar</a>
          </form>
        </div>
        <div class="modal-footer">
          <a href="#" class="btn" id="button-cancel">Cancelar</a>
        </div>
      </div>
    </div>
  """

)(@app, @app.module("about.templates"))
