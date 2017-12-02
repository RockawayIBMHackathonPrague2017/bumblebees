/* eslint-disable */
var debug = process.env.NODE_ENV !== 'production';
var webpack = require('webpack');

module.exports = {
    devtool: debug ? 'inline-sourcemap' : null,
    entry: ['babel-polyfill', 'react-hot-loader/patch', './js/app.js'],
    module: {
        rules: [
	        {
		        test: /\.css$/,
		        use: [
			        { loader: 'style-loader' },
			        { loader: 'css-loader' }
		        ]
	        },
            {
                test: /\.jsx?$/,
                loader: 'babel-loader',
                exclude: /(node_modules|bower_components)/,
            },
        ]
    },
    output: {
	    publicPath: '/',
	    filename: './build/bundle.js',
    },
	devServer: {
    	contentBase: './',
		historyApiFallback: true,
		port: '3333'
	},
	plugins: debug ? [
		new webpack.NamedModulesPlugin(),
	] : [
        new webpack.DefinePlugin({
            'process.env': {
                // This has effect on the eit-app lib size
                'NODE_ENV': JSON.stringify('production'),
            }
        }),
        new webpack.optimize.AggressiveMergingPlugin(),
        new webpack.optimize.OccurrenceOrderPlugin(),
        new webpack.optimize.DedupePlugin(),
        new webpack.optimize.UglifyJsPlugin({
            mangle: true,
            compress: {
                warnings: false, // Suppress uglification warnings
                pure_getters: true,
                unsafe: true,
                unsafe_comps: true,
                screw_ie8: true
            },
            output: {
                comments: false,
            },
            exclude: [/\.min\.js$/gi], // skip pre-minified libs
            sourceMap: false
        }),
        new webpack.IgnorePlugin(/^\.\/locale$/, [/moment$/])
    ],
};
