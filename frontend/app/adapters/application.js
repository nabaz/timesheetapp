import DRFAdapter from './drf';

export default DRFAdapter.extend({
  namespace: 'api',
  addTrailingSlashes: false
});
