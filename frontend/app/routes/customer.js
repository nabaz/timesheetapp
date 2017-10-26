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
  },

  handleSave(customers) {
    return customers.save().catch((e) => {
      if(e.errors[0].status === '409') {
        this.get('handleConflict').perform(customers);
      }
    });
  },
  actions:{
    saveCustomer() {
      let customer = this.store.createRecord('customer', {
        name: "this.getProperties('name')",
        email: "this.getProperties('email')",
        phone: "this.getProperty('phone')",
        note: "asdasds",
        status: "A",
      })

      customer.save();
    }
  }
});
