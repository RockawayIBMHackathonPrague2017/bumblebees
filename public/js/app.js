import { AppContainer } from 'react-hot-loader';
import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import RootContainer from './root';

axios.defaults.baseURL = 'https://bumblebee.mybluemix.net';

const root = document.getElementById('tips-better-product');

const render = (Component) => ReactDOM.render(
	<AppContainer>
		<Component />
	</AppContainer>,
root);

render(RootContainer);

ReactDOM.render(<RootContainer />, root);

if (module.hot) {
	module.hot.accept('./root', () => {
		const NextRootContainer = require('./root').default;
        render(RootContainer);
	});
}

export default RootContainer;
