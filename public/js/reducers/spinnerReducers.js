import { handleActions } from 'redux-actions';

const spinnerReducers = handleActions({
    'FETCH_TIPS_STARTED': (state, action) => { return true; },
    'FETCH_TIPS_ENDED': (state, action) => { return false; },
}, false);

export default spinnerReducers;
