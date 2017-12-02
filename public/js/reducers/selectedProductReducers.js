import { handleActions } from 'redux-actions';

const selectedProductReducers = handleActions({
    'FETCH_DEMO_PRODUCT_SUCCEEDED': (state, action) => action.payload.data.docs[0],
    'STORE_SELECTED_PRODUCT': (state, action) => action.payload,
}, {});

export default selectedProductReducers;
