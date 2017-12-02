import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { map } from 'ramda';
import { ProductCard, SelectBox } from '../components';
import { tipsSelectors } from '../selectors';

const Layout = ({ tips }) =>
    <main>
        <div className="container">
            <div className="recommended">
                <h2>Náš tip na lepší výrobek</h2>
                <section className="products">
                    {map(renderProductCards, tips)}
                </section>
                <section>
                    <SelectBox />
                </section>
            </div>
        </div>
    </main>;

const renderProductCards = (props) => <ProductCard key={props.ITEM_ID} {...props} />;

const mapStateToProps = (state) => ({
    tips: tipsSelectors.getTips(state),
});

Layout.propTypes = {
    tips: PropTypes.array,
};

export default connect(mapStateToProps)(Layout);
