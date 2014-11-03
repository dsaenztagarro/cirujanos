this.app = {
  modules: function() {
    var modules = {};
    return function(name) {
      var full_path = name.split(".");
      var root = modules;
      for (var node in full_path) {
        if (!root[name]) {
          root[name] = {};
        }
        root = root[name];
      }
      return root;
    };
  }
};

this.app.module = this.app.modules();
