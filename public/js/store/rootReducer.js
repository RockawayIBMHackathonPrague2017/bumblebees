import { combineReducers } from 'redux';
import { demoProductsReducers, selectedProductReducers, spinnerReducers, tipsReducers } from '../reducers';

const rootReducer = combineReducers({
    demoProducts: demoProductsReducers,
    selectedProduct: selectedProductReducers,
    showSpinner: spinnerReducers,
    tips: tipsReducers,
});

export default rootReducer;
