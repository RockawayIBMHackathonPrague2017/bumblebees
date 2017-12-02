import request from 'axios';

export default (productId) => request.get(`/id/${productId}`);
