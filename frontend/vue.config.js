module.exports = {
    configureWebpack: {
        devServer: {
            // https://github.com/vuejs-templates/webpack/issues/378
            watchOptions: {
                poll: true,
            },
        },
    }
};
