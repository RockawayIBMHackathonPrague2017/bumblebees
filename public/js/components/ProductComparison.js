import React from 'react';
import PropTypes from 'prop-types';
import { isNil, map, toPairs } from 'ramda';

const ProductComparison = ({ LABELS }) =>
        <div className="benefits">
            <ul>
                {map(renderComparison, LABELS)}
            </ul>
        </div>;

const renderComparison = ({VALUE, PARAM}) => <li key={`${PARAM}-${VALUE}`}>{`${PARAM}: ${VALUE}`}</li>;

ProductComparison.propTypes = {
    LABELS: PropTypes.array,
};

export default ProductComparison;
