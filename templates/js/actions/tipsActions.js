import { createActionThunk } from 'redux-thunk-actions';
import * as api from '../api';

const getTips = createActionThunk('FETCH_TIPS', () => api.getTips());

export default {
    getTips,
};
