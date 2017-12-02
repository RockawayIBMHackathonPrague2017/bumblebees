import request from 'axios';

export default (urlSuffix) => request.get(`/filtered/${urlSuffix}`);
