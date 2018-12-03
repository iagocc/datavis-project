import '../styles/index.scss';

import {chart1} from '../scripts/chart1';
import {chart2, populateCountries} from '../scripts/chart2';
import {chart3, updateSelectedCountry} from '../scripts/chart3';
import {chart9} from '../scripts/chart9';
import {chart11} from '../scripts/chart11';

window.onload = function() {

    let selectedCountries = ["BRA", "Overall"];
    let selectedCountry = "BRA";

    function updateSelectedCountry(countryCode) {
        selectedCountries = [];
        selectedCountries.push(countryCode);
        selectedCountries.push("Overall");
        selectedCountry = countryCode;

        // Charts that uses selected country
        chart3(selectedCountries);
        chart9(selectedCountry);
    }


    chart1(updateSelectedCountry);
    populateCountries();
    chart2();
    chart3(selectedCountries);
    chart9(selectedCountry);
    chart11();
};