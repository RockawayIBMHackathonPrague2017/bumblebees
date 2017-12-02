import React from 'react';
import { HashRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from '../store';
import { Layout } from '../containers';

const RootContainer = () =>
	<Provider store={store}>
		<HashRouter>
			<Layout />
		</HashRouter>
	</Provider>;

export default RootContainer;
