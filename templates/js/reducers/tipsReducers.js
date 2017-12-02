import { handleActions } from 'redux-actions';

const tipsReducers = handleActions({
    'FETCH_TIPS_SUCCEEDED': (state, action) => ({ tips: action.payload.data }),
}, []);

export default tipsReducers;
