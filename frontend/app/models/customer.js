import Model from 'ember-data/model';
import attr from 'ember-data/attr'
export default DS.Model.extend({
  name: attr(),
  email: attr(),
  phone: attr(),
  address: attr(),
  status: attr(),
  note: attr()
});
