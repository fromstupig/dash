"use strict";

/*
Custom webpack configuration
Used to add functionality to the default Angular Webpack build
    */

const webpackCommonConfig = require("./webpack-common.config");

module.exports = {
    module: {
        rules: [
            webpackCommonConfig.tailwindWebpackRule,
        ],
    },
};