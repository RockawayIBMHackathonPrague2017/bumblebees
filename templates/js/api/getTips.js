import request from 'axios';

export default () => request.get('/filter', {
    auth: {
        username: 'b1e62467-67b2-4585-ad3b-c29952fc5392-bluemix',
        password: '8eae19c07e80ce73b90011a9ce3287208bcc06b43c41d42fa65ff2036d802977'
    },
    params: {
        include_docs: true,
    }
});

