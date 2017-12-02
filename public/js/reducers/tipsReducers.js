import { handleActions } from 'redux-actions';

const tipsReducers = handleActions({
    'FETCH_TIPS_SUCCEEDED': (state, action) => action.payload.data.docs,
}, []);

export default tipsReducers;
