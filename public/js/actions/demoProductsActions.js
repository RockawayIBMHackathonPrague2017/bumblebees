import { createActionThunk } from 'redux-thunk-actions';
import * as api from '../api';

const getDemoProduct = createActionThunk('FETCH_DEMO_PRODUCT', (productId) => api.getDemoProduct(productId));
const getMobiles = createActionThunk('FETCH_DEMO_PRODUCTS', () => api.getMobiles());
const getPCs = createActionThunk('FETCH_DEMO_PRODUCTS', () => api.getPCs());

export default {
    getDemoProduct,
    getMobiles,
    getPCs,
};
