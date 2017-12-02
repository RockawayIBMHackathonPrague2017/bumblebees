import { handleActions } from 'redux-actions';

const tipsReducers = handleActions({
    'FETCH_DEMO_PRODUCTS_SUCCEEDED': (state, action) => action.payload.data.docs,
}, []);

export default tipsReducers;
