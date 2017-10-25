import Ember from 'ember';
import Route from '@ember/routing/route';

export default Route.extend({
  model(params) {
    return Ember.RSVP.hash({
      customers: this.store.findAll('customer'),
    })
  },
  setupController(controller, model){
    controller.set('customers', model.customers);
  }


});
