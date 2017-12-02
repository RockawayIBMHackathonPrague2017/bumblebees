import { compose, join, splitEvery, reverse } from 'ramda';

export default compose(reverse, join(' '), splitEvery(3), reverse)