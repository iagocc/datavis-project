import '../styles/index.scss';

import {chart1} from '../scripts/chart1';
import {chart2, populateCountries} from '../scripts/chart2';
import {chart3, updateSelectedCountry} from '../scripts/chart3';

window.onload = function() {
    chart1(updateSelectedCountry);
    populateCountries();
    chart2();
    chart3();
};