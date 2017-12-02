import React from 'react';
import PropTypes from 'prop-types';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { map, take } from 'ramda';
import { Loader, ProductCard, ProductDetail, RequestForm, SelectBox } from '../components';
import { demoProductsActions } from '../actions';
import { tipsSelectors } from '../selectors';

class Layout extends React.Component {

    constructor(props) {
        super(props);
    }

    componentDidMount() {
        this.props.getMobiles();
    }

    _handleMobilesClick = (event) => this.props.getMobiles();
    _handlePCsClick = (event) => this.props.getPCs();

    render() {
        return (
            <main>
                <div className="container">
                    {this.props.showSpinner ?
                        <Loader /> :
                        <ProductDetail />
                    }
                    <div className="recommended">
                        <h2>Náš tip na lepší výrobek</h2>
                        { this.props.showSpinner ?
                            <Loader /> :
                            <section className="products">
                                {map(renderProductCards, this.props.tips)}
                            </section>
                        }
                        <h2>Demo dashboard</h2>
                        <section>
                            <RequestForm />
                            <SelectBox />
                            <button onClick={this._handleMobilesClick}>Mobiles</button>
                            <button onClick={this._handlePCsClick}>PCs</button>
                        </section>
                    </div>
                </div>
            </main>
        )
    }

}

const renderProductCards = (props) => <ProductCard key={props.ITEM_ID} {...props} />;

const mapStateToProps = (state) => ({
    showSpinner: state.showSpinner,
    tips: tipsSelectors.getTips(state),
});

const mapDispatchToProps = (dispatch) => ({
    getMobiles: bindActionCreators(demoProductsActions.getMobiles, dispatch),
    getPCs: bindActionCreators(demoProductsActions.getPCs, dispatch),
});

Layout.propTypes = {
    tips: PropTypes.array,
};

export default connect(mapStateToProps, mapDispatchToProps)(Layout);
