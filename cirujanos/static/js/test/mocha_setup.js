mocha.setup('bdd');
var expect = chai.expect;

window.onload = function() {
  mocha.checkLeaks();
  mocha.globals(['jQuery']);
  mocha.run();
};
